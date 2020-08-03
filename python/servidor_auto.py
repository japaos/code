import socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=socket.gethostbyname(socket.gethostname())
print('ip de conexion :',ip)
port=5025
address=(ip,port)
server.bind(address)
server.listen(1)
print("[]escuchando en",ip,"#:#",port)
client,addr=server.accept()
print("[]conexion obtenida de ",addr[0],":",addr[1])
while True:
    data=client.recv(1024)
    print ("[]recibido",data," del cliente ")
    print ("pensando")
    if (data=="hola servidor"):
        client.send("hola cliente")
    elif(data=="desconecta"):
        client.send('desconectando')
        client.close()
        break
    else:
        client.send('comando no reconocido\n pensando')
  
