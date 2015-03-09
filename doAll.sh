#!/bin/bash
echo "installo gedit"
#sudo apt-get install gedit -y
#sudo apt-get install apache2 -y
#sudo apt-get install php5 -y
sudo apt-get install mysql-client -y
export DEBIAN_FRONTEND=noninteractive
sudo -q -y apt-get install mysql-server
mysqladmin -u root password leonardo


cd
git clone https://github.com/banzaiberry/leonardo.git leonardo
mysql -u root -pleonardo -e "create database leonardo;";
mysql -u root -pleonardo -e "GRANT ALL PRIVILEGES ON leonardo.* TO 'leonardo'@'localhost' IDENTIFIED BY 'leonardo' WITH GRANT OPTION;FLUSH PRIVILEGES ;";
mysql -uleonardo -pleonardo leonardo < /home/pi/leonardo/Lezioni_1_2_3_4/sql/TabellaStudenti.sql