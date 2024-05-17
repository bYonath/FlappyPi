import pygame
import random
from sys import exit

pygame.init()

window = pygame.display.set_mode((800,400))
pygame.display.set_caption('FlappyPi')

timer = pygame.time.Clock()

gameActive = False

gravity = 0

score = 0

text = pygame.font.Font("Pixeltype.ttf", 50)

i = 0

message = text.render('test', False, (0,0,0))
messageRect = message.get_rect(center = (300,300))
messageRectActive = message.get_rect(topleft = (750,20))

title = text.render('FlappyPi', False, (0,0,0))
titleRect = title.get_rect(center = (350,50))

info = text.render('Press Space To Start!', False, (0,0,0))
infoRect = info.get_rect(center = (350, 150))

# Player defenition code

# This list will be used for animation, it stores 
# the other assets of the player "Flying animation"
playerAnimate = ['Ball1.png', 'Ball2.png', 'Ball3.png']
# there is a convert_alpha command in order to "increase performance"
player = pygame.image.load(playerAnimate[0]).convert_alpha()
# This rectangle will be drawn around the player and used for collisions
playerRect = player.get_rect(topleft = (100,0))

# Coin setup
coin = pygame.image.load('Coin.png').convert_alpha()
coinRect = coin.get_rect(topleft = (20,20))
# Using the coin as the window icon
pygame.display.set_icon(coin)
# Top Wall
topWall = pygame.image.load('Pipe.png').convert_alpha()
topWallRect = topWall.get_rect(topleft = (900,-150))

# Bottom Wall
bottomWall = pygame.image.load('Pipe.png').convert_alpha()
bottomWallRect = bottomWall.get_rect(topleft = (1100,0))

def coinCollision(thing, coin):
    global score
    global message
    coin.x -= 3
    if coin.x < -100:
            coin.x = 1000
            coin.y = random.randint(50,200)
    if thing.colliderect(coin):
        score += 1
        coin.y = 1000
        message = text.render(f'{score}', False, (0,0,0))
        print(score)

def reset():
    global coinRect, playerRect, topWallRect, bottomWallRect, gravity
    coinRect.x = 20
    coinRect.y = 20
    playerRect.x = 100
    playerRect.y = 0
    topWallRect.x = 900
    topWallRect.y = -150
    bottomWallRect.x = 1100
    bottomWallRect.y = 0
    gravity = 0

def wallCollision(thing, wall, x, y):
    global gameActive
    wall.x -= 3
    if wall.x < -100:
        wall.x = 1000
        wall.y = random.randint(x,y)
    if thing.colliderect(wall):
            gameActive = False
            reset()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if gameActive:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameActive = False
                    print(gameActive)
                if event.key == pygame.K_SPACE:
                    gravity = -10
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameActive = True
                    score = 0
                    print(gameActive)
    # This will fill the window so that it is light blue * it uses
    # a tuple for rgb values
    if gameActive:
        window.fill((173,216,230))
        # Positioning of the code is important!
        window.blit(coin, coinRect)
        window.blit(player, playerRect)
        window.blit(topWall, topWallRect)
        window.blit(bottomWall,bottomWallRect)
        window.blit(message, messageRectActive)

        message = text.render(f'{score}', False, (0,0,0))
        

        if i > 2:
            i = 0
        else:
            player = pygame.image.load(playerAnimate[int(i)]).convert_alpha()       
            i += 0.1

        playerRect.y+=gravity
        gravity+=0.5

        wallCollision(playerRect, topWallRect, -200,-70)
        wallCollision(playerRect, bottomWallRect, 200, 270)
        coinCollision(playerRect, coinRect)

        if playerRect.y > 600 or playerRect.y < -200:
            gameActive = False
            reset()


    else:
        window.fill((173,216,230))
        window.blit(message, messageRect)
        window.blit(title, titleRect)
        window.blit(info, infoRect)
        message = text.render(f'Score is: {score}', False, (0,0,0))

    timer.tick(60)
    pygame.display.update()