#from scipy import signal
import threading as tr
import numpy as np
import serial,random,sys
#import matplotlib.animation as animation
#import matplotlib.pyplot as plt
import socket
'''s1=signal.lti([1],[1, 1])
w,mag,fase=signal.bode(s1)

plt.figure();plt.semilogx(w,mag);plt.figure();plt.semilogx(w,fase);

plt.show();
while(n==0):
	msg=arduino.readline()
	n=input('salir')
'''
arduino = serial.Serial("COM4", 115200)
cls=0
b=''
bt=[]
#fig=plt.figure()
#ax1=fig.add_subplot(1,1,1)

x=np.arange(0,1000,(1000/20))
y=np.arange(0,1000,(1000/20))
xv=np.zeros(21)

name=socket.gethostname()
ip=socket.gethostbyname(name)
cliente=socket.socket()
lector=0
todo=0
def mostrador():
     global cls,b,x,xv,y,cliente,bt
     #cliente.connect(('192.168.0.11',5011))
     print('inicia comunicaciones')
     while(True):
        xv[1:21]=y
        b=arduino.readline()
        #bt=int(b[b.find('b')+1:b.find('\r')])
        xv[0]=random.randint(1,100)
        y=xv[0:20]
        datx=open('x.txt','w')
        datx.write(str(y).replace(' ','\n'))
        datx.close()
        #cliente.send('mensaje')
        msg=str(y).replace(' ','b');msg=msg.replace('\n','');
        #cliente.send(msg)                  
        if(cls==3):
             if (b.find('r')>0):
                  bt.append(b[b.find('b')+1:b.find('r')])
        if(cls==1):
             print('cerrando')
             break
         #       cliente.send('finaliza')
         #       cliente.close()                  
     arduino.close()
        
##def carga(i):
##     global x,y,ax1
##     ax1.clear()
##     ax1.plot(x,y)
   
def servicio():
     #global fig
     print(' iniciando servicio')
     print(' pasa show y cerrando servicio')

mostrar = tr.Thread(target=mostrador, name='mostrador\n')
mostrar.start()
s = tr.Thread(target=servicio, name='servicio\n')
s.start()
#mostrar = tr.Thread(target=lector, name='lector\n')
#mostrar.start()

