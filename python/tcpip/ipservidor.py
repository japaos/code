import socket
import cv2
import numpy



TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
img = cv2.imread('C:\Desert.jpg', cv2.IMREAD_GRAYSCALE)
#MESSAGE = "Hello, World!"+TCP_IP+" "+str(img[0][0])
MESSAGE = img[0][0]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print "received data:", data

