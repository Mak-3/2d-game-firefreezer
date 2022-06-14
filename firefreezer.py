import pygame
import sys
import math
from pygame.locals import *
pygame.init()

#dimensions
WINDOW_WIDTH=1200
WINDOW_HEIGHT=600
FPS=20

#colors
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

ADD_NEW_BULLET_RATE = 25
fire_img = pygame.image.load('fire.png')
fire_img_rect = fire_img.get_rect()
fire_img_rect.left = 0
ice_img = pygame.image.load('ice.png')
ice_img_rect = ice_img.get_rect()
ice_img_rect.left = 0
CLOCK = pygame.time.Clock()
mainClock=pygame.time.Clock()
font = pygame.font.SysFont('forte', 20)
canvas = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('FIREFREEZER')

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False
 
def main_menu():
    while True:
        start_img = pygame.image.load('main_bg.png')
        start_img_rect = start_img.get_rect()
        canvas.blit(start_img, start_img_rect)
        
        draw_text('Main Menu', font, (0,0,0), canvas, 250, 100)
 
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(200, 100, 200, 50)
        button_2 = pygame.Rect(200, 180, 200, 50)
        button_3 = pygame.Rect(200, 260, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                start_game()
        if button_2.collidepoint((mx, my)):
            if click:
                about()
        if button_3.collidepoint((mx, my)):
            if click:
                exit()

        pygame.draw.rect(canvas, (255, 0, 0), button_1)
        pygame.draw.rect(canvas, (255, 0, 0), button_2)
        pygame.draw.rect(canvas, (255, 0, 0), button_3)
       
        draw_text('START GAME', font, (255,255,255), canvas, 270, 115)
        draw_text('     ABOUT', font, (255,255,255), canvas, 250, 195)
        draw_text('        EXIT', font, (255, 255, 255), canvas, 230, 275)


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)


class Topscore:
    def __init__(self):
        self.high_score = 0
    def top_score(self, score):
        if score > self.high_score:
            self.high_score = score
        return self.high_score
topscore = Topscore()

class Villain:
    villain_speed=10
    def __init__(self):
        self.villain_img=pygame.image.load('villain.png')
        self.villain_img_rect = self.villain_img.get_rect()
        self.villain_img_rect.width-= 10
        self.villain_img_rect.height-= 10
        self.villain_img_rect.top=WINDOW_HEIGHT/2
        self.villain_img_rect.right=WINDOW_WIDTH
        self.up=True
        self.down=False
        
    def update(self):
        canvas.blit(self.villain_img,self.villain_img_rect)
        if self.villain_img_rect.top <= fire_img_rect.bottom:
            self.up = False
            self.down=True
        elif self.villain_img_rect.bottom >= ice_img_rect.top:
            self.up=True
            self.down=False
        if self.up:
            self.villain_img_rect.top -= self.villain_speed
        elif self.down:
            self.villain_img_rect.top += self.villain_speed
        
class Bullet:
    bullet_speed=20
    
    def __init__(self):
        self.shooter=pygame.image.load('fireball.png')
        self.shooter_img=pygame.transform.scale(self.shooter, (20,20))
        self.shooter_img_rect=self.shooter_img.get_rect()
        self.shooter_img_rect.right=villain.villain_img_rect.left
        self.shooter_img_rect.top=villain.villain_img_rect.top+70

    def update(self):
        canvas.blit(self.shooter_img,self.shooter_img_rect)
        
        if self.shooter_img_rect.left>0:
            self.shooter_img_rect.left -= self.bullet_speed

class Snowman:
    speed=10
    
    def __init__(self):
        self.snowman_img=pygame.image.load('snowman.png')
        self.snowman_img_rect=self.snowman_img.get_rect()
        self.snowman_img_rect.left=20
        self.snowman_img_rect.top=(WINDOW_HEIGHT/2)-100
        self.down=True 
        self.up=False

    def update(self):
        canvas.blit(self.snowman_img, self.snowman_img_rect)
        if self.snowman_img_rect.top <= fire_img_rect.bottom:
            game_over()
            if SCORE > self.firefreezer_score:
                self.firefreezer_score = SCORE
        if self.snowman_img_rect.bottom >= ice_img_rect.top:
            game_over()
            if SCORE > self.firefreezer_score:
                self.firefreezer_score = SCORE
        if self.up:
            self.snowman_img_rect.top -= 10
        if self.down:
            self.snowman_img_rect.bottom += 10
            
def game_over():
   pygame.mixer.music.stop()
   music=pygame.mixer.Sound('game_over.wav')
   music.play()
   topscore.top_score(SCORE)
   game_over_img=pygame.image.load('game_over.png')
   game_over_img_rect=game_over_img.get_rect()
   game_over_img_rect.center=(WINDOW_WIDTH/2,WINDOW_HEIGHT/2)
   canvas.blit(game_over_img,game_over_img_rect)
   while True:
       for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
          if event.type == pygame.KEYDOWN:
              if event.type == pygame.K_ESCAPE:
                  pygame.quit()
                  sys.exit()
              music.stop()
              game_loop()
       pygame.display.update()
    
def start_game():
    start_img = pygame.image.load('main_bg.png')
    start_img_rect = start_img.get_rect()
    canvas.blit(start_img, start_img_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                game_loop()
        pygame.display.update()

def check_level(SCORE):
    global LEVEL
    if SCORE in range(0, 10):
        fire_img_rect.bottom = 50
        ice_img_rect.top = WINDOW_HEIGHT - 50
        LEVEL = 1
    elif SCORE in range(10, 20):
        fire_img_rect.bottom = 100
        ice_img_rect.top = WINDOW_HEIGHT - 100
        LEVEL = 2
    elif SCORE in range(20, 30):
        fire_img_rect.bottom = 150
        ice_img_rect.top = WINDOW_HEIGHT - 150
        LEVEL = 3
    elif SCORE > 30:
        fire_img_rect.bottom = 200
        ice_img_rect.top = WINDOW_HEIGHT - 200
        LEVEL = 4

def exit():
    pygame.quit()
    sys.exit()
def about():
    text_obj1 = font.render("-> snowman can be moved either up or down", True, GREEN)
    text_obj2 = font.render("-> if snowman goes near to the fire zone then the size of snowman gets strink", True, GREEN)
    text_obj3 = font.render("-> if it goes near ice zone then it expands in size", True, GREEN)
    text_obj4 = font.render("-> maintain high score by escaping from the attacks", True, GREEN)
    while True:
        canvas.fill('BLACK')
        canvas.blit(text_obj1, (22, 0))
        canvas.blit(text_obj2, (22, 30))
        canvas.blit(text_obj3, (22, 60))
        canvas.blit(text_obj4, (22, 90))
        for eve in pygame.event.get():
            if eve.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

def game_loop():
    while True:
        global villain
        global snowman
        global bullet
        villain = Villain()
        snowman = Snowman()
        bullet = Bullet()
        add_new_bullet_counter=0
        global SCORE
        SCORE=0
        global TOP_SCORE
        bullet_list=[]
        pygame.mixer.music.load('firefreezer_theme.wav')
        pygame.mixer.music.play(-1,0,0)
        bg=pygame.image.load('bg.jpg').convert()
        bg_width = bg.get_width()
        scroll = 0
        tiles = math.ceil(WINDOW_WIDTH / bg_width) + 1

        while True:
            for i in range(0,tiles):
                canvas.blit(bg,(i*bg_width+scroll,0))
                scroll -= 5
                if abs(scroll)>bg_width:
                    scroll=0
            check_level(SCORE)
            villain.update()
            add_new_bullet_counter += 1

            if add_new_bullet_counter == ADD_NEW_BULLET_RATE:
                add_new_bullet_counter = 0
                new_bullet = Bullet()
                bullet_list.append(new_bullet)
            for f in bullet_list:
                if f.shooter_img_rect.left <= 0:
                    bullet_list.remove(f)
                    SCORE += 1
                f.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        snowman.up = True
                        snowman.down = False
                    elif event.key == pygame.K_DOWN:
                        snowman.down = True
                        snowman.up = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        snowman.up = False
                        snowman.down = True
                    elif event.key == pygame.K_DOWN:
                        snowman.down = True
                        snowman.up = False

            score_font = font.render('Score:' + str(SCORE), True, BLUE)
            score_font_rect = score_font.get_rect()
            score_font_rect.center = (200, fire_img_rect.bottom + score_font_rect.height / 2)
            canvas.blit(score_font, score_font_rect)

            level_font = font.render('Level:' + str(LEVEL), True, GREEN)
            level_font_rect = level_font.get_rect()
            level_font_rect.center = (500, fire_img_rect.bottom + score_font_rect.height / 2)
            canvas.blit(level_font, level_font_rect)

            top_score_font = font.render('Top Score:' + str(topscore.high_score), True, GREEN)
            top_score_font_rect = top_score_font.get_rect()
            top_score_font_rect.center = (800, fire_img_rect.bottom + score_font_rect.height / 2)
            canvas.blit(top_score_font, top_score_font_rect)

            canvas.blit(fire_img, fire_img_rect)
            canvas.blit(ice_img, ice_img_rect)

            if snowman.snowman_img_rect.top==fire_img_rect.bottom+75:
             snowman.snowman_img=pygame.transform.scale(snowman.snowman_img, (50, 50))
            if snowman.snowman_img_rect.top==fire_img_rect.bottom+100:
             snowman.snowman_img=pygame.transform.scale(snowman.snowman_img, (75, 75))
            if snowman.snowman_img_rect.top == fire_img_rect.bottom+200:
             snowman.snowman_img = pygame.transform.scale(snowman.snowman_img, (100, 100))
            if snowman.snowman_img_rect.top==fire_img_rect.bottom+300:
             snowman.snowman_img=pygame.transform.scale(snowman.snowman_img, (150, 150))
            snowman.update()
            for f in bullet_list:
                if f.shooter_img_rect.colliderect(snowman.snowman_img_rect):
                    game_over()
                    if SCORE > snowman.snowman_score:
                        snowman.snowman_score = SCORE
            pygame.display.update()
            CLOCK.tick(FPS)

main_menu()






              