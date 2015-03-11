#!/bin/bash
#curl https://raw.githubusercontent.com/banzaiberry/leonardo/master/doAll.sh | sh
#curl -Ls http://goo.gl/4IhyLv | sh
#sudo apt-get install gedit -y
#sudo apt-get install apache2 -y
#sudo apt-get install php5 -y
#sudo apt-get install mysql-client -y
#sudo DEBIAN_FRONTEND=noninteractive apt-get install mysql-server -y 
#mysqladmin -u root password leonardo

#cd
#git clone https://github.com/banzaiberry/leonardo.git leonardo
#mysql -u root -pleonardo -e "create database leonardo;";
#mysql -u root -pleonardo -e "GRANT ALL PRIVILEGES ON leonardo.* TO 'leonardo'@'localhost' IDENTIFIED BY 'leonardo' WITH GRANT OPTION;FLUSH PRIVILEGES ;";
#mysql -uleonardo -pleonardo leonardo < /home/pi/leonardo/Lezioni_1_2_3_4/sql/TabellaStudenti.sql

#cd /var/www ; sudo ln -s /home/pi/leonardo/Lezioni_5_6_7/html
cd
sudo sed -i 's/display_errors = Off/display_errors = On/' /etc/php5/apache2/php.ini
sudo service apache2 restart
