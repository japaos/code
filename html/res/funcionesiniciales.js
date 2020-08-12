var n=0;
var texto="";
var hora= new Date;
var vector=[0,1,2,3,4,5,6,7,8,9];

for( n=2;n<vector.length;n++){
console.log(vector[n]);

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
