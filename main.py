

import pygame
import sys
import random
pygame.init()


screen = pygame.display.set_mode((500, 800))
clock = pygame.time.Clock()
floor_move_up = 300
fps = 120
isPlaying = True
gravity = .25
ball_movement_y = 0
ball_movement_x = 0

floor_position = [0, 30, 60, 90, 130, 160, 190,  230, 260, 290, 300]
random_postion_1 = random.choice(floor_position)
random_postion_2 = random.choice(floor_position)
random_postion_3 = random.choice(floor_position)
random_postion_4 = random.choice(floor_position)
random_postion_5 = random.choice(floor_position)


# backround
background = pygame.image.load('assets/imgs/bg.jpg')

# floor
floor = pygame.image.load('assets/imgs/floor.png')
floor = pygame.transform.scale(floor, (240, 50))


# spine
spine = pygame.image.load('assets/imgs/spine.png')
spine = pygame.transform.scale(spine, (200, 60))

# ball
ball = pygame.image.load('assets/imgs/ball.png')
ball = pygame.transform.scale(ball, (60, 60))
ball_rect = ball.get_rect(center=(random_postion_1 + 75, 0))


def draw_floor():

    floor_rect_1 = floor.get_rect(center=(random_postion_1, floor_move_up))
    floor_rect_2 = floor.get_rect(center=(random_postion_2, floor_move_up+120))
    floor_rect_3 = floor.get_rect(center=(random_postion_3, floor_move_up+240))
    floor_rect_4 = floor.get_rect(center=(random_postion_4, floor_move_up+360))
    screen.blit(floor, floor_rect_1)
    screen.blit(floor, floor_rect_2)
    screen.blit(floor, floor_rect_3)
    screen.blit(floor, floor_rect_4)


while isPlaying:
    for event in pygame.event.get():
        # close game
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        # control ball
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ball_movement_x = +2
            if event.key == pygame.K_LEFT:
                ball_movement_x = -2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ball_movement_x = 0
            if event.key == pygame.K_LEFT:
                ball_movement_x = 0

    screen.blit(background, (0, 0))  # Thêm hình ảnh vào màn hình

    draw_floor()

    if floor_move_up <= 0:
        floor_move_up = 800
    screen.blit(spine, (random_postion_5, floor_move_up+800))

    screen.blit(ball, ball_rect)

    ball_movement_y += gravity
    ball_rect.centery += ball_movement_y
    ball_rect.centerx += ball_movement_x

    floor_move_up -= 1

    pygame.display.update()
    clock.tick(fps)
