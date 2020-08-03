//funciones en js

function  crear_tabla(){

    document.write("<table width=200 border=1 cellpadding=1 cellspacing=1>"); 
for (i=0;i<temperaturas_cuidades.length;i++){ 
   	document.write("<tr>") 
   	document.write("<td><b>Ciudad " + i + "</b></td>") 
   	for (j=0;j<temperaturas_cuidades[i].length;j++){ 
      	document.write("<td>" + temperaturas_cuidades[i][j] + "</td>") 
   	} 
   	document.write("</tr>") 
} 
document.write("</table>")
}