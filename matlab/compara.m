function [m]=compara(matriz,fila,col)
tam=size(matriz);
A=fila;B=col;m=zeros(A,B);
 if tam(1)==A
    fprintf ('long adecuada');
 elseif tam(1)<A
     m=cat(1,matriz,zeros(A-tam(1),tam(2)));
 else 
     m=matriz(1:A,1:tam(2));
 end
  if tam(2)==B
     fprintf ('ancho adecuado');
  elseif tam(2)<B
      m=cat(2,m,zeros(A,B-tam(2)));
  else 
      m=m(1:A,1:B);
  end
end 