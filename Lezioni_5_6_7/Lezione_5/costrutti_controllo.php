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

echo "ISTRUZIONI DI CONTROLLO \n";

$qta_totale = 0;
echo "ISTRUZIONE IF\n";
if($qta_totale == 0){
 echo "Non hai ordinato alcun articolo! \n";
}


if($qta_totale >= 30000)
{
 echo "Hai diritto ad uno sconto del 10% \n";
}



echo "ISTRUZIONE IF-ELSE\n";
if($qta_totale == 0)
{
 echo "Non hai ordinato alcun articolo! \n";
}else {
 echo "Hai oridinato degli articoli! \n";
}

echo "ISTRUZIONE IF-ELSE-IF\n";

if($qta_totale == 0)
{
 echo "Non hai ordinato alcun articolo! \n";
}else if($qta_totale > 0 && $qta_totale <= 10){
 echo "Hai oridinato $qta_totale articoli! \n";
}else {
 echo "Hai oridinato più di 10 articoli! \n";
}


echo "ISTRUZIONE SWITCH\n";
$classe_studente = 1;
switch ($classe_studente) {
	case 1:
		echo "Studente del primo anno \n";
	break;

	case 2:
		echo "Studente del secondo anno \n";
	break;

	case 3:
		echo "Studente del terzo anno \n";
	break;

	case 4:
		echo "Studente del quarto anno \n";
	break;
	case 5:
		echo "Studente del quinto anno \n";
	break;
	
	default:
		echo "Errore, studente senza classe \n";
	break;
}












?>