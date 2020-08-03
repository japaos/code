import socket
import cv2
import numpy as np
import cv2
import threading
img = cv2.imread('C:\Chrysanthemum.jpg', cv2.IMREAD_GRAYSCALE)
TCP_IP = '127.0.0.1'
TCP_PORT = 6015
BUFFER_SIZE = 767  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

mensaje=['']
mik=mensaje
conn, addr = s.accept()
print 'Connection address:', addr

img = cv2.imread('C:\Desert.jpg', cv2.IMREAD_GRAYSCALE)
data=''
info=''
flg=1

def receptor(nombre):
   global data,info,flg,conn,addr,mensaje,BUFFER_SIZE
   while True:
      data = conn.recv(BUFFER_SIZE)
      if data=='n':
         flg=1
         print ('Imagen recibida')
      if flg==2:
         mensaje.append(data)
      if data=='l':
         mensaje=['k']
         flg=2
         info=info+data
      if flg==0:
         flg=1;BUFFER_SIZE=int(data);print (BUFFER_SIZE)
      if data=='BUFFER_SIZE':
         print('recibido buffer')
         flg=0
      #print "received data:", data
      if data=='s' : break   
      conn.send('')  # echo
   print('saliendo de recepcion')
hilo1 = threading.Thread(name='receptor', 
                         target=receptor,
                         args=('lost',))
hilo1.setDaemon(True)
hilo1.start()
      

if len(mensaje)>5 :
   if len(mensaje[1])>5 :   
     mik=np.zeros((len(mensaje),len(mensaje[1])),dtype='uint8')


def envio(ping):
      global mensaje
      n=0
      while True:
            if n==ping:
                break
            print('tamaño de mensaje',len(mensaje[n]))
            n=n+1
            #s.recv(BUFFER_SIZE)
      
def convertir():
      global mensaje
      global mik
      n=1;limite1=len(mensaje[1])-1;limite2=len(mensaje)-1
      if len(mensaje)>5 :
         if len(mensaje[1])>5 :   
           mik=np.zeros((len(mensaje),len(mensaje[1])),dtype='uint8')

           for den in range(1,len(mik)):
               for den1 in range(1,len(mik[0])):
                       try :
                          mik[den][den1]=ord(mensaje[den][den1])
                       except :
                          print(den,den1)
      
##      while True:
##            p=1
##            if n==(limite2):
##                break
##            while p<(limite1):
##               ordinal=ord(mensaje[p][n])
##               #print()
##               mik[n][p]=ordinal
##               p=p+1
##            n=n+1
            #s.recv(BUFFER_SIZE)
     # mik=np.delete(mensaje, 0, 0)

def mostrar():
 global mik
 mico=np.transpose(mik)
 while True:
    cv2.imshow('imagen',mico)
 #   time.sleep(0.1)
    op=cv2.waitKey(10)
  #  print(op)
    
    #if cv2.waitKey(10) & 0xff==ord('q'):
     #             break
    if op==113:
        break
 cv2.destroyAllWindows()

