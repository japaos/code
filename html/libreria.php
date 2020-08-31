<?php
        function holis($n=0){            
              while($n<10){
                  echo '<br>holis';$n++;
              }  
        }

        function crearvectorvacio($r=0,$c=0){
            $arreglo=array();
            for($i=0;$i<$r;$i++){
                if($c>0){
                    for($j=0;$j<$c;$j++){
                        array_push($arreglo[$i],$j);
                    }
                }
                else{
                    array_push($arreglo,$i);
                }
            }
            if($c>0){
                return $arreglo;  
            }
            else{
                mostrarmatriz($arreglo);
                return $arreglo;
            }            
            
        }
        function mostrarmatriz($array){
            foreach($array as $elemento){
                echo $elemento.'<br>';
            }
        }
        function idioma(){
            #NEGOCIAR EL LENGUAGE DE LA PAGINA CON PHP LA VARIABLE $_SERVER CONTIENE LOS PARAMETROS DE CONEXION
            #DEPENDIENDO DEL INDICE ESCOGIDO EN ESTE CASO EL PARAMETRO 0,2 CONTIENE EL LENGUAGE
            $idioma=substr($_SERVER["HTTP_ACCEPT_LANGUAGE"],0,2);
            $fr="orbua";
            $es="adios";
            $en="bye";
            if($idioma=="es"){
                echo "<script>alert(\"$es\")</script>";

            }
            elseif($idioma=="fr"){
                echo "<script>alert(\"$fr\")</script>";

            }
            else{
                echo "<script>alert(\"$en\")</script>";

            }
        }

?>