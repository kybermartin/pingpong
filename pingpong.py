
from pygame import *
from pygame.locals import *


WIN_WIDTH = 500
WIN_HEIGHT = 400
FPS = 60
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Palka(sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.x = x
        self.y = y

    def update(self, action):
        if action == 'down':
            self.y += 10
        elif action == 'up':
            self.y -= 10
        
            
    def draw(self):
        draw.rect(window, BLACK, (self.x, self.y, 20, 100), width=2)

window = display.set_mode((WIN_WIDTH, WIN_HEIGHT))
display.set_caption("Ping Pong")
clock = time.Clock()


palkaA = Palka(100,100)
action = "stop"

run = True
while run:

    for ev in event.get():
        if ev.type == QUIT:
            run = False
        if ev.type == KEYDOWN:
            if ev.key == K_q:
                action = "up"
            if ev.key == K_a:
                action = "down"
        if ev.type == KEYUP:
            action = "stop"

    palkaA.update(action)


    window.fill(RED)    
    palkaA.draw()

    display.update()
    clock.tick(FPS)

quit()