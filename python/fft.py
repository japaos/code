from numpy import *
import matplotlib.pyplot as plt
from numpy.fft import fft,fftfreq
import socket
import serial
from threading import *
import sys
x=linspace(0,0.001,500)
factor=2.0*pi/0.001
y=sin(2*x*factor)
frecuencias=fftfreq(500)

datx=open('datos_20Hz.txt','r').read()

ydatx=datx.split('\n')
for i in range(len(ydatx)):
	ydatx[i]=int(ydatx[i])
	
def f():
    global x,ydatx;
    x=linspace(-1,1,100)
    plt.plot(real(fft(ydatx)))
    plt.show()
    print "sale de plot"



