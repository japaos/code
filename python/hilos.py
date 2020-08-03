import threading
import time
from Tkinter import Tk, Label, Button
import serial

arduino = serial.Serial("COM3", 9600)
msg='000'
fin=0;
window = Tk()
window.title("Variables")
lbl=Label(window,text='Variables detectadas del vivero',bg="Green",font=16);lbl.pack()
lbl1=Label(window,text=msg);lbl1.pack()
lbl2=Label(window,text=msg);lbl2.pack()
lbl3=Label(window,text=msg);lbl3.pack()
def servicio():
    global msg
    global fin
    global window
    print threading.currentThread().getName(), 'Lanzado\n'
    #window = Tk()
    #window.title("Welcome to LikeGeeks app")    
    window.mainloop()
    print threading.currentThread().getName(), 'Deteniendo\n'
    fin=1

def seria():
    global msg
    global fin
    global lbl
    global window
    while fin==0:        
        msg=arduino.readline()
        var=msg.split(',')
        if fin==0:
            lbl1['text']='Humedad= '+var[0]+" % "
            lbl2['text']='Temperatura= '+var[1]+"°C"
            lbl3['text']='Luminicencia= '+var[2]+"Lumens"
    print('\n cerrando seria')
    arduino.close()
t = threading.Thread(target=servicio, name='servicio\n')
w = threading.Thread(target=seria, name='seria\n')
w.start()
t.start()
