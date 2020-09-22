<html>
<head>
  Ejercicios PHP
  <script>
    function calificar(){
      alert("correcto");
    }
  </script>
</head>
<body>
    <h1>Primer ejercicio</h1>
    <p>
   
    <form action="">
        <button>Guardar</button>
        Nombre:  <input type="text" name="nom" id="ape">
        <br>Apellido: <input type="text" name="ape" id="ape">
    </form>

    <?php 
        if(isset($_GET["nom"])){ 
              if($_GET["nom"]==""){
                  echo "Ingrese un nombre";
              }  
        }
        if(isset($_GET["ape"])){ 
            if($_GET["ape"]==""){
                echo "Ingrese un apellido";
            }  

      }
      foreach($_GET as $elemento){
        echo "<br>".$elemento;
        $lin=$_COOKIE["migalleta"];  
        echo $lin;
      }
      

    ?>  

    <FORM name="modificador">  <p>Seleccione un color</p>
        <input type="radio" name="color" value="FFFFFF" checked>Blanco <br>
        <input type="radio" name="color" value="F31414">Rojo <br>
        <input type="radio" name="color" value="141BF3">Azul <br>
        <input type="radio" name="color" value="F05B00">Naranja <br>                    
        <input type="Button" name="" value="Cambia Color" onclick="calificar()"> 
    </FORM>

    </p>
</body>
<footer>

</footer>
</html>