import pygame, random
pygame.init() 

#Display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Sprite Groups")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Define classes
class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Graphics/Blue_Monster.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.Velocity = random.randint(1, 5)

    def update(self):
        self.rect.y += self.Velocity
    
#Create a sprite group
monster_group = pygame.sprite.Group()
for i in range(10):
    monster = Monster(i*64, 10)
    monster_group.add(monster)

#Running game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        display_surface.fill((0, 0, 0))

        #Draw assets
        monster_group.update()
        monster_group.draw(display_surface)

        pygame.display.update()
        clock.tick(FPS)

pygame.quit