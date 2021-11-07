import pygame
from pygame import color, init
from pygame.constants import K_LEFT

left = False
right = False
a = False
d = False

class Vector2:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

pygame.init()

screen = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Epic Pixel Art Game from ME")

run = True

main = Vector2(250,250)
center_bottom_left_vec = Vector2(50,260)
center_top_left_vec = Vector2(50,240)
center_bottom_right_vec = Vector2(450,260)
center_top_right_vec = Vector2(450,240)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            left = True
            #main.x -= 1
            #main.y -= 1
        
        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            left = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            right = True
            #main.x -= 1
            #main.y -= 1
        
        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            right = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            a = True
            #main.x -= 1
            #main.y -= 1
        
        if event.type == pygame.KEYUP and event.key == pygame.K_a:
            a = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            d = True
            #main.x -= 1
            #main.y -= 1
        
        if event.type == pygame.KEYUP and event.key == pygame.K_d:
            d = False


    if left:
        main.x -= 0.1
        main.y -= 0.1
        center_bottom_left_vec.y -= 0.1
        center_top_left_vec.y -= 0.1
        center_bottom_right_vec.y -= 0.1
        center_top_right_vec.y -= 0.1

    if right:
        main.x += 0.1
        main.y += 0.1
        center_bottom_left_vec.y += 0.1
        center_top_left_vec.y += 0.1
        center_bottom_right_vec.y += 0.1
        center_top_right_vec.y += 0.1

    if a:
        main.x -= 0.1
        main.y += 0.1
        center_bottom_left_vec.y += 0.1
        center_top_left_vec.y += 0.1
        center_bottom_right_vec.y += 0.1
        center_top_right_vec.y += 0.1

    if d:
        main.x += 0.1
        main.y -= 0.1
        center_bottom_left_vec.y -= 0.1
        center_top_left_vec.y -= 0.1
        center_bottom_right_vec.y -= 0.1
        center_top_right_vec.y -= 0.1

    screen.fill((0,0,0))

    squ = pygame.draw.rect(screen, (255,0,0), (main.x-2.5,main.y-10,5,20))
    top_left = pygame.draw.rect(screen, (255,255,255), (50,50,5,5))
    top_right = pygame.draw.rect(screen, (255,255,255), (450,50,5,5))
    bottom_left = pygame.draw.rect(screen, (255,255,255), (50,450,5,5))
    bottom_right = pygame.draw.rect(screen, (255,255,255), (450,450,5,5))

    top_right_to_bottom_left = pygame.draw.line(screen, (0,0,255), (450, 50), (50, 450), 1)
    top_left_to_bottom_right = pygame.draw.line(screen, (0,255,0), (50,50), (450,450), 1)

    

    center_bottom_left = pygame.draw.rect(screen, (255,255,255), ((center_bottom_left_vec.x,center_bottom_left_vec.y,5,5)))

    

    center_top_left = pygame.draw.rect(screen, (255,255,255), ((center_top_left_vec.x,center_top_left_vec.y,5,5)))

    

    center_bottom_right = pygame.draw.rect(screen, (255,255,255), ((center_bottom_right_vec.x,center_bottom_right_vec.y,5,5)))

    

    center_top_right = pygame.draw.rect(screen, (255,255,255), ((center_top_right_vec.x,center_top_right_vec.y,5,5)))

    bottom_left_center_to_bottom_left = pygame.draw.line(screen, (0,0,255), (center_bottom_left_vec.x, center_bottom_left_vec.y), (50,450), 1)
    bottom_right_center_to_bottom_right = pygame.draw.line(screen, (0,255,0), (center_bottom_right_vec.x, center_bottom_right_vec.y), (450,450), 1)

    left_top_to_left_center = pygame.draw.line(screen, (0,255,0), (50,50), (center_top_left_vec.x,center_top_left_vec.y), 1)
    right_top_to_right_center = pygame.draw.line(screen, (0,0,255), (450,50), (center_top_right_vec.x,center_top_right_vec.y), 1)

    center_bottom_left_to_center = pygame.draw.line(screen, (0,0,255), (center_bottom_left_vec.x, center_bottom_left_vec.y), (main.x, center_bottom_left_vec.y), 1)
    center_bottom_right_to_center = pygame.draw.line(screen, (0,255,0), (center_bottom_right_vec.x, center_bottom_right_vec.y), (main.x, center_bottom_right.y), 1)
    center_top_left_to_center = pygame.draw.line(screen, (0,255,0), (center_top_left_vec.x, center_top_left_vec.y), (main.x, center_top_left_vec.y), 1)
    center_top_right_to_center = pygame.draw.line(screen)

    pygame.display.update()