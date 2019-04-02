import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)  # ekranı belirle
pygame.display.set_caption("Pong Game")  # başlık

# Creating 2 bars, a ball and background.
back = pygame.Surface((640, 480))  # alanı belirliyor
background = back.convert()
background.fill((0, 0, 0))  # arkaplan rengi
paddle = pygame.Surface((10, 50))  # bar tanımlıyoruz
paddle1 = paddle.convert()
paddle1.fill((0, 0, 255))  # bar rengi
paddle2 = paddle.convert()
paddle2.fill((255, 0, 0))
ball_sur = pygame.Surface((15, 15))  # topu belirliyoruz
ball = pygame.draw.circle(ball_sur, (0, 255, 0), (int(15 / 2), int(15 / 2)), int(15 / 2))  # yuvarlaklık, rengi
ball = ball_sur.convert()
ball.set_colorkey((0, 0, 0))

# some definitions,başlangıç noktaları
paddle1_x, paddle2_x = 10., 620.
paddle1_y, paddle2_y = 215., 215.
ball_x, ball_y = 307.5, 232.5
paddle1_move, paddle2_move = 0., 0.
speed_x, speed_y, speed_ball = 250., 250., 250.
paddle1_score, paddle2_score = 0, 0
# clock and font objects
clock = pygame.time.Clock()
font = pygame.font.SysFont("calibri", 40)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_w:
                paddle1_move = -ai_speed  # tuşa basınca hareketi değişkene eşitlemiş
            elif event.key == K_s:
                paddle1_move = ai_speed
        elif event.type == KEYUP:
            if event.key == K_w:
                paddle1_move = 0.  # tuşları bırakınca hareketi sıfırlama
            elif event.key == K_s:
                paddle1_move = 0.
        if event.type == KEYDOWN:
            if event.key == K_UP:
                paddle2_move = -ai_speed  # tuşa basınca hareketi değişkene eşitlemiş
            elif event.key == K_DOWN:
                paddle2_move = ai_speed
        elif event.type == KEYUP:
            if event.key == K_UP:
                paddle2_move = 0.  # tuşları bırakınca hareketi sıfırlama
            elif event.key == K_DOWN:
                paddle2_move = 0.

    score1 = font.render(str(paddle1_score), True, (255, 255, 255))
    score2 = font.render(str(paddle2_score), True, (255, 255, 255))

    screen.blit(background, (0, 0)) 
    frame = pygame.draw.rect(screen, (255, 255, 255), Rect((5, 5), (630, 470)), 2)  # dikdörtgen çiz
    middle_line = pygame.draw.aaline(screen, (255, 255, 255), (330, 5), (330, 475))  # ortadaki çizgi
    screen.blit(paddle1, (paddle1_x, paddle1_y))  # ekrana bastır
    screen.blit(paddle2, (paddle2_x, paddle2_y))
    screen.blit(ball, (ball_x, ball_y))
    screen.blit(score1, (250., 210.))
    screen.blit(score2, (380., 210.))

    paddle1_y += paddle1_move
    paddle2_y += paddle2_move

    # movement of circle
    time_passed = clock.tick(30)
    time_sec = time_passed / 1000.0

    ball_x += speed_x * time_sec
    ball_y += speed_y * time_sec
    ai_speed = speed_ball * time_sec
    # AI of the computer.

    if paddle1_y >= 420.:
        paddle1_y = 420.
    elif paddle1_y <= 10.:
        paddle1_y = 10.
    if paddle2_y >= 420.:
        paddle2_y = 420.
    elif paddle2_y <= 10.:
        paddle2_y = 10.
    # since i don't know anything about collision, ball hitting bars goes like this.
    if ball_x <= paddle1_x + 10.:
        if ball_y >= paddle1_y - 7.5 and ball_y <= paddle1_y + 42.5:
            ball_x = 20.
            speed_x = -speed_x
    if ball_x >= paddle2_x - 15.:
        if ball_y >= paddle2_y - 7.5 and ball_y <= paddle2_y + 42.5:
            ball_x = 605.
            speed_x = -speed_x
    if ball_x < 5.:  # top çizgiyi çeçti mi
        paddle2_score += 1  # skoru artır
        ball_x, ball_y = 320., 232.5  # top çizgiyi geçince yeni koordinatlar
        paddle1_y, paddle2_y = 215., 215.
    elif ball_x > 620.:
        paddle1_score += 1
        ball_x, ball_y = 307.5, 232.5  # (640-25)/2 ve (480-15)/2 15:circle diameter
        paddle1_y, paddle2_y = 215., 215.
    if ball_y <= 10.:
        speed_y = -speed_y
        ball_y = 10.
    elif ball_y >= 460:
        speed_y = -speed_y
        ball_y = 460

    pygame.display.update()
