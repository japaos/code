import socket
import cv2
img = cv2.imread('C:\Chrysanthemum.jpg', cv2.IMREAD_GRAYSCALE)
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr

img = cv2.imread('C:\Desert.jpg', cv2.IMREAD_GRAYSCALE)

while 1:
   data = conn.recv(BUFFER_SIZE)
   img=data
   if not data: break
   print "received data:", data
   conn.send(data)  # echo
   
print data
