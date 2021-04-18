from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, height_sprite, width_sprite):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (height_sprite, width_sprite))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 490:
            self.direction = "right"
        if self.rect.x >= win_width - 65:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Coach(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 180:
            self.direction = "right"
        if self.rect.x >= win_width - 400:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
            
class Star(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 360:
            self.direction = "right"
        if self.rect.x >= win_width - 240:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        #draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))5
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

mixer.init()
mixer.music.load('Maze2.mp3')
mixer.music.play()

player = Player('sprite2.png', 20, 350, 5, 100, 100)
villian = Enemy('sprite1.png', 480, 200, 1, 100, 150)
coach = Coach('sprite3.png', 200, 180, 1, 50, 100)
final = GameSprite('money.png', 580, 400, 0, 90, 90)
star = Star('ninjastar.png', 360, 180, 3, 40, 40)

w1 = Wall(99, 185, 85, 170, 150, 10, 420)
w2 = Wall(99, 185, 85, 350, 0, 10, 350)
w3 = Wall(99, 185, 85, 500, 150, 10, 420)

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

clock = time.Clock()
FPS = 60
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        player.update()
        villian.update()
        coach.update()
        star.update()

        player.reset()
        villian.reset()
        coach.reset()
        final.reset()
        star.reset()  

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()

        '''if sprite.collide_rect(player, villian) or sprite.collide_rect(player, coach) or sprite.collide_rect(player, star) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3):
            finish = True
            window.blit(lose, (200, 200))
            kick.play()'''
        
        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (200, 200))
            money.play()

    display.update()
    clock.tick(FPS)