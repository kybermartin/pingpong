from pygame import *
from pygame.locals import *

WIN_WIDTH = 500
WIN_HEIGHT = 400
FPS = 60

window = display.set_mode((WIN_WIDTH, WIN_HEIGHT))
display.set_caption("Ping Pong")
clock = time.Clock()

run = True
while run:

    for ev in event.get():
        if ev.type == QUIT:
            run = False

    display.update()
    clock.tick(FPS)
    
quit()