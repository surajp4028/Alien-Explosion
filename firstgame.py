import pygame
import sys
import random
import math
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((800, 600))  #screen width, height
#background
bg = pygame.image.load('space (1).jpg')

#bg sounds
mixer.music.load('background.wav')
mixer.music.play(-1)  #1 for 1 time , 2 for 2 times play and -1 for infinite loop

pygame.display.set_caption("First Game")
icon = pygame.image.load('rocket.png')
pygame.display.set_icon(icon)
playerImg = pygame.image.load('rocket1.png')

playerX = 370
playerY = 480
player_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


player2 = pygame.image.load('alien.png')
enemyX = random.randrange(0, 700)
enemyY = random.randrange(0, 100)
enemyX_change = 0.3
enemyY_change = 40


def enemy(x, y):
    screen.blit(player2, (x, y))


bullet = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 2
bullet_state = "ready"  # ready state you can't fire bullets


def bullet_fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x + 16, y + 16))


def iscollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) +
                         (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10


def show_score(x, y):
    score = font.render("score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


#game loop
running = True
while running:
    # screen.fill((198, 156, 234))
    screen.blit(bg, (0, 0))
    # playerX +=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # player_change = -5
            if event.key == pygame.K_LEFT:
                player_change = -1
                # print("key left")
            if event.key == pygame.K_RIGHT:
                player_change = 1
                # print("key right")
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    bullet_fire(playerX, bulletY)
        if event.type == pygame.KEYUP:
            # player_change = -5
            if event.key == pygame.K_LEFT:
                player_change = 0
                # print("key left up")
            if event.key == pygame.K_RIGHT:
                player_change = 0
                # print("key right up")

    playerX += player_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change
    if enemyY >= 400:
        enemyX = random.randrange(0, 700)
        enemyY = random.randrange(0, 300)
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        bullet_fire(bulletX, bulletY)
        bulletY -= bulletY_change

    collision = iscollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        explosion_sound = mixer.Sound('explosion.wav')
        explosion_sound.play()
        bulletY = 480
        bullet_state = "ready"
        score_value += 1
        print(score_value)
        enemyX = random.randrange(0, 700)
        enemyY = random.randrange(0, 100)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    show_score(textX, textY)
    pygame.display.update()
