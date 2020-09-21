<?php
    setcookie("migalleta", "mivalor",time()+(365*24*60*60)); 
?>
<?
header("HTTP/1.0 404 Not Found");
?>
<HTML lang="es">
<meta charset="UTF-8">    
<HEad>
Guarda
<link rel="stylesheet" type="text/css" href="basse.css">
<?php
 $REF="";
 $flag=0;
?>
</HEad>
<body>
    <div id="contenedor">
        <div id="t">
            
            <?php
                 $server=mysqli_connect("localhost","root",""); 
                 $db=mysqli_select_db($server,"ejemplo"); 
                 $result=mysqli_query($server,"select * from clientes");
                if(!isset($_GET["nombre"])){
                    $REF=$_POST["REF"];                   
                    while($busqueda=mysqli_fetch_array($result)){
                        if($busqueda["ref"]==$REF){
                            $flag=1;echo "<br>cliente encontrado";
                            echo "REF: $REF"."<br>ID: ".$busqueda["id"];
                            $_COOKIE["encontrada"]=[$REF,$busqueda["id"]];                          
                            break;}
                        else{$flag=0;}
                        
                    }                    
                    if($flag==0){echo "Referencia no encontrada";}
                }
                else{
                    $REF=$_GET["ref"];echo "Dato almacenado";$ID=$_GET["nombre"];
                    if($_GET["nombre"]=="??"){
                        echo "??";
                        $sSQL="Delete From clientes Where ref='$REF'";
                    }
                    else{echo "====";
                        $sSQL="Update clientes Set id='$ID' Where ref='$REF'";
                    }                        
                    mysqli_query($server,$sSQL);
                }

            ?>

        </div>  
        <div id="t1">
        
        
    <?php 
        if(!isset($_GET["nombre"])){  ?>
            <FORM name="forma">
                        <input type="hidden" name="ref" value=<?php echo "\"".$REF."\"";?>>
                        <br><input type="text" name="nombre" id="   nombre" value="--"><button >Modificar</button>                    
                                                           
            </FORM>
            <FORM name="forma">
                        <input type="hidden" name="ref" value=<?php echo "\"".$REF."\"";?>>
                        <input type="hidden" name="nombre" id="   nombre" value="??"><button >Borrar</button>                                                                               
            </FORM>    
        <?php   }

    ?>  
    <button onclick="window.history.back()">Volver</button>   
        </div>
    </div>            

</body>

</HTML>
