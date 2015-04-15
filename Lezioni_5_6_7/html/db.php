<html>
    <head>
        <title></title>
    </head>
    <body>
        <table border='1'>
            <tr><td>Nome</td><td>Cognome</td><td>Matematica</td><td>Italiano</td><td>Scienze</td></tr>

<?php

$user = "root";
$password = "";
$dbname = "leonardo";

$conn = mysqli_connect("localhost", $user, $password, $dbname);

if (mysqli_connect_errno()) {
    die("Connect failed: " . mysqli_connect_error());
}

$query = "SELECT * FROM TabellaStudenti LIMIT 10";

$result = mysqli_query($query, $conn);

while ($row = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
    echo "<tr>";
    echo "<td>".$row['nome']."</td>";
    echo "<td>".$row['cognome']."</td>";
    echo "<td>".$row['votoMatematica']."</td>";
    echo "<td>".$row['votoItaliano']."</td>";
    echo "<td>".$row['votoScienze']."</td>";
    echo "</tr>";
}

mysqli_free_result($result);
mysqli_close($link);

?>

        </table>
    </body>
</html>