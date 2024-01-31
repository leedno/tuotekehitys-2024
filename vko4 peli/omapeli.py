import pygame
import sys
from pygame.locals import *
pygame.init()
import time

screen_width = 1200 #screen width
screen_height = 750 #screen height
dispSurf = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("jutix1 futispeli")

# load images
font = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 100)
footballpitch = pygame.image.load("football_pitch.png").convert()
player1_big = pygame.image.load("player_2.png").convert()
player2_big = pygame.image.load("player_1.png").convert()
left_g = pygame.image.load("left_goal.png").convert()
right_g = pygame.image.load("right_goal.png").convert()
ball_big = pygame.image.load("ball.png").convert()

# RESIZE EVERYTHING
goal_width = 150  # goal width
goal_height = 300  # goal height
player_width = 60  # player width
player_height = 130  #player height
ball_size = 50
player2 = pygame.transform.scale(player2_big, (player_width, player_height))
player1 = pygame.transform.scale(player1_big, (player_width, player_height))
left_goal = pygame.transform.scale(left_g, (goal_width, goal_height))
right_goal = pygame.transform.scale(right_g, (goal_width, goal_height))
ball = pygame.transform.scale(ball_big, (ball_size, ball_size))

rectangle = pygame.Surface((1,goal_height))
rectangle2 = pygame.Surface((1,goal_height))

# colors
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
dispSurf.blit(right_goal, (0,0))
dispSurf.blit(left_goal, (0,0))
dispSurf.blit(ball, (0,0))
dispSurf.blit(rectangle, (0,0))
dispSurf.blit(rectangle2, (0,0))

pygame.display.flip()

player1Area = player1.get_rect()
player2Area = player2.get_rect()
ballArea = ball.get_rect()
left_goalArea = left_goal.get_rect()
right_goalArea = right_goal.get_rect()
rectangleArea = rectangle.get_rect()
rectangle2Area = rectangle2.get_rect()

player1Area.left = 900
player1Area.top = screen_height-player_height
player2Area.left = 250
player2Area.top = screen_height-player_height
left_goalArea.left = 0
left_goalArea.top = screen_height-goal_height
right_goalArea.left = screen_width-goal_width
right_goalArea.top = screen_height-goal_height
rectangleArea.left = goal_width
rectangleArea.top = screen_height-goal_height
rectangle2Area.left = screen_width-goal_width
rectangle2Area.top = screen_height-goal_height


speed = [1,1]
score = 0
score2 = 0

start_screen = True
end_screen = False
keys = pygame.key.get_pressed()

while True:
    uus_peli = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        #check for mouse clicks
        if event.type == MOUSEBUTTONDOWN and start_screen:
            start_screen = False
        #check if space key has been pressed
        if event.type == KEYDOWN and end_screen:
            if event.key == K_SPACE:
                end_screen = False
                #return players to starting position
                player1Area.left = 900
                player1Area.top = screen_height-player_height
                player2Area.left = 250
                player2Area.top = screen_height-player_height

    
    if start_screen: # start screen
        dispSurf.fill(black)
        start_text = font2.render("Click to start", True, white)
        start_text_rect = start_text.get_rect(center=(screen_width//2, screen_height//2))
        dispSurf.blit(start_text, start_text_rect)
        pygame.display.flip()
        continue
    
    if end_screen: # end screen
        dispSurf.fill(black)
        start_text = font2.render("Press space to restart or esc to quit", True, white)
        start_text_rect = start_text.get_rect(center=(screen_width//2, screen_height//2))
        dispSurf.blit(start_text, start_text_rect)
        pygame.display.flip()
        continue


    ballArea.move_ip(speed)
    
    #ball baounces from walls
    if ballArea.left < 0 or ballArea.right > screen_width:
        speed[0] = -speed[0]
    if ballArea.top < 0 or ballArea.bottom > screen_height:
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
    if left_goalArea.colliderect(ballArea):
        if left_goalArea.colliderect(ballArea.move(-speed[0],0)):
            speed[1] = -speed[1]
        else:
            speed[0] = -speed[0]
    if right_goalArea.colliderect(ballArea):
        if right_goalArea.colliderect(ballArea.move(-speed[0],0)):
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
    #player 2 moves
    pressings2 = pygame.key.get_pressed()
    if pressings2[K_a] and player2Area.left > 0:
        player2Area.move_ip((-1,0))
    if pressings2[K_d] and player2Area.left < screen_width-player_width:
        player2Area.move_ip((1,0))
    if pressings2[K_s] and player2Area.top < screen_height-player_height:
        player2Area.move_ip((0,1))
    if pressings2[K_w] and player2Area.top > 0:
        player2Area.move_ip((0,-1))
    #player 1 moves
    pressings1 = pygame.key.get_pressed()
    if pressings1[K_LEFT] and player1Area.left > 0:
        player1Area.move_ip((-1,0))
    if pressings1[K_RIGHT] and player1Area.left < screen_width-player_width:
        player1Area.move_ip((1,0))
    if pressings1[K_DOWN] and player1Area.top < screen_height-player_height:
        player1Area.move_ip((0,1))
    if pressings1[K_UP] and player1Area.top > 0:
        player1Area.move_ip((0,-1))

    if score == 3:
        player1_win_text = font2.render(f"Player 1 WINNER:", True, (255, 255, 255))
        dispSurf.blit(player1_win_text, (300, 300))
        pygame.display.flip()
        time.sleep(2)
        uus_peli = True

    if score2 == 3:
        player2_win_text = font2.render(f"Player 2 WINNER", True, (255, 255, 255))
        dispSurf.blit(player2_win_text, (300, 300))
        pygame.display.flip()
        time.sleep(2)
        uus_peli = True

    if uus_peli == True:
        score = 0
        score2 = 0
        end_screen = True
        continue
    
    dispSurf.blit(footballpitch, (0,0))
    dispSurf.blit(right_goal, right_goalArea)
    dispSurf.blit(left_goal, left_goalArea)
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
