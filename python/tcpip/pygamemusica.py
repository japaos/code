'''
import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()
pygame.mixer.music.load('Arduino/itsfear.mp3')
pygame.mixer.music.play()


####'''
import serial
import pygame
from pygame.locals import *
from datetime import datetime, timedelta
import serial, time
##----------------------
import cv2
import numpy as np
##----------------------
captura = cv2.VideoCapture(0)
palabra=0
arduino = serial.Serial("COM48", 9600)
time.sleep(2)

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('itsfear.mp3')
def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image
def hablando(cancion):
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load(cancion)
                        pygame.mixer.music.play(1)
                        time.sleep(0.5)
                        arduino.write('h')
                        palabra=0
                        return

pantalla = pygame.display.set_mode((600,600))
pygame.display.set_caption("Prueba")
background_image = load_image('cara.jpg')
arduino.write('abriendo')
reloj = pygame.time.Clock()
pygame.mixer.music.play(1)
nio=datetime.now()
n=True
b=0;
t=0
contado=0
a=0
bi=0
limite=4
ubicacion=0;iz=0;de=0;

while n:    
    _, imagen = captura.read()
    #raws=arduino.readline()
    #raws=arduino.read()
    aux=datetime.now()
    if (not(aux.second==nio.second)) :
        nio=datetime.now()
        if(contado>limite):
                contado=0
                bi=0 
        contado=contado+1
        print (aux.second," segundos\n")          
           
        hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
     
        #Establecemos el rango de colores que vamos a detectar
        #En este caso de verde oscuro a verde-azulado claro
        verde_bajos = np.array([49,50,50], dtype=np.uint8)
        verde_altos = np.array([80, 255, 255], dtype=np.uint8)
     
        #Crear una mascara con solo los pixeles dentro del rango de verdes
        mask = cv2.inRange(hsv, verde_bajos, verde_altos)
     
        #Encontrar el area de los objetos que detecta la camara
        moments = cv2.moments(mask)
        area = moments['m00']
     
        #Descomentar para ver el area por pantalla
        #print area
        print (area)
        if(area > 2000000):
             
            #Buscamos el centro x, y del objeto
            x = int(moments['m10']/moments['m00'])
            y = int(moments['m01']/moments['m00'])
             
            #Mostramos sus coordenadas por pantalla
            print "x = ", x
            print "y = ", y
     
            #Dibujamos una marca en el centro del objeto
            cv2.rectangle(imagen, (x, y), (x+2, y+2),(0,0,255), 2)
            if x<200 :
                print ("izquierda")
                arduino.write('izquierda')
                de=0;ubicacion=0;                
                iz=iz+1
                if (iz==3):
                        hablando('iz.mp3')
                        palabra=0
                        bi=1;contado=0;limite=2;
            if x>400:
                de=de+1    
                print ("derecha")
                arduino.write('derecha')
                iz=0;ubicacion=0;
                if (de==3):
                        hablando('de.mp3')
                        bi=1;contado=0;limite=2;
            if 200<x<400:
                print ("centro")
                arduino.write('centro')
                ubicacion=ubicacion+1
                if (ubicacion==5):
                        hablando('Hola.mp3')
                        bi=1;contado=0;limite=2;    
                if (ubicacion==8):
                        hablando('Que.mp3')
                        bi=1;contado=0;limite=2;    
                if (ubicacion==11):
                        hablando('risa.mp3')
                        bi=1;contado=0;limite=2; 
        #Mostramos la imagen original con la marca del centro y
        #la mascara
        cv2.imshow('mask', mask)
        cv2.imshow('Camara', imagen)            
    ##raws=arduino.read()
      ##print (raws)
            
           
           
    if t==0:
        a=arduino.read()        
        print (a)
        t=1
    if a=='X' and bi==0:
            hablando('adios.mp3')
            bi=1;contado=0;limite=2;    
    elif a=='G' and bi==0:
            hablando('risa.mp3')
            bi=1;contado=0;limite=2;            
    elif a=='W' and bi==0:
            hablando('frente.mp3')
            bi=1;contado=0;limite=2;             
    elif a=='J' and bi==0:
            hablando('Hola.mp3')
            bi=1;contado=0;limite=2;                
    elif a=='L' and bi==0:
            hablando('itsfear.mp3')
            bi=1;contado=0;limite=2;    
    elif a=='B' and bi==0:
            hablando('BOOM.mp3')
            bi=1;contado=0;limite=2;
    elif a=='O' and bi==0:
            hablando('iz.mp3')
            bi=1;contado=0;limite=2;         
    elif a=='P' and bi==0:
            hablando('de.mp3')
            bi=1;contado=0;limite=2;
    elif a=='R' and bi==0:
            hablando('Que.mp3')
            bi=1;contado=0;limite=2;         
    elif a=='S' and bi==0:
            pygame.mixer.music.play(1)
            bi=1;contado=0;limite=2;    
    for event in pygame.event.get():
        
        if event.type == MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            if(100<x_mouse<190)and (252<y_mouse<287):
                   
                   ubicacion=ubicacion+1
                   if (ubicacion==5):
                        hablando('Hola.mp3')
                        arduino.write('hablar')
                        bi=1;contado=0;limite=2;    
                   if (ubicacion==8):
                        hablando('Que.mp3')
                        arduino.write('hablar')
                        bi=1;contado=0;limite=2;    
                   if (ubicacion==11):
                        hablando('risa.mp3')
                        arduino.write('hablar')
                        bi=1;contado=0;limite=2;
            if(20<x_mouse<124)and (128<y_mouse<179):
                   arduino.write('iz')    
            print (x_mouse, y_mouse)
            if(176<x_mouse<228)and (128<y_mouse<179):
                   arduino.write('de')    
            print (x_mouse, y_mouse)
            if(128<x_mouse<164)and (210<y_mouse<236):
                   arduino.write('ce')    
            print (x_mouse, y_mouse)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("lee tecla baja\n")
                raws=arduino.read()
                bi=0
                if raws=='a' and b==0:
                    pygame.mixer.music.pause()
                    nio=datetime.now()
                    b=1
                if raws=='D' and b==1:
                    pygame.mixer.music.play(1)
                    b=0
                    
                    
                print(raws)
            if event.key == pygame.K_DOWN:
                pygame.mixer.music.stop()
                pygame.mixer.music.load("adios.mp3")
                arduino.write('hablar')
                arduino.write('abajo')
                pygame.mixer.music.play(1)    
                print("Salir")
                n=False
    
    reloj.tick(60)
    t=0
    pantalla.blit(background_image, (0, 0))   
    pygame.display.update()

pygame.mixer.music.stop()    
pygame.quit()
arduino.write('cerrando\n')
captura.release()
arduino.close()
cv2.destroyAllWindows()

##
##
##import pygame
##
##BLANCO = (255,255,255)
##NEGRO = (0, 0, 0)
##MAGENTA = (255,0,255)
##FPS = 60
##
##class Cuadrado:
##    def __init__(self, x, y, lado, color, fondo):
##        self.x = x
##        self.y = y
##        self.color = color
##        self.fondo = fondo
##        self.lado = lado
##        self.rect = pygame.Rect(self.x,
##                                self.y,
##                                self.lado,
##                                self.lado)
##
##    def __pinta(self, pantalla, color):
##        'Realiza el dibujo efectivo'
##        pygame.draw.rect(pantalla, color, self.rect, 0)
##        
##    def pinta(self, pantalla):
##        'Pinta el cuadrado con el color propio'
##        self.__pinta(pantalla, self.color)
##
##    def borra(self, pantalla):
##        'Borra el cuadrado'
##        # Realmente lo pinta con el color de fondo
##        self.__pinta(pantalla, self.fondo)
##
##    def colisiona_con(self, cuadrado2):
##        'Comprueba la colisión con otro cuadrado'
##        return self.rect.colliderect(cuadrado2.rect)
##
##    def mover(self, avance_x, avance_y):
##        'avance del cuadrado en un cuadro (frame)'
##        self.rect.move_ip(avance_x, avance_y)
##
##    def mover_p(self, pantalla, avance_x, avance_y):
##        'avance del cuadrado en un cuadro, con refresco de pantalla'
##        cuadrado.borra(pantalla)
##        rect_inicial = cuadrado.rect.copy()
##        cuadrado.mover(avance_x, avance_y)
##        rect_final = cuadrado.rect.copy()
##        cuadrado.pinta(pantalla)
##        pygame.display.update(rect_final.union(rect_inicial))
##
##
### inicializamos pygame
##pygame.init()
##
### definición de la pantalla
##pantalla = pygame.display.set_mode((640,480))
##pantalla.fill(NEGRO)
##
##cuadrado = Cuadrado(50,50, 35, BLANCO, NEGRO)
##cuadrado2 = Cuadrado(540,50,35, MAGENTA, NEGRO)
##cuadrado.pinta(pantalla)
##cuadrado2.pinta(pantalla)
##pygame.display.update()
##
### reloj de control de refresco
##clock = pygame.time.Clock()
##pygame.key.set_repeat(True)
##pygame.mixer.init()
##pygame.mixer.music.load('itsfear.mp3')
##pygame.mixer.music.play()
##
##while not cuadrado.colisiona_con(cuadrado2):
##    # pausa hasta el siguiente "tick" de reloj
##    clock.tick(FPS)
##
##    # detección de evento QUIT (aspa)
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            pygame.quit()
##    
##        # Movimiento
##        if event.type == pygame.KEYDOWN:
##            if event.key == pygame.K_LEFT:
##                cuadrado.mover_p(pantalla, -2, 0)
##                print("funciona")    
##            if event.key == pygame.K_RIGHT:
##                cuadrado.mover_p(pantalla, 2, 0)
##
##pygame.mixer.music.stop()    
##print("Hay solape")
##    
##pygame.time.delay(3000)
##pygame.quit()
##



