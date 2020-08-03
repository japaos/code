from socket import socket
f = open("Chrysanthemum.jpg", "rb")
s = socket()
def main():
    global f
    global s
    s.connect(("localhost", 6002))
    s.send('Start')
    while True:
        f = open("Chrysanthemum.jpg", "rb")
        content = f.read(1024)
        
        while content:
            # Enviar contenido.
            s.send(content)
            content = f.read(1024)
        
        break
    
    # Se utiliza el caracter de código 1 para indicar
    # al cliente que ya se ha enviado todo el contenido.
    try:
        print ('enviando orden de cerrado')
        s.send(chr(1))
    except TypeError:
        # Compatibilidad con Python 3.
        s.send(bytes(chr(1), "utf-8"))
    # Cerrar conexión y archivo.
##    while True:
##        data=s.recv(1024)
##        print ('recibi: ',data)
##        if data=='s':
##            break
       
    #s.close()
    #f.close()
    print("El archivo ha sido enviado correctamente.")
if __name__ == "__main__":
    main()
