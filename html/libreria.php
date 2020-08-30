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
?>