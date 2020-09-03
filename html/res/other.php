<?php
session_start();
function sumar(){
          $GLOBALS["car"]=$GLOBALS["car"]+1;
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
        
    </body>
    <footer>

    </footer>
</HTML>