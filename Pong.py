import pygame, random
pygame.init() 

#Display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300

display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Pong")

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#FPS AND CLOCK
FPS = 60
clock = pygame.time.Clock()

#Points
Points1 = 0
Points2 = 0

#Define fonts
system_font = pygame.font.SysFont("calibri", 30)

#Define text
system_text = system_font.render(str(Points1), True, WHITE)
system_text_rect = system_text.get_rect()
system_text_rect.center = (20,20)

custom_text = system_font.render(str(Points2), True, WHITE)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (580,20)

#Positions
y1 = 30
y2 = 30
xb = 300
yb = 150
velocity_x = -2
velocity_y = 0

#Running game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #Keys list
    keys = pygame.key.get_pressed()

    #Contiuous movement
    if (keys[pygame.K_DOWN]):
        y2 += 3
    if (keys[pygame.K_UP]):
        y2 -= 3
    if ( keys[pygame.K_w]):
        y1 -= 3
    if ( keys [pygame.K_s]):
        y1 += 3
    
    #Ball movement
    xb += velocity_x
    yb += velocity_y
    

    display_surface.fill(BLACK)
    pygame.draw.line(display_surface, WHITE, (30,y1), (30, y1 + 80), 5)
    pygame.draw.line(display_surface, WHITE, (570,y2), (570, y2 + 80), 5)
    pygame.draw.circle(display_surface,(255,255,255),(xb,yb),5)


    #Collisions
    if (xb == 566 and y2 <= yb <= y2+80):
        velocity_x = -2
        velocity_y = random.randint(-4,4)
 
    if (xb == 34 and y1 <= yb <= y1+80):
        velocity_x = 2
        velocity_y = random.randint(-4,4)

    if (yb < 0):
        velocity_y = velocity_y*-1
    if (yb > WINDOW_HEIGHT):
        velocity_y = velocity_y*-1
    if (xb < 5):
        xb = 300
        yb = 150
        velocity_y = 0
        velocity_x = -2
        Points2 += 1
    if (xb > WINDOW_WIDTH - 10):
        xb = 300
        yb = 150
        velocity_y = 0
        velocity_x = 2
        Points1 += 1
      
    system_text = system_font.render(str(Points1), True, WHITE)
    custom_text = system_font.render(str(Points2), True, WHITE)
    display_surface.blit(system_text, system_text_rect)
    display_surface.blit(custom_text, custom_text_rect)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit