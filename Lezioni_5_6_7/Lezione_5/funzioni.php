<?php
/* 
 Autore: Nome Autore
 Ultima modifica: 10 marzo 2015
 Descrizione dello script: Costrutti
*/


function somma($a,$b){
	$somma = $a + $b;
	return $somma;
}

function  calcSommaGauss($n){
    $somma = $n*($n+1)/2;
    return $somma;
}    

$x = somma(10,20);
echo "\nSOMMA $x\n";
$g = calcSommaGauss(100);
echo "\nSOMMA Gauss di 100 -> $g\n";
