<?php
@error_reporting(1);

$db="localhost";
$username="root";
$password= "root";
$dbname= "testdb";

// tao ket noi den db
$conn = new mysqli($db,$username,$password,$dbname);
// kiem tra co loi hay ko
if ($conn->connect_error){
  die("Fail...". $conn->connect_error);
}

// tao query
if(isset($_GET["id"])){
  $id = $_GET["id"];
  $id=preg_replace('/\s+/', '', $id);
  echo $id;
  if(preg_match("/1|2|3|4|5|6|7|8|9|0| |/",$id)){
    die("duck");
  }

  $sql= "select * from users where id=".$id;

  $result = $conn->query($sql);
  echo "<table>";
  echo "<tr><th>id</th><th>username</th></tr>";
  if($result->num_rows > 0){
    while($row = $result->fetch_assoc()){
      echo "<tr>";
      echo "<td>". $row["id"] ."</td>";
      echo "<td>". $row["username"] ."</td>";
      echo "</tr>";
    }
  }
  echo "</table>";
}
?>
