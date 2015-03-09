python costruisciDati.py > TabellaStudenti.txt
mysqlimport -u edu -pedu --local edudb   TabellaStudenti.txt
-------------------------------------------------------------
-------------------------------------------------------------
# Create DB
CREATE DATABASE edudb;
GRANT ALL PRIVILEGES ON edudb.* TO 'edu'@'localhost' IDENTIFIED BY 'edu' WITH GRANT OPTION;
FLUSH PRIVILEGES; 
