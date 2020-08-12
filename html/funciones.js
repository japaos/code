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

//creacion de clases por el metodo class:   ---------------------------------
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
	constructor(nombre="X",ubicacion=[0,0,0],satelites=0,gravedad=1,tam=1){
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
				orbita=window.prompt("Orbita : \nCircular\nEliptica\nNo","No");
				switch(orbita){
					case "Circular":
						masa=1.989;
						radio=parseInt(window.prompt("Radio orbita Km: ","1"));

						return(Math.sqrt((this.gravedad*masa)/radio));
						break;
					case "Eliptica":
						masa=1.989;
						radio=parseInt(window.prompt("Radio orbita Km: ","1"));
						semi=parseInt(window.prompt("Semi eje mayor de orbita Km: ","1"));
						vel=Math.sqrt((this.gravedad*masa*2)*((1/radio)-(1/(semi*2))))
						return(vel);
						break;
					default:
						return(0);
						break;
				}
				break;
		   default:
			   return(0);
			   


	   }

   }

   }
   var sistema_solar=[];
   function f1(){
	sistema_solar.push(new Planeta("tierra",[1,1,1],1,9.8,1000)) ;
	sistema_solar.push(new Planeta()) ;
	sistema_solar[0].mostrar_todo();
	sistema_solar[1].mostrar_todo();
	//document.write("<button onclick=tierra.mostar_todo()>Mostrar parametros de "+tierra.nombre+"</boton>");
	
}

//creacion de objetos por el metodo literal antiguo de json

var esfera={
	
	radio:1,angulo:360,
	get datos(){
		return ([this.radio,this.angulo]);
	}, calcular_v :function(){
			return(2*Math.PI*this.radio);
	},
	set datos(r){
        this.radio=r[0];this.angulo=r[1];
	}

}	
	pelota= esfera;
	console.log(pelota.calcular_v())
	console.log(pelota.datos)
	pelota.datos=[11,23];
	console.log(pelota.datos)
	pelota.datos=[12,22];
	console.log(pelota.datos)
	alert("llega hasta aca "+pelota.calcular_v())

