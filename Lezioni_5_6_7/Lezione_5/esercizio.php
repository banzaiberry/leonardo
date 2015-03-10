<html>
<head>
<title></title>
</head>
<body>
<?php
function stampa_form($a='',$b=''){
	?>
	<form action="" method="POST">
			A:<input type="text" name="a" value="<?php echo $a?>">
			<select name = "op">
			  <option value="somma">+</option>
			  <option value="divisione">/</option>
			</select>
			B:<input type="text" name="b" value="<?php echo $b?>">
			<input type="submit" value="Calcola">
	</form>
	<?php
}
function stampa_risultato($risultato){
	echo "Risultato: $risultato <br>";
}


function somma($a,$b){
	return $a + $b;
}

function divisione($a,$b){
	return $a / $b;
}




echo "<h1>Operazione</h1>";
$a = 0;
$b = 0;
if(isset($_POST['a']))
	$a = $_POST['a'];

if(isset($_POST['b']))
	$b = $_POST['b'];
stampa_form($a,$b);

$op = false;
$risultato = false;
if(isset($_POST['op']))
	$op = $_POST['op'];

switch ($op) {
	case 'somma':
		$risultato = somma($a,$b);
	break;

	case 'divisione':
		$risultato = divisione($a,$b);
	break;
	
	default:
		$risultato = false;
	break;
}

if($risultato){
	stampa_risultato($risultato);
}

?>


</body>
</html>