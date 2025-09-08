import pygame
import math
import random
from pygame import mixer

pygame.init()
screen= pygame.display.set_mode((800,600))

background=pygame.image.load('background.png')
background=pygame.transform.scale(background,(800,600))

#Background sound
mixer.music.load('background.wav')
mixer.music.play(-1)

pygame.display.set_caption("Space Invaders")
icon=pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

#Positions of player
playerImg=pygame.image.load('spaceship.png')
playerImg=pygame.transform.scale(playerImg,(64,64))
playerX=370
playerY=480
playerX_change=0

#positions of enemy
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=6

for i in range(num_of_enemies):
  img=pygame.image.load('enemy.png')
  img=pygame.transform.scale(img,(64,64))
  enemyImg.append(img)
  enemyX_change.append(0.3)
  enemyY_change.append(40)
  enemyX.append(random.randint(0,736))
  enemyY.append(random.randint(50,150))

#positions of bullet
bulletImg=pygame.image.load('bullet.png')
bulletImg=pygame.transform.scale(bulletImg,(32,32))
bulletX_change=0
bulletY_change=1
bulletX=0
bulletY=480
bullet_state="ready"

#score
score=0
font=pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10

def show_score(x,y):
  score_value=font.render("Score: "+str(score),True,(255,255,255))
  screen.blit(score_value,(x,y))

def player(x,y):
  screen.blit(playerImg,(x,y))

def enemy(x,y,i):
  screen.blit(enemyImg[i],(x,y))

def fire_bullet(x,y):
  global bullet_state
  bullet_state="fire"
  screen.blit(bulletImg,(x+16,y+10))

def isCollision(enemyX,enemyY, bulletX, bulletY):
  distance=math.sqrt(math.pow(enemyX-bulletX,2)+math.pow(enemyY-bulletY,2))
  if distance<27:
    return True
  else:
    return False
  
def draw_restart_button():
    button_font = pygame.font.Font('freesansbold.ttf', 32)
    button_text = button_font.render("RESTART", True, (0, 0, 0))
    button_rect = pygame.Rect(300, 350, 200, 60)
    pygame.draw.rect(screen, (255, 255, 255), button_rect)
    screen.blit(button_text, (button_rect.x + 35, button_rect.y + 10))
    return button_rect

def reset_game():
    global playerX, playerY, playerX_change, bulletX, bulletY, bullet_state, score, enemyX, enemyY
    playerX = 370
    playerY = 480
    playerX_change = 0
    bulletX = 0
    bulletY = 480
    bullet_state = "ready"
    score = 0
    for i in range(num_of_enemies):
        enemyX[i] = random.randint(0, 736)
        enemyY[i] = random.randint(50, 150)

game_over = False

#Game Loop
running=True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if not game_over:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    playerX_change=-0.5
                if event.key==pygame.K_RIGHT:
                    playerX_change=0.5
                if event.key==pygame.K_SPACE:
                    if bullet_state=="ready":
                        bullet_sound = mixer.Sound('laser.wav')
                        bullet_sound.play()
                        bulletX=playerX
                        fire_bullet(bulletX,bulletY)
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    playerX_change=0
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if restart_button.collidepoint(mouse_pos):
                    reset_game()
                    game_over = False

    if not game_over:
        # ...existing game logic...
        playerX+=playerX_change
        if playerX<=0:
            playerX=0
        elif playerX>=736:
            playerX=736

        for i in range(num_of_enemies):
            if enemyY[i]>440:
                for j in range(num_of_enemies):
                    enemyY[j]=2000
                game_over = True
                break

            enemyX[i]+=enemyX_change[i]
            if enemyX[i]<=0:
                enemyX_change[i]=0.3
                enemyY[i]+=enemyY_change[i]
            elif enemyX[i]>=736:
                enemyX_change[i]=-0.3
                enemyY[i]+=enemyY_change[i]

            collision=isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                collision_sound=mixer.Sound('explosion.wav')
                collision_sound.play()
                bulletY=480
                bullet_state="ready"
                score+=1
                enemyX[i]=random.randint(0,736)
                enemyY[i]=random.randint(50,150)

            enemy(enemyX[i],enemyY[i],i)

        if bullet_state=="fire":
            fire_bullet(bulletX,bulletY)
            bulletY-=bulletY_change
            if bulletY<=0:
                bulletY=480
                bullet_state="ready"

        show_score(textX,textY)
        player(playerX,playerY)
    else:
        game_over_font=pygame.font.Font('freesansbold.ttf',64)
        game_over_text=game_over_font.render("GAME OVER",True,(255,255,255))
        screen.blit(game_over_text,(200,250))
        restart_button = draw_restart_button()

    pygame.display.update()