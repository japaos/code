import socket
import cv2
import numpy
import threading
captura = cv2.VideoCapture(0)


TCP_IP = '127.0.0.1'
TCP_PORT = 6015
BUFFER_SIZE = 767
img = cv2.imread('C:\Desert.jpg', cv2.IMREAD_GRAYSCALE)
#MESSAGE = "Hello, World!"+TCP_IP+" "+str(img[0][0])
img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
li=img
n=[0,0,0]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

nido=''
mensaje=['']
fin=0

def chequear(nombre):
       global fin,img,captura
       global n,mensaje,nido,img,li
       while fin==0:
          ref,imagen=captura.read()
          gry=  cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
          img = cv2.resize(gry, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
          n=[0,0,0];mensaje=[''];nido=''
          for den in range(1,len(img[0])):
               for den1 in range(1,len(img)):
                       nido=nido+chr(img[den1][den])
               mensaje.append(nido)
               nido=''
      #print ('inicia conversion')
##          while True:
##            if n[2]==(numpy.shape(img)[1]-1):
##                break   
##            while True:
##               if n[1]==(numpy.shape(img)[0]-1):
##                  break
##               nido=nido+chr(img[n[1]][n[2]])
##               n[1]=n[1]+1
##            mensaje.append(nido)
##            nido='n'
##            n[1]=0
##            n[2]=n[2]+1
          n=[0,0,0];li=img
       captura.release()     
          



#cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
def convertir():
      global n,mensaje,nido,img
      n=[0,0,0];mensaje=[''];nido=''      
      #print ('inicia conversion')
      for den in range(1,len(img[0])):
               for den1 in range(1,len(img)):
                       nido=nido+chr(img[den1][den])
               mensaje.append(nido)
               nido=''
      n=[0,0,0]

def modBUFF():
      global mensaje
      global s
      s.send('BUFFER_SIZE')
      s.send(str(len(mensaje)))
      BUFFER_SIZE=len(mensaje)

    
###inicio deelhilo___________________________________
hilo1 = threading.Thread(name='chequear', 
                         target=chequear,
                         args=('lost',))
hilo1.setDaemon(True)
##hilo1.start()



def envio(ping):
      global mensaje
      global s
      s.send('l')
      while True:
            if n[0]==ping:
                break
            s.send(mensaje[n[0]])
            n[0]=n[0]+1
            #s.recv(BUFFER_SIZE)
      n[0]=0

def envioII():
      global mensaje
      global s
      s.send('l')
      for den in range(1,len(mensaje)):
             s.send(mensaje[den])
##      ping=len(mensaje)-1
##      while True:
##            if n[0]==(ping):
##                break
##            s.send(mensaje[n[0]])
##            n[0]=n[0]+1
##            #s.recv(BUFFER_SIZE)
      s.send('n')
      s.send('s')
      n[0]=0


##while True:
##      if n[0]==(numpy.shape(img)[0]-1):
##          break
##      MESSAGE=chr(img[100][n[0]])
##      s.send(MESSAGE)
##      n[0]=n[0]+1
##      s.recv(BUFFER_SIZE)



   
##    if n[0]==(numpy.shape(img)[0]):
##        if n[1]==(numpy.shape(img)[1]-1):
##            break
##        else:
##            n[0]=0
##            n[1]=n[1]+1
##        
##    MESSAGE=img[100][n]
##    s.send(MESSAGE)
##    n[0]=n[0]+1
##    s.recv(BUFFER_SIZE)
    
print('fin')
s.send('n')
#

#s.close()

def mostrar2(nombre):
 global img,li
 while True:
    if nido=='n':
       li=img    
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


##
##def chequear(nombre):
##    '''Chequea tamaño de archivo'''
##    global n
##    global captura
##    global ref,imagen,mask,regist,font,bottomLeftCornerOfText,fontScale,fontColor,lineType
##
##    tam = 0
##    
##    while n==0:
##        ref,imagen=captura.read()
##        
###________
##        hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
##     
##        #Establecemos el rango de colores que vamos a detectar
##        #En este caso de verde oscuro a verde-azulado claro
##        verde_bajos = np.array([49,50,50], dtype=np.uint8)
##        verde_altos = np.array([80, 255, 255], dtype=np.uint8)
##     
##        #Crear una mascara con solo los pixeles dentro del rango de verdes
##        mask = cv2.inRange(hsv, verde_bajos, verde_altos)
##     
##        #Encontrar el area dqe los objetos que detecta la camara
##        moments = cv2.moments(mask)
##        area = moments['m00']
##        
##        cv2.putText(mask,regist, 
##            bottomLeftCornerOfText, 
##            font, 
##            fontScale,
##            fontColor,
##            lineType)
##        
##        if(area>400000):
##            x = int(moments['m10']/moments['m00'])
##            y = int(moments['m01']/moments['m00'])
##            cv2.rectangle(mask, (x, y), (x+30, y+30),(100,0,255), 2)
##            cv2.putText(mask,'Digite texto:', 
##            (x,y), 
##            cv2.FONT_HERSHEY_PLAIN, 
##            1,
##            fontColor,
##            1)
##    #        print "x = ", x
##    #        print "y = ", y
##           # print(area)
##      
###________        
##        time.sleep(0.01)
##        tam=tam+1
##        if(tam>30000):
##            tam=0            
##    print('maxima cuenta',tam)
##

