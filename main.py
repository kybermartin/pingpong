from pygame import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.set_caption("Ping Pong")

clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, x, y, speed, wight, height, color):
        self.speed = speed
        self.color = color
        self.rect = Rect(x, y, wight, height)
    
    def draw(self):
        draw.rect(screen, self.color, self.rect)

class Player(GameSprite):

    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < SCREEN_HEIGHT - self.rect.height:
            self.rect.y += self.speed

    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < SCREEN_HEIGHT - self.rect.height:
            self.rect.y += self.speed

class Ball(GameSprite):

    def __init__(self, x, y, speed, radius, color):
        super().__init__(x, y, speed, radius * 2, radius * 2, color)
        self.radius = radius
        self.speed_x = speed
        self.speed_y = speed

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.y < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.speed_y *= -1  

    def draw(self):
        draw.circle(screen, self.color, self.rect.center, self.radius)
        draw.rect(screen, "white", self.rect, width=1)

player1 = Player(10, 200, 10, 30, 150, "red")
player2 = Player(760, 200, 10, 30, 150, "blue")
ball = Ball(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 5, 10, "green")

font.init()
font_game = font.Font(None, 75)
player1_lose = font_game.render("Player 1 lose!", True, "yellow")
player2_lose = font_game.render("Player 2 lose!", True, "yellow")
center_text_pos_player1 =  player1_lose.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
center_text_pos_player2 =  player2_lose.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

finish = False
runing = True
while runing:

    #events
    for ev in event.get():
        if ev.type == QUIT:
            runing = False

    if finish != True:
        #draw
        screen.fill("black")
        player1.draw()
        player2.draw()
        ball.draw()
        
        #update
        player1.update_left()
        player2.update_right()
        ball.update()
        
        #collides
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            ball.speed_x *= -1

        #vyhry prehry
        if ball.rect.right > SCREEN_WIDTH:
            screen.blit(player2_lose, center_text_pos_player1)
            finish = True

        if ball.rect.x < 0:
            screen.blit(player1_lose, center_text_pos_player2)
            finish = True


    display.update()
    
    clock.tick(FPS)
        
quit()
