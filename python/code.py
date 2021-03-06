import numpy
import sys
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dropout
from keras.layers import Dense

raw_text = open("/Users/Konstantin/git/JokeGenerator/data/jokes").read()
raw_text = raw_text.replace("\\\n"," ").replace("\n###","\n")

chars = sorted(list(set(raw_text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))
int_to_char = dict((i, c) for i, c in enumerate(chars))

n_chars = len(raw_text)
n_chars = 1000
n_vocab = len(chars)

seq_length = 25
dataX=[]
dataY=[]

for line in raw_text.split("\n"):
    for i in range(0,len(line) - seq_length):
        seq_in = line[i:i+seq_length]
        seq_out = line[i+seq_length]
        dataX.append([char_to_int[c] for c in seq_in])
        dataY.append(char_to_int[seq_out])
n_patterns = len(dataX)
print ("Total patterns:" + str(n_patterns))

X = numpy.reshape(dataX, (n_patterns, seq_length, 1))
X = X / float(n_vocab)
y = np_utils.to_categorical(dataY)


model = Sequential()
model.add(LSTM(256,input_shape=(X.shape[1],X.shape[2]), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(256))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation="softmax"))
model.compile(loss="categorical_crossentropy", optimizer="adam")

model.fit(X, y, epochs=50, batch_size=64)


numpy.random.seed(a=1)


pattern = dataX[25]
pattern
for i in range(1000):
    x = numpy.reshape(pattern, (1, len(pattern), 1))
    x = x / float(n_vocab)
    prediction = model.predict(x, verbose=0)
    index = numpy.argmax(prediction)
    result = int_to_char[index]
    seq_in = [int_to_char[value] for value in pattern]
    sys.stdout.write(result)
    pattern.append(index)
    pattern = pattern[1:len(pattern)]
    

