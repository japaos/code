      var personas = 4;
      var importeEntradas = 9.50;
      //alert('Necesitas ' + personas * importeEntradas + ' euros para que entren todos al cine');
      //i=11;
      //for(let i=0; i<1; i++) {
        // en este caso, la variable i sólo existe dentro del bucle for
        //alert(i);  // crea una alerta en ventana la cantidad de veces i definida en el limite del for
      //}
      //document.write(i);

      //let hace que la variable solamente exista en el bloque declarado es decir el espacio con  llaves "{}"
      //var hace que la variable exista ademas que esta sea global y pueda ser consultada en el resto del codigo

      var personas=escape("Texto ISO_1 latin ñ");
      document.write ("<b>"+personas+"</b>"+"tipo de variable : "+typeof personas+"<br>");
      //escape takes a strings and turns to ISO_1 format this format represent caracter specials
      //from the lenguage example ñ o ì and chage to a code like C3  or FF

      document.write("<br>"+isNaN("55f"));
      //isNaN returns a boolean if is a number true other case false
      document.write (parseInt("3F",16));
      //parseInt returns the number in the format ask in the second paramater, if is empty means decimal
      //2: binary   8:octagonal  16:hexagesimal
