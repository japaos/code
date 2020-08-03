import socket
name=socket.gethostname()
ip=socket.gethostbyname(name)
cliente=socket.socket()
cliente.connect(('192.168.0.16',5025))
