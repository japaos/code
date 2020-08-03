import matplotlib.animation as animation
import matplotlib.pyplot as plt
import threading as tr
import socket
import serial,random,sys
import numpy as np
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=socket.gethostbyname(socket.gethostname())
print('ip de conexion :',ip)
port=5011
address=(ip,port)

'''
datx=open('x.txt','w')
datx.write('[20,20,50,50,60,60,'+str(11)+']')
datx.close()
'''
##datx=open('x.txt','r').read()
##x=datx.replace('[','')
##x=x.replace(']','')
##x=x.split(' ')
##y=range(len(x))

tam=100
y=[]

##x=np.arange(0,1000,(1000/tam))
##y=np.arange(0,1000,(1000/tam))
##xv=np.zeros(tam+1)

fig=plt.figure()
ax1=fig.add_subplot(1,1,1)

cls=0
##def lector():
##     global cls,b,x,y
##     print('inicia comunicaciones')
##     while(True):
##        datx=open('x.txt','r').read()
##        x=datx.replace('[','')
##        x=x.replace(']','')
##        x=x.split('\n')
##        y=range(len(x))
##        if(cls>0):
##                print('cerrando')  
##                break;
##
dat=''


def servidor():
     global address,server,ip,port,y,data
     server.bind(address)
     server.listen(1)
     print("[]escuchando en",ip,"#:#",port)
     client,addr=server.accept()
     print("[]conexion obtenida de ",addr[0],":",addr[1])
     while True:
         data=client.recv(1024)
         if (data=="finaliza"):
             client.close()
             print('cierra conexion servidor')
             break               
         elif (len(data)>5):
            if(data=='mensaje'):
                   data=client.recv(1024)   
                   y1=data.replace('[','')
                   y1=y1.replace(']','')
                   y=y1.split('b')
                   dat=data 



     
def carga(i):
     global y,ax1,cls,tam
     y23=y
     cont=[]     
##     datx=open('x.txt','r').read()
##     y=datx.replace('[','')
##     y=y.replace(']','')
##     y=y.split('\n')
##     for i in range(y.count('')):
##          y.remove('')
##		
##     x=range(len(y))
     y22=[]
     x23=[]
     for i in range(len(y23)):
        if(y23[i]==''):
             cont=0
        else:
             y22.append(float(y23[i]))
             x23.append(i)

     #x=np.arange(0,1000,(1000/tam))
     if(len(y22)>10):
          ax1.clear()
          ax1.plot(x23,y22)     

b=''
'''
def servidor():
     global cls,b,x,xv,address,server,ip,port,y,data,tam
     server.bind(address)
     server.listen(1)
     print("[]escuchando en",ip,"#:#",port)
     client,addr=server.accept()
     print("[]conexion obtenida de ",addr[0],":",addr[1])
     while(True):
        xv[1:(tam+1)]=y
        #b=arduino.readline()
        xv[0]=random.randint(1,100)
        y=xv[0:tam]
        data=client.recv(1024)
        if (data=="finaliza"):
             client.close()
             print('cierra conexion servidor')
             break
        if(cls>0):
                print('cerrando')
                cliente.send('finaliza')
                cliente.close()
                break;

 
'''



serv = tr.Thread(target=servidor, name='server\n')
serv.start()


ani=animation.FuncAnimation(fig,carga,interval=200)
print('pasa anima')
plt.show()
cls=1
