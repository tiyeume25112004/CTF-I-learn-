<?php
if(isset($_GET['source'])){
    highlight_file(__FILE__);
}
if(isset($_GET['konchan'])){
    if(preg_replace("/konchaniscute/","", $_GET["konchan"])==="konchaniscute"){
        echo "flag is KonCTF{ABC_XYZ}";
    }else{
        die("duck");
    }
}
?>
