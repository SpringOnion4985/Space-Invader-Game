import pygame
import random

pygame.init()
screen= pygame.display.set_mode((800,600))

pygame.display.set_caption("Space Invaders")
icon=pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

playerImg=pygame.image.load('spaceship.png')
playerImg=pygame.transform.scale(playerImg,(64,64))
enemyImg=pygame.image.load('enemy.png')
enemyImg=pygame.transform.scale(enemyImg,(64,64))
playerX=370
playerY=480
playerX_change=0
playerY_change=0
enemyX=random.randint(0,736)
enemyY=random.randint(50,150)

def player(x,y):
  screen.blit(playerImg,(x,y))

def enemy(x,y):
  screen.blit(enemyImg,(x,y))

running=True
while running:
  screen.fill((0,0,0))
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      running=False

    if event.type==pygame.KEYDOWN:
      print("A keystroke has been pressed")
      if event.key==pygame.K_LEFT:
        print("Left arrow key is pressed")
        playerX_change=-0.3
      if event.key==pygame.K_RIGHT:
        print("Right arrow key is pressed")
        playerX_change=0.3
      if event.key==pygame.K_UP:
        print("Up arrow key is pressed")
        playerY_change=-0.3
      if event.key==pygame.K_DOWN:
        print("Down arrow key is pressed")
        playerY_change=0.3

    if event.type==pygame.KEYUP:
      if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_UP or event.key==pygame.K_DOWN:
        print("Key stroke has been released")
        playerX_change=0
        playerY_change=0

  playerX+=playerX_change
  if playerX<=0:
    playerX=0
  elif playerX>=736:
    playerX=736

  playerY+=playerY_change
  if playerY<=0:
    playerY=0
  elif playerY>=536:
    playerY=536
  enemy(enemyX,enemyY)
  player(playerX,playerY)
  pygame.display.update()