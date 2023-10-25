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
RED = (255,0,0)
turn1 = True

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

#Figures
rect1f = None
rect2f = None
rect3f = None
rect4f = None
rect5f = None
rect6f = None
rect7f = None
rect8f = None
rect9f = None


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
              if turn1 and rect1f == None:
                pygame.draw.line(display_surface,RED, (50,50),(150,150),7)
                pygame.draw.line(display_surface,RED, (150,50),(50,150),7)
                rect1f = "Cross"
                turn1 = not turn1
              elif turn1 == False and rect1f == None:
                pygame.draw.circle(display_surface,RED,(100,100),47,7)
                turn1 = not turn1
                rect1f = "Circle"

            if rect2.collidepoint(mouse_x, mouse_y):
              if turn1 and rect2f == None:
                pygame.draw.line(display_surface,RED, (150,50),(250,150),7)
                pygame.draw.line(display_surface,RED, (150,150),(250,50),7)
                rect2f = "Cross"
                turn1 = not turn1
              elif turn1 == False and rect2f == None:
                pygame.draw.circle(display_surface,RED,(200,100),47,7)
                turn1 = not turn1
                rect2f = "Circle"

            if rect3.collidepoint(mouse_x, mouse_y):
              if turn1 and rect3f == None:
                pygame.draw.line(display_surface,RED, (250,50),(350,150),7)
                pygame.draw.line(display_surface,RED, (250,150),(350,50),7)
                rect3f = "Cross"
                turn1 = not turn1
              elif turn1 == False and rect3f == None:
                pygame.draw.circle(display_surface,RED,(300,100),47,7)
                turn1 = not turn1
                rect3f = "Circle"


            if rect4.collidepoint(mouse_x, mouse_y):
              if turn1 and rect4f == None:
                pygame.draw.line(display_surface,RED, (50,150),(150,250),7)
                pygame.draw.line(display_surface,RED, (150,150),(50,250),7)
                rect4f = "Cross"
                turn1 = not turn1
              elif turn1 == False and rect4f == None:
                pygame.draw.circle(display_surface,RED,(100,200),47,7)
                turn1 = not turn1
                rect4f = "Circle"


            if rect5.collidepoint(mouse_x, mouse_y):
              if turn1 and rect5f == None:
                pygame.draw.line(display_surface,RED, (50,250),(150,350),7)
                pygame.draw.line(display_surface,RED, (150,250),(50,350),7)
                rect5f = "Cross"
                turn1 = not turn1
              elif turn1 == False and rect5f == None:
                pygame.draw.circle(display_surface,RED,(100,300),47,7)
                turn1 = not turn1
                rect5f = "Circle"

            if rect6.collidepoint(mouse_x, mouse_y):
              if turn1 and rect6f == None:
                pygame.draw.line(display_surface,RED, (150,150),(250,250),7)
                pygame.draw.line(display_surface,RED, (250,150),(150,250),7)
                rect6f = "Cross"
                turn1 = not turn1
              elif turn1 == False and rect6f == None:
                pygame.draw.circle(display_surface,RED,(200,200),47,7)
                turn1 = not turn1
                rect6f = "Circle"

            if rect7.collidepoint(mouse_x, mouse_y):
              if turn1 and rect7f == None:
                pygame.draw.line(display_surface,RED, (150,250),(250,350),7)
                pygame.draw.line(display_surface,RED, (250,250),(150,350),7)
                rect7f = "Cross"
                turn1 = not turn1
              elif turn1 == False and rect7f == None:
                pygame.draw.circle(display_surface,RED,(200,300),47,7)
                turn1 = not turn1
                rect7f = "Circle"

            if rect8.collidepoint(mouse_x, mouse_y):
              if turn1 and rect8f == None:
                pygame.draw.line(display_surface,RED, (250,150),(350,250),7)
                pygame.draw.line(display_surface,RED, (350,150),(250,250),7)
                rect8f = "Cross"
                turn1 = not turn1
              elif turn1 == False and rect8f == None:
                pygame.draw.circle(display_surface,RED,(300,200),47,7)
                turn1 = not turn1
                rect8f = "Circle"

            if rect9.collidepoint(mouse_x, mouse_y):
              if turn1 and rect9f == None:
                pygame.draw.line(display_surface,RED, (250,250),(350,350),7)
                pygame.draw.line(display_surface,RED, (350,250),(250,350),7)
                rect9f = "Cross"
                turn1 = not turn1
              elif turn1 == False and rect9f == None:
                pygame.draw.circle(display_surface,RED,(300,300),47,7)
                turn1 = not turn1
                rect9f = "Circle"

            if rect1f == "Cross" and rect2f == "Cross" and rect3f == "Cross":
              print("Player1 Wins")
              pygame.display.flip()
              pygame.time.wait(1000)
              running = False
            elif rect4f == "Cross" and rect6f == "Cross" and rect8f == "Cross":
              print("Player1 Wins")
              pygame.display.flip()
              pygame.time.wait(1000)
              running = False
            elif rect5f == "Cross" and rect7f == "Cross" and rect9f == "Cross":
              print("Player1 Wins")
              pygame.display.flip()
              pygame.time.wait(1000)
              running = False
            elif rect1f == "Cross" and rect4f == "Cross" and rect5f == "Cross":
              print("Player1 Wins")
              pygame.display.flip()
              pygame.time.wait(1000)
              running = False
            elif rect2f == "Cross" and rect6f == "Cross" and rect7f == "Cross":
              print("Player1 Wins")
              pygame.display.flip()
              pygame.time.wait(1000)
              running = False
            elif rect3f == "Cross" and rect8f == "Cross" and rect9f == "Cross":
              print("Player1 Wins")
              pygame.display.flip()
              pygame.time.wait(1000)
              running = False
            elif rect1f == "Cross" and rect6f == "Cross" and rect9f == "Cross":
              print("Player1 Wins")
              pygame.display.flip()
              pygame.time.wait(1000)
              running = False
            elif rect3f == "Cross" and rect6f == "Cross" and rect5f == "Cross":
              print("Player1 Wins")
              pygame.display.flip()
              pygame.time.wait(1000)
              running = False

            if rect1f == "Circle" and rect2f == "Circle" and rect3f == "Circle":
              print("Player2 Wins")
              pygame.display.flip()
              pygame.time.wait(1000)
              running = False
            elif rect4f == "Circle" and rect6f == "Circle" and rect8f == "Circle":
              print("Player2 Wins")
              pygame.display.flip()
              pygame.time.wait(1000)
              running = False
            elif rect5f == "Circle" and rect7f == "Circle" and rect9f == "Circle":
              print("Player2 Wins")
              pygame.display.flip()
              pygame.time.wait(1000)
              running = False
            elif rect1f == "Circle" and rect4f == "Circle" and rect5f == "Circle":
              print("Player2 Wins")
              pygame.display.flip()
              pygame.time.wait(1000)
              running = False
            elif rect2f == "Circle" and rect6f == "Circle" and rect7f == "Circle":
              print("Player2 Wins")
              pygame.display.flip()
              pygame.time.wait(1000)
              running = False
            elif rect3f == "Circle" and rect8f == "Circle" and rect9f == "Circle":
              print("Player2 Wins")
              pygame.display.flip()
              pygame.time.wait(1000)
              running = False
            elif rect1f == "Circle" and rect6f == "Circle" and rect9f == "Circle":
              print("Player2 Wins")
              pygame.display.flip()
              pygame.time.wait(1000)
              running = False
            elif rect3f == "Circle" and rect6f == "Circle" and rect5f == "Circle":
              print("Player2 Wins")
              pygame.display.flip()
              pygame.time.wait(1000)
              running = False
    
    pygame.display.flip()

pygame.quit