import threading
import numpy as np
import cv2


captura = cv2.VideoCapture(0)
vector=[range(1,11),range(10,21),range(100,111)]
img = cv2.imread('C:\Desert.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
li=img


nido=''
mensaje=['']
for den in range(len(img)):
	mensaje.append('')
blanco=mensaje
fin=0
n=0
rango=[0,(len(img)+1)/3,(len(img)+1)*2/3,len(img)]
##print(len(blanco),len(blanco[0]))
##def worker(den):
##    global mensaje,n,rango,blanco
##    """funcion que realiza el trabajo en el thread"""
##    while fin==0:
##        mensaje=blanco
##        for cont in range(rango[den],rango[den+1]):
##               for den1 in range(1,len(img[0])):
##                       mensaje[cont]=mensaje[cont]+chr(img[cont][den1])                       
##    n=n+1   
##    return
##threads = list()
##for i in range(3):
##    t = threading.Thread(target=worker, args=(i,))
##    threads.append(t)
##    t.start()
##    
##print('workers iniciados listos para operar')

##n=0
##
##fin=0
##g=0
##def worker(den):
##    global fin,g,n
##    """funcion que realiza el trabajo en el thread"""
##    while fin==0:     
##         img[den]=den+g
##    n=n+1
##    return
##threads = list()
##for i in range(len(img)):
##    t = threading.Thread(target=worker, args=(i,))
##    threads.append(t)
##    t.start()
##
##print('worker operando')

fin=input('ingrese numero mayor 0 para acabar workers')


def mostrar2(nombre):
 global img,li
 while True:   
    cv2.imshow('imagen',li)
 #   time.sleep(0.1)
    op=cv2.waitKey(10)
  #  print(op)
    
    #if cv2.waitKey(10) & 0xff==ord('q'):
     #             break
    if op==113:
        break
 cv2.destroyAllWindows()



hilo2 = threading.Thread(name='mostrar2', 
                         target=mostrar2,
                         args=('lost',))
hilo2.setDaemon(True)

def convertir():
      global n,mensaje,nido,img,captura
      ref,imagen=captura.read()
      gry=  cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
      img = cv2.resize(gry, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
      n=[0,0,0];mensaje=[''];nido=''      
      #print ('inicia conversion')
      for den in range(1,len(img[0])):
               for den1 in range(1,len(img)):
                       nido=nido+chr(img[den1][den])
               mensaje.append(nido)
               nido=''
      n=[0,0,0]
      return  
def conv(nomb):
        global img,li
        while fin==0:
                convertir()
                li=img
        print('saliendo conversion')

        
hilo1 = threading.Thread(name='conv', 
                         target=conv,
                         args=('lost',))
hilo1.setDaemon(True)
