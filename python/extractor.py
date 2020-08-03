import sys
import numpy as np
def extraer_texto():
    datx=open('textoextraccion.txt','r').read()
    b=datx.split('\n')
    n=0
    a=[]
    while(n<(len(b)-1)):
        if(not(b[n][0]=='0')):
              a.append((b[n].split('/')[5])[0:b[n].split('/')[5].index('?')])
              
        n=n+1
        
                    
    for t in range(0,len(a)):
            print a[t]        
