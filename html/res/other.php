<?php
session_start();
function sumar(){
          $GLOBALS["car"]=$GLOBALS["car"]+1;
}




function verificar_url($url)
{
   //abrimos el archivo en lectura
   $id = @fopen($url,"r");
   //hacemos las comprobaciones
   if ($id) $abierto = true;
   else $abierto = false;
   //devolvemos el valor
   return $abierto;
   //cerramos el archivo
   fclose($id);
}
?>
<?php
////////////////////////////////////////////
//USUARIOS ACTIVOS
//Calcula el numero de usuarios activos
////////////////////////////////////////////

function usuarios_activos()
{
   //permitimos el uso de la variable portadora del numero ip en nuestra funcion
   global $REMOTE_ADDR;

   //asignamos un nombre memotecnico a la variable
   $ip = $REMOTE_ADDR;
   //definimos el momento actual
   $ahora = time();

   //conectamos a la base de datos
   //Usad vuestros propios parametros!!
   $server=mysqli_connect("localhost","root",""); 
   
   $db=mysqli_select_db($server,"ejemplo"); 

   //actualizamos la tabla
   //borrando los registros de las ip inactivas (24 minutos)
   $limite = $ahora-24*60;
   $ssql = "Delete From control_ip Where fecha < ".$limite;
   mysql_query($server,$ssql);

   //miramos si el ip del visitante existe en nuestra tabla
   $ssql = "select ip, fecha from control_ip where ip = '$ip'";
   $result = mysql_query($server,$ssql);
   

   //si existe actualizamos el campo fecha
   if (mysql_num_rows($server,$result) != 0) $ssql = "update control_ip set fecha = ".$ahora." where ip = '$ip'";
   //si no existe insertamos el registro correspondiente a la nueva sesion
   else $ssql = "insert into control_ip (ip, fecha) values ('$ip', $ahora)";

   //ejecutamos la sentencia sql
   mysql_query($server,$ssql);

   //calculamos el numero de sesiones
   $ssql = "select ip from control_ip";
   $result = mysql_query($server,$ssql);
   $usuarios = mysql_num_rows($server,$result);

   //liberamos memoria
   mysql_free_result($server,$result);

   //devolvemos el resultado
   return $usuarios;
   mysqli_close( $server);

}
?>


<HTML>
    <head lang="es">cabeza
        
    </head>
    <body>
        <button>BB</button>
        <?php
            $car=&$_SESSION["carrito"];
            echo "Carrito= ";
            echo $car;
            $car++;

        ?>
    <?php
if (!isset($url))
{
?>
   <FORM name="forma" action="other.php" method="post">
   Indica tu URL:<br>
   <input type="Text" size="25" maxlength="100" name="url" value="http://">
   <input type="Submit" value="Verificar!">
   </FORM>
<?php
}
else
{
   $abierto = verificar_url($url);
   if ($abierto) echo "La URL existe!";
   else echo "La URL no existe o es inaccesible...";
}
?>  
<p>
<?php $active_users = usuarios_activos();
       
       echo "Usuarios activos $active_users";
       echo "Usuarios activos"; 
    ?>
     
</p>  
    </body>
    <footer>
    

    </footer>
</HTML>