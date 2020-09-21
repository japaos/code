<?
header("HTTP/1.0 404 Not Found");
?>
<HTML lang="es">
    

<meta charset="UTF-8">  
<HEad>
Guarda
<link rel="stylesheet" type="text/css" href="res/base.css">
</HEad>
<body>
    <div id="contenedor">
        <div id="t">
                contenido dentro del testo
        </div>
        <div id="t1">
                    <?php
                    $ID=$_POST["ID"];echo "<br>ID: $ID";
                    $REF=$_POST["REF"];echo "<br>REF $REF";
                    //Conexion con la base
                    $server=mysqli_connect("localhost","root",""); 
                    if(!$server){
                        echo "no se pudo conectar al servidor".mysql_error();
                    }
                    else{
                        echo "servidor encontrado";
                    }
                    //selección de la base de datos con la que vamos a trabajar 
                    $db=mysqli_select_db($server,"ejemplo"); 
                    $result=mysqli_query($server,"select * from clientes");
                    $flag=1;
                    echo "<br>ID    REF:";
                    while($i=mysqli_fetch_array($result)){
                        echo "<br>".$i["id"];echo "   ".$i["ref"];
                        if($i["id"]==$ID){$flag=0;}
                    }

                    //Ejecucion de la sentencia SQL
                    if($flag){
                        mysqli_query($server,"insert into clientes (ref,id) values ('$REF','$ID')");                    
                    }
                    mysqli_close( $server);
                    ?>
        <h1><div align="center">Registro
        <?php if(!$flag){echo " No ";}?> Insertado</div></h1>
        <div align="center"><a href="lectura.php">Visualizar el contenido de la base</a></div>        
        <script>//window.history.back();</script>                
        </div>
    </div>
</body>

</HTML>


