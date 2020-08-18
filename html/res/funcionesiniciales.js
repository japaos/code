var n=0;
var texto="";
var hora= new Date;
var vector=[0,1,2,3,4,5,6,7,8,9];

// cuando una funcion ejecuta algun cambio tipo html y no se desea refrescar la pagina se debe retornar
// falso en la funcion que corresponde al cambio

//when a function execute any change in the web html format and dont want to refresh the page the function
//has to return a false element and the button that make the funtion has to have retunr before call funtion

for( n=2;n<vector.length;n++){
console.log(vector[n]);

}

function correo(){
    if (document.forms[1].contenido.value == "") 
    {alert("Debe rellenar el formulario") }
 else 
    {document.forms[1].submit() }
    document.forms[1].contenido.defaultValue = "Hola!!" 

    return false
}

function crear(nu){
    switch(nu){
        case 0:    
            var miString = "Hola Amigos" 
            var result = ""        
            for (i=0;i<miString.length-1;i++) { 
                result += miString.charAt(i) 
                result += "-" 
            } 
            result += miString.charAt(miString.length - 1);

            alert(result);
            break;
        case 1:
            document.bgColor="#81F1F3";
            break;
        case 2:
            for(i=0;i<document.images.length;i++){
                console.log(document.images[i]);

            }
            console.log(document.links)

            break;
        case 3:
            console.log(window.scrollbars);
            console.log(window.frames);
            console.log("alto:"+window.innerHeight);
            console.log("ancho: "+window.innerWidth);
            console.log("frames :"+window.length);
            console.log("Location :"+window.location);
            console.log(window.opener);
            console.log(window.status);

            break;
        case 4:
            console.log(confirm("accion?","si"));
            //open();abre una nueva pestaña
            prompt("ingrese nombre","");
            print();  //accion de imprimir la imagen de la pagina actual

            break;
        case 5:
            resizeTo(300,300);
            scroll(1,innerHeight)

            break;
        case 6:
            alert(document.title);
            document.title=prompt("digite nuevo titulo","maketa");
            alert("nuevo titulo: "+document.title);
            break;  
        case 7:
            document.forms[1].contenido.focus();    
            break;
        case 8:
            document.forms[1].contenido.select();
            break;
        case 9:
            checks=document.getElementById("caja");
            if (checks.checked == true){
                console.log("block");
              }
            else{
                console.log("no block");
                }  

             for(var n=0;n<=document.modificador.elements.length-1;n++){
                
                if(document.modificador.elements[n].checked){
                    document.bgColor=document.modificador.elements[n].value;
                }
             }

            break;
        default:
            var miString = "0123456789" 
            var mitad1,mitad2
            
            posicion_mitad = miString.length / 2
            
            mitad1 = miString.substring(0,posicion_mitad) 
            mitad2 = miString.substring(posicion_mitad,miString.length)
            
            document.write(mitad1 + "<br>" + mitad2)
            break;            

    }
}

function calificar(){
    var elemento=document.forms[3].califica.selectedIndex 
    console.log(elemento);
    console.log(document.forms[3].califica.options[elemento].text);
    return false;
}

function arriba(){
//    console.log(document.getSelection());
//    console.log(document.forms[0])
    
    document.forms[0].elements[0].value = 11
    alert(document.getSelection())
}

function opera(o="+"){
    var a=document.forms[0].N1.value;
    var b=document.forms[0].N2.value;
    var res=eval(a+o+b);
    document.forms[0].Res.value=res;
    return false;
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

  