<?php 
$servername = "localhost";
$username = "root";
$password = "root";

$dbname = "democtf";

$conn = new mysqli($servername,$username,$password,$dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }
$name=$_GET['name'];
$query="select * from konchan where name='". $name ."';";
echo $query . "\n";
if($result=$conn->query($query)){
  while($obj=$result->fetch_object()){
    print($obj->NAME." ");
  }
}
?>
