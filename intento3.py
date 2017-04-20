# -*- coding: cp1252 -*-
import sys, pygame
from pygame.locals import *
 
 

WIDTH = 1000
HEIGHT = 500
#sposx= S del nombre del wn y posx= 100 es donde empezara en X
SposX=100
SposY=299
##momentaneamente sin funcion
cont = 6
direc = True #este si funciona, ayuda a intercalar la imagen de izq a der
i=0
xixf={}#matriz de movimiento de imagen x inicial x final
Rxixf={}
#===========================================================
#=================IMAGEN====================================
 
def imagen(filename, transparent=False):
        try: image = pygame.image.load(filename)#
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()#formato interno de python para trabajar mejor
        
  # este codigo es para quitarle  ese cuadrado blanco)transparencia que el personaje       
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image
#======================TECLADO==========================================


def teclado():

    #con esto obtien la info del teclado y get.presset devuelve las teclas precionadas            
    teclado=pygame.key.get_pressed()

    global SposX, SposY
    global cont, direc
    
    if teclado [K_RIGHT]:
        SposX+=2
        cont+=1
        direc= True
    elif teclado[K_LEFT]:
        SposX-=2
        cont+=1
        direc= False
    elif teclado [K_UP]:
        SposY -=5

    SposY = min (299, SposY+2)#al momento de usar el UP esto lo hace bajar
        
       

    return
    

#===========================================================
#=================SPRITE====================================
def sprite(): #momentaneamente fuera de servicio
              #esto lo que hace es ver los sprites de la imagen y hacer que cambien
    global cont
    
    xixf[0]=(12,12,35,55)
    xixf[1]=(53,10,34,45)
    xixf[2]=(97,10,32,50)
    xixf[3]=(146,5,28,45)
    xixf[4]=(178,8,25,45)
    xixf[5]=(208,8,28,49)
    xixf[6]=(240,9,37,49)
    xixf[7]=(281,9,32,48)
    xixf[8]=(322,10,25,45)
    xixf[9]=(354,9,24,48)
    xixf[10]=(384,10,31,49)
        
    Rxixf[0]=(386,9,27,47)
    Rxixf[1]=(325,8,43,49)
    Rxixf[2]=(290,7,34,46)
    Rxixf[3]=(252,6,24,46)
    Rxixf[4]=(218,7,25,48)
    Rxixf[5]=(184,8,29,49)
    Rxixf[6]=(144,8,37,49)
    Rxixf[7]=(109,9,32,48)
    Rxixf[8]=(74,11,25,46)
    Rxixf[9]=(44,9,24,48)
    Rxixf[10]=(7,11,32,49)
    
    p=6

    global i

    if cont == p:
        i=0
    if cont == p*2:
        i=1
    if cont == p*3:
        i=2
    if cont == p*4:
        i=3
    if cont == p*5:
        i=4
    if cont == p*6:
        i=5
    if cont == p*7:
        i=6
    if cont == p*8:
        i=7
    if cont == p*9:
        i=8
    if cont == p*10:
        i=9
        cont=0
    return

#================================================================
 
def main():
    pygame.init()    
    pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
    #nombre de la pantalla
    pygame.display.set_caption("juegazo")
 
   
    #fondo = imagen("C:\Users\Gustavo\Desktop\proyecto/fondo.png")      
    #descarga = imagen("C:\Users\Gustavo\Desktop\proyecto/prota0.png",True)
    fondo = imagen("C:\Users\Gabriel\Documents\Universidad\Proyecto 2\proyecto/fondo.png")      
    descarga = imagen("C:\Users\Gabriel\Documents\Universidad\Proyecto 2\proyecto/sprite2.png",True)
    descargainv = pygame.transform.flip(descarga,True,False); # da vuelta el Sprite
    pygame.mixer.music.load("C:\Users\Gabriel\Documents\Universidad\Proyecto 2/musica.mp3")
    #con el true estamos diciendo que si hay transpariencia, osea se la quitamos

    clock=pygame.time.Clock()

    pygame.mixer.music.play(-1, 0.0)
 
    # el bucle principal del juego
    while True:
        time=clock.tick(60)
        sprite()
        #llamar a la funcion teclado con
        teclado()
        #cambiarle el tamaño de la imagen    
        fondo = pygame.transform.scale(fondo, (1000, 400))
        #descarga = pygame.transform.scale(descarga,(100,100))
        
        # es para que empiece a dibujar de la posicion 0,0   
        pantalla.blit(fondo, (0, 0))
        #partira en la posicion sposX,283
        #empieza a dibujar la imagen con condiciones, que ayuda a indicar
        #inquierza y derecha 
        if direc==False :
            pantalla.blit(descarga,  (SposX, SposY), (xixf[i]))

        if direc == True:
            pantalla.blit(descargainv,  (SposX, SposY), (Rxixf[i]))

        pygame.display.flip()
        
        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
   
    return 0
 
if __name__ == '__main__':
    main()
    
    

