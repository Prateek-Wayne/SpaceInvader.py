import pygame
import random
import math
from pygame import mixer

# initialize the py_game
pygame.init()
# create the screen
screen = pygame.display.set_mode((800, 600))
# Background
background_img = pygame.image.load('background.png')
# TITLE AND DISPLAY NAME
pygame.display.set_caption("Space Invaders 2021")
icon = pygame.image.load('spaceship 64px.png')
pygame.display.set_icon(icon)
# Sound
mixer.music.load("background.wav")
mixer.music.play(-1)
# SCORE
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10
# GAMEOVER
game_over_font = pygame.font.Font('freesansbold.ttf', 64)




# PLAYER
playerImg = pygame.image.load('battleship.png')
playerX = 355
playerY = 500
playerX_change = 0
# ENEMY
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemy = 6
for i in range(num_of_enemy):
    enemyImg.append(pygame.image.load('alien 64px.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(2)
    enemyY_change.append(30)
 # Bullets
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 500
bulletX_change = 0
bulletY_change = 4
bullet_state = 'ready'

def game_over_text():
    over_ = font.render('GAME OVER', True, (225, 225, 225))
    screen.blit(over_, (400, 300))

def show_score(x, y):
    show = font.render('Score:' + str(score_value), True, (225, 225, 225))
    screen.blit(show, (x, y))


def Player(X, Y):
    screen.blit(playerImg, (X, Y))


def Enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def Bullet_fire(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 2))


def Colli_son(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance <= 27:
        return True
    else:
        return False


# GAME LOOP
running = True
while running:
    # created a screen
    screen.fill((0, 0, 7))
    # Background
    screen.blit(background_img, (0, 0))
    for event in pygame.event.get():
        # keystroke is pressed or not ****************
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                # print('left arrow')
                playerX_change = -2.5
            if event.key == pygame.K_d:
                # print('right arrow')
                playerX_change = 2.5
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    bulletX = playerX
                    Bullet_fire(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 00

    # playerX=playerX+0.04
    # playerY=playerY-0.03
    # print(playerX,playerY)
    Player(playerX, playerY)
    if playerX < 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    playerX = playerX + playerX_change

    for i in range(num_of_enemy):
        if enemyY[i] > 440:
            for j in range(num_of_enemy):
                enemyY[j]=2000
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] < 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyY[i] += enemyY_change[i]
            enemyX_change[i] = -2
            # Collison
        collisson = Colli_son(enemyX[i], enemyY[i], bulletX, bulletY)
        if collisson:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 500
            bullet_state = 'ready'
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(25, 100)
            # enemy
        Enemy(enemyX[i], enemyY[i], i)
    # bullet
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'
    if bullet_state is 'fire':
        Bullet_fire(bulletX, bulletY)
        bulletY -= bulletY_change
    show_score(textX, textY)
    pygame.display.update()  # always come
