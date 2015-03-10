<?php
/* 
 Autore: Nome Autore
 Ultima modifica: 10 marzo 2015
 Descrizione dello script: Costrutti
*/

/*
Istruzione if
if( condizione ){
 istruzioni
}
*/

echo "ISTRUZIONI DI ITERAZIONE \n";

echo "ISTRUZIONE FOR\n";
$a = 10;
for($x=1;$x<11;$x++){
	$somma = $a + $x;
	echo "Eseguo la somma di a($a) + x($x) per la $x volta -> risultato $somma\n";
}

echo "ISTRUZIONE WHILE\n";
$a = 10;
$x = 0;
$somma = 0;
while($somma < 20){
	$somma = $a + $x;
	$x++;
	echo "Eseguo la somma di a($a) + x($x) per la $x volta -> risultato $somma\n";
}




echo "ISTRUZIONE DO-WHILE\n";
$a = 10;
$x = 0;
$somma = 0;
do{
	$somma = $a + $x;
	$x++;
	echo "Eseguo la somma di a($a) + x($x) per la $x volta -> risultato $somma\n";

}while ($somma <= 20);
