from typing import Any
import pygame
from pygame.sprite import AbstractGroup
pygame.init() 

#Display surface
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

WHITE = (255,255,255)

#Lines
rect1 = pygame.draw.rect(display_surface, WHITE,(50, 50 , 100, 100), 3)
rect2 = pygame.draw.rect(display_surface, WHITE,(150, 50 , 100, 100), 3)
rect3 = pygame.draw.rect(display_surface, WHITE,(250, 50 , 100, 100), 3)
rect4 = pygame.draw.rect(display_surface, WHITE,(50, 150 , 100, 100), 3)
rect5 = pygame.draw.rect(display_surface, WHITE,(50, 250 , 100, 100), 3)
rect6 = pygame.draw.rect(display_surface, WHITE,(150, 150 , 100, 100), 3)
rect7 = pygame.draw.rect(display_surface, WHITE,(150, 250 , 100, 100), 3)
rect8 = pygame.draw.rect(display_surface, WHITE,(250, 150 , 100, 100), 3)
rect9 = pygame.draw.rect(display_surface, WHITE,(250, 250 , 100, 100), 3)

cross_group = pygame.sprite.Group()

#Running game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            if rect1.collidepoint(mouse_x, mouse_y):
                pygame.draw.line(display_surface,WHITE, (50,50),(150,150),3)
                pygame.draw.line(display_surface,WHITE, (150,50),(50,150),3)
            if rect2.collidepoint(mouse_x, mouse_y):
                print("rect2")
            if rect3.collidepoint(mouse_x, mouse_y):
                print("rect3")
            if rect4.collidepoint(mouse_x, mouse_y):
                print("rect4")
            if rect5.collidepoint(mouse_x, mouse_y):
                print("rect5")
            if rect6.collidepoint(mouse_x, mouse_y):
                print("rect6")
            if rect7.collidepoint(mouse_x, mouse_y):
                print("rect7")
            if rect8.collidepoint(mouse_x, mouse_y):
                print("rect8")
            if rect9.collidepoint(mouse_x, mouse_y):
                print("rect9")
    
    cross_group.update()
    pygame.display.flip()

pygame.quit