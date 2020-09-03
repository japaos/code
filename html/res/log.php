<?
      session_start();
    ?>
<HTMl>
    
    <HEAd>
        <script>
           function vision(){
                var canvas = document.getElementById("myCanvas");
                var ctx = canvas.getContext("2d");
                ctx.fillStyle = "#FF0000";
                ctx.fillRect(0, 0, 150, 75);
                
            } 
        </script>

    </HEAd>
    <body>
        
        <?php
        if(!$_GET){
            echo "s";
            for($i=0;$i<6;$i++){
                echo "<br><a href=\"log.php?tabla=$i\">Tabla del $i</a>";
            }
        }
        else{
            $tabla=$_GET["tabla"];  
            for($i=0;$i<11;$i++){
                 echo "<br>".$i*$tabla ;   
            }
        }
        if(count($_POST)==3){
            $cliente=$_POST["cliente"];
            $clave=$_POST["clave"];
            echo "<br>variable Cliente: $cliente <br>";
            echo "variable Clave: $clave ";
            $edad=intval($_POST["edad"]);
            if($edad<18){
                echo "<script>alert(\"no puede acceder menor de edad\")</script>";
            }
            else{
                echo "<script>alert(\"bienvenido\")</script>";
            }
            echo  "<form method=\"POST\" action=\"log.php\">";
            echo "<br>Tabla del: <input type=\"number\" name=\"numero\">";
            echo "<input type=\"submit\" value=\"calcular\">";
        }                    
        else{
                for($i=0;$i<11;$i++){
                    echo "<br>".$_POST["numero"]*$i;
                }
        }
            ?>
        
    </body>
</HTMl>