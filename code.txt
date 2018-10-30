1) Скачать древнюю базу
2) Установить MySQL 5.5
3) Скопировать в новую базу дата-файлы
4) прописать в my.ini параметр secure_file_priv
5) Сэексопртировать в текстовый файл 

SELECT text INTO OUTFILE "C:/Users/konstantin/work/anekdots.txt" FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\r\n###' FROM caneks;

