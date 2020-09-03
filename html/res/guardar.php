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

                    //Ejecucion de la sentencia SQL
                    mysqli_query($server,"insert into clientes (nombre,telefono) values ('$REF','$ID')");
                    mysqli_close( $server);

                    ?>
        <h1><div align="center">Registro Insertado</div></h1>
        <div align="center"><a href="lectura.php">Visualizar el contenido de la base</a></div>        
        <script>window.history.back();</script>                
        </div>
    </div>
</body>

</HTML>


