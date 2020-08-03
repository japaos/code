import socket
import cv2
import numpy

img = cv2.imread('C:\Desert.jpg', cv2.IMREAD_GRAYSCALE)

n=[0,0,0]
nido=''
mensaje=['']
while True:
      if n[2]==(numpy.shape(img)[1]-1):
          break   
      while True:
         if n[1]==(numpy.shape(img)[0]-1):
            break
         nido=nido+chr(img[n[1]][n[2]])
         n[1]=n[1]+1
      mensaje.append(nido)
      nido=''
      n[1]=0
      n[2]=n[2]+1
