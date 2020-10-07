
<?php
   // session_register("carrito");
   session_start();
    setcookie("migalleta", "mivalor",time()+(365*24*60*60)); 
    //setcookie("cookie2", "mivalor2", time() + 3600); 
    //setcookie("otracookie", "valorfinal", time() + 3600, "/", ".midominio.com");
?>
<?
header("HTTP/1.0 404 Not Found");
?>
<!doctype html>

<html lang="es">
<head>
  
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <meta charset="UTF-8">
    <title>Primera página PHP</title>
    <script language="javascript">
      function esconder(ide='w3',nombt='b2'){
        var a=document.getElementById(nombt);
        alert (a.value);
        if(a.value=="esconder"){document.getElementById(ide).style.display = 'none';a.value="mostrar";}
        else{document.getElementById(ide).style.display = 'block';a.value="esconder";}
        }
      function sow(){
        document.getElementById('nuevaimg').innerHTML = '<img src="res/circle.png">';}
    </script>        
</head>
<body>
    <h1>Esto es HTML</h1>
    <?php
      include("libreria.php");
      echo '<p>Esto viene de PHP</p>';
      $numero1=1;
      $numero2="33";
      echo $numero1+$numero2;      
      #idioma();
      holis(5);
      $objetivo="texto";$apuntador=&$objetivo;
      echo "<br>Variable objetivo $objetivo";
      echo "<br>Contenido apuntador$apuntador";
      echo "<br>Cuando objetivo cambia objetivo cambia apuntador = nuevo";
      $apuntador="nuevo $objetivo";
      echo "<br>Variable objetivo $objetivo";
      echo "<br>Contenido apuntador$apuntador";
    ?>
    <div id="contenedor">
          <a href="javascript:sow()" id="nuevaimg">Mostrar</a> 

    </div>
    <div id="Botonera">
        <table>
             <tr>
               <td>
                 <a href="res/other.php"><button onclick="">AccionPHP</button></a> 
                 <br><FORm method="POST" action="res/guardar.php">
                 Referencia <input type="text" value="--" name="REF">
                 <br>CC cliente <input type="text" value="--" name="ID">
                 <input type="SUBMIT" value="crear">                 
                 </FORm>
               </td>
               <td>
                  <button>AccionP JS</button> 
                  <br>
                  <FORm method="POST" action="res/buscar.php">
                  REF<input type="text" value="--" name="REF">                  
                  <input type="SUBMIT" value="buscar">                 
                  </FORm>
               </td>
               <td>
                  <?php
                    $as=crearvectorvacio(4,0);
                  ?>
               </td>
             </tr>
             <tr>
              <td>
                <FORM id="phpform">
                      <?php   #la funcion array shift comienza de atras adenlante
                        $entrada = array ("Miguel", "Pepe", "Juan", "Julio", "Pablo");
                        //modifico el tamaño
                        $salida = array_shift ($entrada);
                        //muestro valor guardado dentro salida
                        echo $salida."<br><br>";
                        foreach ($entrada as $actual)
                            echo $actual . "<br>";

                        echo "<p>";
                        //modifico otra vez
                        $salida = array_slice ($entrada, 1);
                        $ubicaciones=scandir("res/");
                        foreach($ubicaciones as $deed){echo "<br>".$deed;}
                        //muestro el array
                        foreach ($salida as $actual)
                            echo $actual . "<br>";                            
                      ?>

                </FORM>
                </td>

                <td>
                    <?php    #comentario  //comentario   /*comentario tambien
                             # la funcion array_slice toma el arreglo y elimina de adelante hacia atras
                             # desde el indice indicado en el primer  numero la cantidad de elementos 
                             #indicados en el segundo elemento  
                      $entrada=array("carlos","julio","juan","sofia","laura");
                      echo $entrada[0]."<br>";
                      $salida=array_slice($entrada,0,3);
                      foreach($salida as $actual)
                          echo $actual."<br>";
                    
                      echo "<br>";
                      $salida=array_slice($entrada,1);
                      foreach($salida as $actual)
                          echo $actual."<br>";

                    ?>
                </td>
                <td>
                    <?php
                        #unset elimina una variable pero si se usa con un array asociativo elimina dicha casilla                      
                        $capitales=array("colombia"=>"bogota","peru"=>"lima","inglaterra"=>"londres","italia"=>array("roma","vaticano"));
                        foreach($capitales as $pais=>$ciudad){
                            if($pais=="italia")
                                {echo $pais."--".$ciudad[0];echo "<br>";}
                            if($pais!="italia")
                                {echo $pais."--".$ciudad;echo "<br>";}
                          }  
                        unset($capitales["italia"]);   
                        foreach($capitales as $pais=>$ciudad){
                          if($pais=="italia")
                              {echo $pais."--".$ciudad[0];echo "<br>";}
                          if($pais!="italia")
                              {echo $pais."--".$ciudad;echo "<br>";}
                        } 
                    ?>
                </td>
                <td>
                    <?php   #array_push() agrega uno o mas elementos a un array
                    $animalitos=array("perro","gato","loro");
                    foreach($animalitos as $animal){
                      echo $animal."<br>";
                    }
                    array_push($animalitos,"pez","mono","canario","serpiente");
                    echo "<br>Array animalitos agregando<br> elementos con la funcion push:<br>";
                    foreach($animalitos as $animal){
                      echo $animal."<br>";
                    }
                    ?>   
                </td>
                <td>
                    <?php
                      #unir multiples arrays
                      $r=array(11,22,33);
                      $g=array(1,3,5);
                      $b=array("w",2,"5");

                      $rgb=array_merge($r,$g,$b);
                      foreach($rgb as $elemento){
                        echo $elemento."<br>";
                      }
                    ?>
                </td>
             </tr>
             <tr>
                 <td>
                  <?php
                    holis(9);
                  ?>
                 </td>     
             </tr>

        </table>
        
    </div>
    <input type="button" id="b1" value="esconder" onclick='esconder("Botonera","b1")'>
    <p>para asignar ver variables de html se usa el parametro _GET de php
    <br>este parametro es una array contiene la informacion correspondiente a<br>
    a las variables enviadas desde http
    </p> 
    <form method="POST" action="paginaphp.php"  enctype="multipart/form-data">
        <input type="file" name="img" id="img">
        <input type="submit" name="subir" value="subir">                
    </form>
    <input type="button" id="b2" value="esconder" onclick='esconder("w3","b2")'>
    <?php
               if(isset($_POST["subir"])){
                 $nombre=$_FILES['img']["name"];
                // echo "s; ".$nombre;
                 //echo "s; ".$_FILES['img']['tmp_name'];
                 if (move_uploaded_file($_FILES['img']['tmp_name'], 'res/'.$nombre)) {
                  //Cambiamos los permisos del archivo a 777 para poder modificarlo posteriormente
                  chmod('res/'.$nombre, 0777);
                  //Mostramos el mensaje de que se ha subido co éxito
                  echo '<div ><b>Se ha subido correctamente la imagen.</b></div>';
                  //Mostramos la imagen subida
                  echo '<div id="w3">p><img src="res/'.$nombre.'"></p><div>';
                  }                    

               }
               else{echo "nada aun";}
        ?>

    Variable "saludo": <?php if($_GET){echo $_GET["saludo"];} ?> 
    <br>
    Variable "texto" <?php if($_GET){echo $_GET["texto"];} ?>
    <br>Lista de elementos almacenados dentro de _GET:<br>
    
    <?php
        //codigo para utilizar la coockie creada llama mi galleta
        foreach($_GET as $elemento){
          echo "<br>".$elemento;
          $lin=$_COOKIE["migalleta"];  
          echo $lin;
        }
        //una sesion es una variable que se almecena en memoria del pc para poder 
        //transmitir durante la navegacion de la pagina solo deja de existir si se cierra el navegador
        //la funcion Session_destroy() elimina todas las varibles de la sesion
        //la funcion Session_unregister('variable') elimina del registro una variable en especifico de la sesion  
        if(isset($_SESSION["carrito"])){
          echo "<br>"."si existe carrito: ";
          echo $_SESSION["carrito"]  ;
          $_SESSION["carrito"]++;  

        }
        else{echo "no existe";
            $_SESSION["carrito"]=0;
        }


    ?>
    <FOrm metod="POST" action="res/ej.php">
       <input type="text" value="--" name="gc">
       <select name="seleccion" id="sel">
         <option value="1">ejercicio1</option>
         <option value="2">ejercicio2</option>
         <option value="1">ejercicio3</option>
       </select>
      <input type="submit" value="carga">
      </FOrm>
</body>
</html>