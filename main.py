import pygame
import random
from sys import exit

pygame.init()

window = pygame.display.set_mode((800,400))

timer = pygame.time.Clock()

gameActive = False

gravity = 0

score = 0

text = pygame.font.Font("Assets/Pixeltype.ttf", 50)

message = text.render('test', False, (0,0,0))
messageRect = message.get_rect(center = (400,300))

# Player defenition code
# there is a convert_alpha command in order to "increase performance"
player = pygame.image.load('Assets/Ball1.png').convert_alpha()
# This rectangle will be drawn around the player and used for collisions
playerRect = player.get_rect(topleft = (100,0))
# This list will be used for animation, it stores 
# the other assets of the player "Flying animation"
playerAnimate = []

# Coin setup
coin = pygame.image.load('Assets/Coin.png').convert_alpha()
coinRect = coin.get_rect(topleft = (20,20))

# Top Wall
topWall = pygame.image.load('Assets/Pipe.png').convert_alpha()
topWallRect = topWall.get_rect(topleft = (900,-150))

# Bottom Wall
bottomWall = pygame.image.load('Assets/Pipe.png').convert_alpha()
bottomWallRect = bottomWall.get_rect(topleft = (1100,0))

def wallCollision(thing, wall, x, y):
    global gameActive
    wall.x -= 3
    if wall.x < -100:
        wall.x = 1000
        wall.y = random.randint(x,y)
    if thing.colliderect(wall):
            gameActive = False
            

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
    global coinRect, playerRect, topWallRect, bottomWallRect, score
    coinRect.x = 20
    coinRect.y = 20
    playerRect.x = 100
    playerRect.y = 0
    topWallRect.x = 900
    topWallRect.y = -150
    bottomWallRect.x = 1100
    bottomWallRect.y = 0
    score = 0

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
        window.blit(message, messageRect)

        message = text.render(f'{score}', False, (0,0,0))

        playerRect.y+=gravity
        gravity+=0.5

        wallCollision(playerRect, topWallRect, -200,-70)
        wallCollision(playerRect, bottomWallRect, 200, 270)
        coinCollision(playerRect, coinRect)


    else:
        window.fill((173,216,230))
        window.blit(message, messageRect)
        message = text.render(f'Score is: {score}', False, (0,0,0))
        reset()

    timer.tick(60)
    pygame.display.update()