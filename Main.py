import pygame,	sys,	glob
from Clases import*
from pygame import*	

h=400	
w=800


screen=pygame.display.set_mode((w,h))
clock=pygame.time.Clock()

player1 = player()
position = 0

while 1:	    
    screen.fill((0,0,0))	
    clock.tick(60)	
    for event in pygame.event.get():	
        if event.type	==	pygame.QUIT:	
            sys.exit()
        elif event.type == KEYDOWN and ( event.key == K_RIGHT):
            position = 1
        elif event.type == KEYDOWN and (event.key == K_LEFT):
            position = -1
        elif event.type == KEYUP and (event.key == K_RIGHT):
            position = 2
        elif event.type == KEYUP and (event.key == K_LEFT):
            position = -2
    player1.update(position)
    pygame.display.flip()
 
if __name__ == '__main__':
    main()
