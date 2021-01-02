<?php   
    require 'res/Classes/PHPExcel/IOFactory.php';
    $server=mysqli_connect("localhost","root",""); 
    if(!$server){
        echo "no se pudo conectar al servidor".mysql_error();
    }
    else{
        echo "servidor encontrado";
    }
    //selección de la base de datos con la que vamos a trabajar 
    $mysqli=mysqli_select_db($server,"ejemplo"); 
    if(mysqli_connect_errno()){
        echo 'error de conexion';
        exit();
    }
    $nombre_archivo='res/consumos.xlsx';
    $objPHPExcel=PHPEXCEL_IOFactory::load($nombre_archivo);
    $hoja=$objPHPExcel->getActiveSheetIndex();

    $valor=$objPHPExcel->getActiveSheet()->getCell('B5');
    echo '<table border 1><tr><td>Equipo</td><td>Costo</td></tr>';
    echo $hoja.$valor;

    $abecedario=array('a','b','c');
    $abecedario[6]='g';
    echo '<br>'.$abecedario[5];
?>