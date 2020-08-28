#interfaz grafica de prueba

# decodigo.com

from tkinter import *
import turtle
import time

s=turtle.Screen()
t=turtle.Turtle()

pasos=["adelante","atras","derecha","izquierda"];
class VentanaEjemplo:
    def __init__(self, master):
        self.master = master
        master.title("Una simple interfaz gráfica")

        self.etiqueta = Label(master, text="Esta es la primera ventana!")
        self.etiqueta.pack()

        self.botonR = Button(master, text="Mover Rapido", command=self.saludar)
        self.botonR.pack()

        self.botonD = Button(master, text="Mover Despacio", command=self.saltar)
        self.botonD.pack()

        self.botonStar = Button(master, text="Estrella", command=self.estrella)
        self.botonStar.pack()

        self.botonCerrar = Button(master, text="Cerrar", command=master.quit)
        self.botonCerrar.pack()

        self.lista=Listbox(master,selectmode="SINGLE")
        for i in range(len(pasos)):            
            self.lista.insert(i,pasos[i]);
        self.lista.pack()
        silp=0
        self.menub=Menubutton(master,text="opciones")
        self.menub.menu=Menu(self.menub)
        self.menub["menu"]=self.menub.menu
        self.menub.menu.add_checkbutton(label = "Courses", variable = 0)
        self.menub.menu.add_checkbutton(label = "Student", variable = 1)
        self.menub.menu.add_checkbutton(label = "Masters", variable = 2)
        self.menub.pack()
    def saludar(self):
        t.color('black', 'black')
        t.home()
        t.clear()
        t.speed(15)
 #       t=turtle.Turtle()
        for n in range(4):            
            t.forward(50)
            t.right(90)
    def saltar(self):
        t.color('black', 'black')
        t.home()
        t.clear()
        t.speed()
#        t=turtle.Turtle()
        for n in range(4):
            time.sleep(0.5)
            t.forward(50)
            time.sleep(0.5)
            t.right(90)
    def estrella(self):
        t.color('red', 'yellow')
        t.begin_fill()
        while True:
            t.forward(200)
            t.left(170)
            if abs(t.pos()) < 1:
                break
        t.end_fill()
        
            


root = Tk()
miVentana = VentanaEjemplo(root)
root.mainloop()



