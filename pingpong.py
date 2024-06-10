
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
    
    def move_up(self):
        self.y -= 10

    def move_down(self):
        self.y += 10

    def update(self):
        if self.y < 0:
            self.y = 0
        if self.y > WIN_HEIGHT - 100:
            self.y = WIN_HEIGHT - 100

    def draw(self):
        draw.rect(window, BLACK, (self.x, self.y, 20, 100), width=0)

class Lopta(sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.x_direction = 1
        self.y_direction = 1

    def update(self):
        if self.x > WIN_WIDTH - 5:
            self.x_direction = -1
        if self.x < 5:
            self.x_direction = 1

        if self.y > WIN_HEIGHT - 5:
            self.y_direction = -1
        if self.y < 5:
            self.y_direction = 1

        self.x += self.x_direction * 5
        self.y += self.y_direction * 5

    def draw(self):
        draw.circle(window, WHITE, (self.x, self.y), 10)




window = display.set_mode((WIN_WIDTH, WIN_HEIGHT))
display.set_caption("Ping Pong")
clock = time.Clock()


palkaA = Palka(10,10)
palkaB = Palka(WIN_WIDTH - 30, 10)
lopta = Lopta(100,100)

run = True
while run:

    for ev in event.get():
        if ev.type == QUIT:
            run = False
    pressed = key.get_pressed()
    if pressed[K_q]:
        palkaA.move_up()  
    if pressed[K_a]:
        palkaA.move_down()       

    if pressed[K_p]:
        palkaB.move_up()
    if pressed[K_l]:
        palkaB.move_down()       


    palkaA.update()
    palkaB.update()
    lopta.update()

    window.fill(RED)    
    palkaA.draw()
    palkaB.draw()
    lopta.draw()

    display.update()
    clock.tick(FPS)

quit()