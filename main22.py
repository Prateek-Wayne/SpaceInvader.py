import time
import pygame
import random
from pygame import mixer

pygame.init()
# CREATING SCREEN
screen_WIDTH = 600
screen_HEIGHT = 600
# crash_sound=mixer.Sound('crash.mp3')
screen = pygame.display.set_mode((screen_WIDTH, screen_HEIGHT))
pygame.display.set_caption('Snake Game')
# CREATE ICON
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)
# PLAYER SNAKE
snake = pygame.image.load('snake new32px.png').convert_alpha()
# snake_X=250
# snake_Y=250
# velocity_x=0
# velocity_y=0
# LENGTH INCREASE
snake_list = []
snake_length = 1
#HISCORE
with open("hiscore.txt", "r")as f:
    hiscore = f.read()


def player(snake_list):
    # print(snake_list)
    for x, y in snake_list:
        screen.blit(snake, (x, y))


# FOOD
food_X = random.randint(60, screen_WIDTH / 2)
food_Y = random.randint(60, screen_WIDTH / 2)


def food():
    global food_X
    global food_Y
    apple = pygame.image.load('apple 32.png')
    screen.blit(apple, (food_X, food_Y))


# SCORE
score = 0
# FONT
font = pygame.font.SysFont(None, 30)


def text_Screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, [x, y])


# FPS
fps = 55
clock = pygame.time.Clock()

# WELCOME SCREEN
def welcome():
    global running

    home=pygame.image.load('snake 512).png').convert_alpha()
    while running:
        screen.fill((233,210,229))
        screen.blit(home, (30, 50))

        text_Screen(' Welcome to Snake Game',(235, 9, 43),200,100)
        text_Screen(':: PRESS SPACE TO ENTER THE GAME',(235, 9, 43),26,300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    running=False
                if event.key==pygame.K_SPACE:
                    gameloop()

        pygame.display.update()
        clock.tick(fps)
# GAMEOVER
def gameover():
    global running
    global  hiscore
    with open("hiscore.txt","w") as f:
        f.write(str(hiscore))

    while running:
        screen.fill((233,210,229))
        text_Screen(' Game Over', (235, 9, 43), 250, 300)
        # text_Screen(':: Press SPACE to Play Again', (235, 9, 43), 50, 400)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type==pygame.KEYDOWN:
                # if event.key==pygame.K_SPACE:
                #     gameloop()
                if event.key==pygame.K_ESCAPE:
                    running = False


        pygame.display.update()

# GAME LOOP
def gameloop():

    # GAME SPECIFIC VARIABLES
    snake_X = 250
    snake_Y = 250
    difficulty=4
    velocity_x = 0
    velocity_y = 0
    # GLOBALS
    global hiscore
    global food_X
    global food_Y
    global score
    global snake_length
    global snake_list
    global running
    global screen

    crash_sound = mixer.Sound('crash.mp3')

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_RIGHT:
                    snake_X += 16
                    velocity_x = difficulty
                    velocity_y = 0
                if event.key == pygame.K_LEFT:
                    snake_X += -16
                    velocity_x = -difficulty
                    velocity_y = 0
                if event.key == pygame.K_UP:
                    snake_Y -= 16
                    velocity_y = -difficulty
                    velocity_x = 0
                if event.key == pygame.K_DOWN:
                    snake_Y += 16
                    velocity_y = difficulty
                    velocity_x = 0
        snake_X += velocity_x
        snake_Y += velocity_y
        # BOUNDRIES
        if snake_X >= 569 or snake_X < 4.5 or snake_Y >= 569 or snake_Y < 4.5:
            crash_sound.play()
            time.sleep(0.95)
            gameover()

        # COLLISON
        if abs(snake_X - food_X) < 24 and abs(snake_Y - food_Y) < 24:
            score += 10
            # print('Yummmy!!!!!')
            # explosionSound = mixer.Sound("explosion.wav")
            eat_sound=mixer.Sound('food_G1U6tlb.mp3')
            eat_sound.play()
            food_X = random.randint(20, 500)
            food_Y = random.randint(20, 500)
            snake_length += 1
        if score>int(hiscore):
            hiscore=score


        screen.fill((45, 237, 119))
        text_Screen("Score: " + str(score)+"|hi-score "+str(hiscore), (235, 9, 43), 5, 5)
        food()
        head = []
        head.append(snake_X)
        head.append(snake_Y)
        snake_list.append(head)

        if len(snake_list) > snake_length:
            del snake_list[0]
        if head in snake_list[:-1]:
            crash_sound.play()
            time.sleep(0.95)
            gameover()

        player(snake_list)

        pygame.display.update()
        clock.tick(fps)



running = True
welcome()

quit()
