# Practiced from Clear Code

import pygame
import sys
import random

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
screen_width, screen_height = 800, 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()

FPS = 60

# game rectangle
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15 , 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

# Colors
bg_color = pygame.Color("grey12")
light_grey = (200, 200, 200)

# speed
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7

# text variables
player_score = opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)

# sound 
pong_sound = pygame.mixer.Sound("./assets/sound/pong.ogg")
score_sound = pygame.mixer.Sound("./assets/sound/score.ogg")

# score timer
score_time = True

def ball_animation():
    global ball_speed_x, ball_speed_y
    global player_score, opponent_score
    global score_time

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_y *= -1

    if ball.left <= 0:
        pygame.mixer.Sound.play(score_sound)
        player_score += 1
        score_time = pygame.time.get_ticks()

    if ball.right >= screen_width:
        pygame.mixer.Sound.play(score_sound)
        opponent_score += 1
        score_time = pygame.time.get_ticks()

    if ball.colliderect(player) and ball_speed_x > 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.right - player.left) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - player.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1


    if ball.colliderect(opponent) and ball_speed_x < 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.left - opponent.right) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1

def ball_restart():
    global ball_speed_y, ball_speed_x
    global score_time

    current_time = pygame.time.get_ticks()
    ball.center = (screen_width / 2, screen_height / 2)
    
    if current_time - score_time < 700:
        number_three = game_font.render("3", True, light_grey)
        screen.blit(number_three, (screen_width/2 - 10, screen_height/2 + 20))

    if 700 < current_time - score_time < 1400:
        number_two = game_font.render("2", True, light_grey)
        screen.blit(number_two, (screen_width/2 - 10, screen_height/2 + 20))

    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render("1", True, light_grey)
        screen.blit(number_one, (screen_width/2 - 10, screen_height/2 + 20))

    if current_time - score_time < 2100:
        ball_speed_x = ball_speed_y = 0
    else:
        ball_speed_y = 7 * random.choice((1, -1))
        ball_speed_x = 7 * random.choice((1, -1))
        score_time = None

def player_animation():
    player.y += player_speed
    
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_animation()
    player_animation()
    opponent_ai()

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))

    if score_time:
        ball_restart()

    player_text = game_font.render(f"{player_score}", True, light_grey)
    screen.blit(player_text, (440, screen_height/2 - 16))
    opponent_text = game_font.render(f"{opponent_score}", True, light_grey)
    screen.blit(opponent_text, (340, screen_height/2 - 16))

    pygame.display.flip()
    clock.tick(FPS)    
