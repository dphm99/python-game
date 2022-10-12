

import pygame
import sys
import random
pygame.init()

# backround
background = pygame.image.load('assets/imgs/bg.jpg')

# floor
floor = pygame.image.load('assets/imgs/floor.png')
floor = pygame.transform.scale(floor, (240, 50))
floor_position = [0, 30, 60, 90, 130, 160, 190,  230, 260, 290, 300]

# spine
spine = pygame.image.load('assets/imgs/spine.png')
spine = pygame.transform.scale(spine, (200, 60))

# ball
ball = pygame.image.load('assets/imgs/ball.png')
ball = pygame.transform.scale(ball, (60, 60))


random_postion_1 = random.choice(floor_position)
random_postion_2 = random.choice(floor_position)
random_postion_3 = random.choice(floor_position)
random_postion_4 = random.choice(floor_position)
random_postion_5 = random.choice(floor_position)


def draw_floor():
    screen.blit(floor, (random_postion_1, floor_move_up))
    screen.blit(floor, (random_postion_2, floor_move_up+200))
    screen.blit(floor, (random_postion_3, floor_move_up+400))
    screen.blit(floor, (random_postion_4, floor_move_up+600))
    screen.blit(spine, (random_postion_5, floor_move_up+800))


def draw_ball():
    ball_rect = ball.get_rect(center=(random_postion_1+75, floor_move_up - 50))
    screen.blit(ball, ball_rect)


def control():
    for event in pygame.event.get():        
        #close game
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: 
            pygame.quit()
            sys.exit()
        #control ball
                
        


screen = pygame.display.set_mode((500, 800))
clock = pygame.time.Clock()
floor_move_up = 300
fps = 120
isPlaying = True
while isPlaying:
    control()
    screen.blit(background, (0, 0))  # Thêm hình ảnh vào màn hình
    floor_move_up -= 1
    draw_floor()
    draw_ball()
    pygame.display.update()
    clock.tick(fps)
