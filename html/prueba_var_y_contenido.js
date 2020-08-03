var a=11;
var SS="SS";
var suma=a+SS;
document.write(suma);
var suma=a+SS;
hexagesimal=0xFF
BInario=045

caraggio="hola me llamo carraggio \n aplico el caracter especial \\n como salto de linea \n  el caracter especial  \t \\t como tabulador";
alert(caraggio);
//The specials caracters like \n or  \t  can be visualized when are used in javascripts codes but in html page are no visible this elements 
//if is necessary put a line between text in the web page can be used the <br> tag  means jump line in html


document.write("hexagesimal = "+hexagesimal+"Decimal= "+a+"suma= "+a+hexagesimal);
suma=a+hexagesimal;
document.write("<br>"+"suma real= "+suma)
//when are using the document.write function the operation maked in parentesis are considerated like sring operation so if is neccesary calculate,  have to be before use document.write()
//<br> represent jump line in html
var t=0xF;
var d=0x9;
document.write("<br>"+"d = "+d+"t = "+t)
d=d&t;
document.write("\n\n\n"+"and logica= "+d)

function ver_tipos() {
  
    alert('\nTipos de variables \n t=' + typeof t+"\nss="+typeof SS+"\nsuma="+typeof suma);
    alert(parseInt("12"));  //parseInt convert a string text to a number so it belongs make operations
                            //between string and numbers 
    var i=0 
    while (i<7){ 
        incrementar = prompt("La cuenta está en " + i + ", dime si incremento", "si") 
        if (incrementar == "no") 
            continue 
        i++ 
    }                        
  } 
  
