import pygame
pygame.init() 

#Display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Test")

CYAN = (0, 255, 255)
MAGENTA = (255,0 , 255)
BLUE = (0,0,255)

#Games values
VELOCITY = 5
MOVEMENT1 = True
MOVEMENT2 = False

#FPS AND CLOCK
FPS = 60
clock = pygame.time.Clock()

#Positions
Cube1X = 250
Cube2X = 400
Cube1Y = 250
Cube2Y = 250

#Rectangle(surface, color,(top-left x, top-left y, width, height))
Cube1 = pygame.draw.rect(display_surface, CYAN, (Cube1X, Cube1Y , 50, 50))
dragon_image = pygame.image.load("Graphics/dragon_left.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.topleft = (Cube2X, Cube2Y)


#Running game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Keys list
    keys = pygame.key.get_pressed()

    #Mouse click
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x = event.pos[0]
        mouse_y = event.pos[1]
        if dragon_rect.collidepoint(mouse_x,mouse_y):
            MOVEMENT1 = False
            MOVEMENT2 = True
        if Cube1.collidepoint(mouse_x,mouse_y):
            MOVEMENT1 = True
            MOVEMENT2 = False

    #Contiuous movement
    if MOVEMENT1 == True:  
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and Cube1X > 0:
            Cube1X -= VELOCITY
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and Cube1X < WINDOW_WIDTH:
            Cube1X += VELOCITY
        if (keys[pygame.K_UP] or keys [pygame.K_w])and Cube1Y > 0:
            Cube1Y -= VELOCITY
        if (keys[pygame.K_DOWN] or keys [pygame.K_s]) and Cube1Y < WINDOW_HEIGHT:
            Cube1Y += VELOCITY
    elif MOVEMENT2 == True:
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and Cube2X > 0:
            Cube2X -= VELOCITY
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and Cube2X < WINDOW_WIDTH:
            Cube2X += VELOCITY
        if (keys[pygame.K_UP] or keys [pygame.K_w])and Cube2Y > 0:
            Cube2Y -= VELOCITY
        if (keys[pygame.K_DOWN] or keys [pygame.K_s]) and Cube2Y < WINDOW_HEIGHT:
            Cube2Y += VELOCITY

    #Fill the display
    display_surface.fill(BLUE)
    Cube1 = pygame.draw.rect(display_surface, CYAN, (Cube1X, Cube1Y , 50, 50))
    pygame.image.load("Graphics/dragon_left.png")
    dragon_rect.topleft = (Cube2X, Cube2Y)
    #Update the display
    display_surface.blit(dragon_image, dragon_rect)
    pygame.display.flip()

    #Tick the clock
    clock.tick(FPS)

pygame.quit