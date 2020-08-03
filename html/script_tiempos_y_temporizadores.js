fecha = new Date() 
var seg=fecha.getSeconds();
var n=0;
while(n<2){
    seg=fecha.getSeconds();
    n++;document.writeln("<li style=\"background-color:rgb(27, 60, 206);color:red;\">"+seg+" tipo "+typeof seg+"</li>");
    
}

//Date().getSeconds() returns seconds of pc clock Day:Month:Year:Hour:Second

seg=fecha.getDay();
if(seg==1){
    alert("que tengas un feliz comienzo de semana");
}
if(seg==6){
    alert("que tengas un feliz fin de semana");
}
switch(d){
    case 1: 
       document.write("numero 1")
       break
    case 2: 
       document.write("numero 2");
       break
    case 1: 
       document.write("numero 3");
       break
    default:
        document.write("otro numero")
}

var arre = new Array(3) 

arre[0] = Math.random();
arre[1] = "texto"
arre[2] = 0x499 

for (i=0;i<3;i++){ 
    document.write("<li>"+"Posición " + i + " del array: " + arre[i]+"</li>") 
    //document.write("<br>") 
}

//document.write("<li>"+"Texto del arreglo en la posiciòn 1: " + arre[1] + " longitud del texto " + arre[i].length()+"</li>"); 
//document.write("<li>"+"Texto del arreglo en la posiciòn 1: " + arre[0] + " tipo de dato " + typeof(arre[0])+"</li>"); 
//length only is a function for array so i have to find other option in this case   
