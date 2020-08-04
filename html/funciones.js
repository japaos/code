//funciones en js

function  crear_tabla(){

	var temperaturas_medias_ciudad0 = [12,10,11] ;
	var temperaturas_medias_ciudad1 = [5,0,2];
	var temperaturas_medias_ciudad2 = [10,8,10];
    var temperaturas_cuidades = [temperaturas_medias_ciudad0,temperaturas_medias_ciudad1,temperaturas_medias_ciudad2];

    document.write("<table width=200 border=1 cellpadding=1 cellspacing=6>"); 
	for (i=0;i<temperaturas_cuidades.length;i++){ 
   	document.write("<tr>")    //tag <tr>  add a new row to the table
   	document.write("<td><b>Ciudad " + i + "</b></td>")  //tag <td>  add a newcolumn to the row
   	for (j=0;j<temperaturas_cuidades[i].length;j++){ 
      	document.write("<td>" + temperaturas_cuidades[i][j] + "</td>") 
   	} 
   	document.write("</tr>") 
} 
document.write("</table>")
}

class Coordenada {
 constructor(x,y){
		this.x=x;
		this.y=y;
 }
comparador(coordenada){
	if(this.x==coordenada.x && this.y==coordenada.y){
		return true;	
	}
	return false;
}
}

class Planeta {
	constructor(x,y){
		   this.nombre=nombre;
		   this.ubicacion=ubicacion;
		   this.satelites=satelites;
		   this.gravedad=gravedad;
		   this.tam=tam;

	}
   mostrar_todo(){
	   var a= new Array(this.nombre,this.ubicacion,this.satelites,this.gravedad,this.tam);
	   alert("Parametros de el objeto"+a);
   }
   calcular(opcion){
       switch(opcion) { 
		   case 1: 
				a=parseInt(window.prompt("digite velocidad del planeta km/h","0"));
				orbita=prompt("Orbita : \nCircular\nEliptica\nNo");
				switch(orbita){
					
				}
				break;
			case 2:


	   }

   }

   }