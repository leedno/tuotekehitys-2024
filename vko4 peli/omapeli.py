import pygame
import sys
from pygame.locals import *
pygame.init()
import time

width = 1200
height = 750
dispSurf = pygame.display.set_mode((width,height))
pygame.display.set_caption("jutix1 futispeli")

font = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 100)
footballpitch = pygame.image.load("footballpitch.jpg").convert()
player1 = pygame.image.load("player1.jpg").convert()
player2 = pygame.image.load("player2.jpg").convert()
goal = pygame.image.load("goal.jpg").convert()
maali = pygame.image.load("maali.jpg").convert()
ball = pygame.image.load("ball.png").convert()
rectangle = pygame.Surface((1,240))
rectangle2 = pygame.Surface((1,240))

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
pink = (255,0,130)

rectangle.fill(red)
rectangle2.fill(red)


dispSurf.blit(footballpitch, (0,0))
dispSurf.blit(player1, (0,0))
dispSurf.blit(player2, (0,0))
dispSurf.blit(maali, (0,0))
dispSurf.blit(goal, (0,0))
dispSurf.blit(ball, (0,0))
dispSurf.blit(rectangle, (0,0))
dispSurf.blit(rectangle2, (0,0))

pygame.display.flip()

player1Area = player1.get_rect()
player2Area = player2.get_rect()
ballArea = ball.get_rect()
goalArea = goal.get_rect()
maaliArea = maali.get_rect()
rectangleArea = rectangle.get_rect()
rectangle2Area = rectangle2.get_rect()

player1Area.left = 900
player1Area.top = 650
player2Area.left = 250
player2Area.top = 650
goalArea.top = 496
maaliArea.left = 1000
maaliArea.top = 496
rectangleArea.left = 201
rectangleArea.top = 510
rectangle2Area.left = 998
rectangle2Area.top = 510


speed = [2,2]
score = 0
score2 = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            

    ballArea.move_ip(speed)
    
    #ball baounces from walls
    if ballArea.left < 0 or ballArea.right > width:
        speed[0] = -speed[0]
    if ballArea.top < 0 or ballArea.bottom > height:
        speed[1] = -speed[1]

    #ball bounces from players
    if player2Area.colliderect(ballArea):
        if player2Area.colliderect(ballArea.move(-speed[0],0)):
            speed[1] = -speed[1]
        else:
            speed[0] = -speed[0]
    if player1Area.colliderect(ballArea):
        if player1Area.colliderect(ballArea.move(-speed[0],0)):
            speed[1] = -speed[1]
        else:
            speed[0] = -speed[0]

    #ball bounces from goals
    if goalArea.colliderect(ballArea):
        if goalArea.colliderect(ballArea.move(-speed[0],0)):
            speed[1] = -speed[1]
        else:
            speed[0] = -speed[0]
    if maaliArea.colliderect(ballArea):
        if maaliArea.colliderect(ballArea.move(-speed[0],0)):
            speed[1] = -speed[1]
        else:
            speed[0] = -speed[0]

    if rectangleArea.colliderect(ballArea):
        if rectangleArea.colliderect(ballArea.move(-speed[0],0)):
            speed[1] = -speed[1]
        else:
            speed[0] = -speed[0]
    if rectangle2Area.colliderect(ballArea):
        if rectangle2Area.colliderect(ballArea.move(-speed[0],0)):
            speed[1] = -speed[1]
        else:
            speed[0] = -speed[0]
   
    if rectangleArea.colliderect(ballArea):
        ballArea.left = 600
        ballArea.top = 375
        score += 1

    if rectangle2Area.colliderect(ballArea):
        ballArea.left = 600
        ballArea.top = 375
        score2 += 1

    pressings2 = pygame.key.get_pressed()
    if pressings2[K_a]:
        player2Area.move_ip((-1,0))
    if pressings2[K_d]:
        player2Area.move_ip((1,0))
    if pressings2[K_s]:
        player2Area.move_ip((0,1))
    if pressings2[K_w]:
        player2Area.move_ip((0,-1))

    pressings1 = pygame.key.get_pressed()
    if pressings1[K_LEFT]:
        player1Area.move_ip((-1,0))
    if pressings1[K_RIGHT]:
        player1Area.move_ip((1,0))
    if pressings1[K_DOWN]:
        player1Area.move_ip((0,1))
    if pressings1[K_UP]:
        player1Area.move_ip((0,-1))

    if score == 3:
        player1_win_text = font2.render(f"Player 1 WINNER:", True, (255, 255, 255))
        dispSurf.blit(player1_win_text, (300, 300))
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    if score2 == 3:
        player2_win_text = font2.render(f"Player 2 WINNER", True, (255, 255, 255))
        dispSurf.blit(player2_win_text, (300, 300))
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    
    dispSurf.blit(footballpitch, (0,0))
    dispSurf.blit(maali, maaliArea)
    dispSurf.blit(goal, goalArea)
    dispSurf.blit(player1, player1Area)
    dispSurf.blit(player2, player2Area)
    dispSurf.blit(ball, ballArea)
    dispSurf.blit(rectangle, rectangleArea)
    dispSurf.blit(rectangle2, rectangle2Area)
    score_text = font.render(f"Player 1:  {score}", True, (255, 255, 255))
    score2_text = font.render(f"Player 2:  {score2}", True, (255, 255, 255))
    dispSurf.blit(score2_text, (600, 25))
    dispSurf.blit(score_text, (400, 25))



    pygame.display.flip()
