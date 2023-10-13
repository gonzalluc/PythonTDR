import pygame, random
pygame.init() 

#Display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Snake")

#Set FPS and clock
FPS = 20
clock = pygame.time.Clock()

#Set Game Values
snake_size = 20
head_x = WINDOW_WIDTH//2
head_y = WINDOW_HEIGHT//2 + 100

snake_dx = 0
snake_dy = 0

score = 0

#Set colors
GREEN = (0,255,0)
RED=(255,0,0)
WHITE = (255, 255, 255)
DARKGREEN = (10,50,10)
DARKRED = (150,0,0)

#Set fonts
font = pygame.font.SysFont("Gabriola", 48)

#Set text
title_text = font.render("Snake", True, GREEN, DARKRED)
title_rect = title_text.get_rect()
title_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

score_text = font.render("Score:" + str(score), True, GREEN, DARKRED)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

game_over_text = font.render("GAMEOVER", True, RED, DARKGREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render("Press any key to play again", True, RED, DARKGREEN)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT + 64)

#Set sounds
pick_up_sound = pygame.mixer.Sound("Graphics/Sound2.wav")

#Set images(simple rects) (x, y, width, height)
apple_coord = (500, 500, snake_size, snake_size)
head_coord = (head_x, head_y, snake_size, snake_size)
body_coords = []

apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)
head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)

#Running game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Move the snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -1*snake_size
                snake_dy = 0
            if event.key == pygame.K_RIGHT:
                snake_dx = snake_size
                snake_dy = 0
            if event.key == pygame.K_UP:
                snake_dx = 0
                snake_dy = -1*snake_size
            if event.key == pygame.K_DOWN:
                snake_dx = 0
                snake_dy = snake_size
    display_surface.fill(WHITE)

    #Update the x,y position of the snakes head and make a new coordinates
    head_x += snake_dx
    head_y += snake_dy
    head_coord = (head_x, head_y, snake_size, snake_size)

    #Check for game over
    if head_rect.left < 0 or head_rect.right > WINDOW_WIDTH or head_rect.top < 0 or head_rect.bottom > WINDOW_HEIGHT or head_coord in body_coords:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()

        #Game paused
        Paused = True
        while Paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    head_x = WINDOW_WIDTH//2
                    head_y = WINDOW_HEIGHT//2 + 100
                    head_coord = (head_x, head_y, snake_size, snake_size)
                    body_coords = []
                    snake_dx = 0
                    snake_dy = 0
                    Paused = False
                if event.type == pygame.QUIT:
                    Paused = False
                    running = False

    #Check for collisions
    if head_rect.colliderect(apple_rect):
        score += 1
        pick_up_sound.play()

        apple_x = random.randint(0, WINDOW_WIDTH - snake_size)
        apple_y = random.randint(0, WINDOW_HEIGHT - snake_size)
        apple_coord = (apple_x, apple_y, snake_size, snake_size)

        body_coords.append(head_coord)

    #Blit HUD
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_rect)

    #Body movement
    body_coords.insert(0, head_coord)
    body_coords.pop()

    #Update HUD
    score_text = font.render("Score:" + str(score), True, GREEN, DARKRED)

    #Blit assets
    for body in body_coords:
        pygame.draw.rect(display_surface, DARKGREEN, body)
    head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)
    apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)

    #Update display and tick clock
    pygame.display.update()
    clock.tick(FPS)
pygame.quit