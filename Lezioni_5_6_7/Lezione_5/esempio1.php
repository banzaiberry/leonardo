<?php
/* 
 Autore: Nome Autore
 Ultima modifica: 10 marzo 2015
 Descrizione dello script: Esempio che mostra il calcolo della somma Gaussiana calcolata in due modi diversi
*/

define('N',100);

function  calcSommaGauss($n){
    $somma = $n*($n+1)/2;
    return $somma;
}    

print "start\n";
$somma = 0;
for($i=0;$i<(N + 1);$i++){
	$somma = $somma + $i;
	print "$i $somma\n";
}
print "somma: $somma\n";


$x = calcSommaGauss(N);
print "somma Gauss: $x\n";

?>