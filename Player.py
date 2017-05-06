import pygame,	sys,	glob
from pygame import*
from Variables import*

h=400	
w=800

screen=pygame.display.set_mode((w,h))

class player:
    def __init__(self):
        self.screen=pygame.display.set_mode((w,h))
        self.x = 200
        self.y = 300
        self.initialAnimSpeed = 7
        self.currentAnimSpeed = self.initialAnimSpeed
        
        self.anim = glob.glob('Personaje\sprite*.png')
        self.anim.sort()
        self.animPosition=0
        self.aniMax = len(self.anim) -1
        
                    
        self.image = pygame.image.load(self.anim[0])

        
        self.update(0)

    def update (self, pos):
        if pos !=0:

            if pos==2:
                self.image2 = pygame.image.load(self.anim[0])
                self.image = pygame.transform.flip(self.image2,True,False)
                
            if pos==-2:
                self.image = pygame.image.load(self.anim[0])

            
                
            if pos==1:#DER
                self.currentAnimSpeed -=1
                self.x += 1

                if self.currentAnimSpeed ==0:
                    self.image2 = pygame.image.load(self.anim[self.animPosition])
                    self.image = pygame.transform.flip(self.image2, True, False)
                    
                    self.currentAnimSpeed = self.initialAnimSpeed
                    if self.animPosition == self.aniMax:
                        self.animPosition = 1
                    else:
                        self.animPosition +=1
                    
            if pos==-1:#IZQ
                self.currentAnimSpeed -=1
                self.x -= 1

                if self.currentAnimSpeed ==0:
                    self.image = pygame.image.load(self.anim[self.animPosition])
                    self.currentAnimSpeed = self.initialAnimSpeed
                    if self.animPosition == self.aniMax:
                        self.animPosition = 1
                    else:
                        self.animPosition +=1
            
            
                               
        screen.blit(self.image,(self.x, self.y))
                
        
