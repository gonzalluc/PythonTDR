import pygame, random
pygame.init() 

#Display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Group Collisions")

#FPS and Clock
FPS = 60
clock = pygame.time.Clock()

#Define classes
class Game():
    def __init__(self, monster_group, knight_group):
        self.monster_group = monster_group
        self.knight_group = knight_group

    def update(self):
        self.check_collisions()

    def check_collisions(self):
        pygame.sprite.groupcollide(self.monster_group, self.knight_group, True, False)

class Knight(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Graphics/Knight.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.Velocity = random.randint(1, 5)

    def update(self):
        self.rect.y -= self.Velocity

class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Graphics/Blue_Monster.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.Velocity = random.randint(1, 5)

    def update(self):
        self.rect.y += self.Velocity
    
#Create groups
my_monster_group = pygame.sprite.Group()
for i in range(12):
    monster = Monster(i*64, 10)
    my_monster_group.add(monster)

my_knight_group = pygame.sprite.Group()
for i in range(12):
    knight = Knight(i*64, 500)
    my_knight_group.add(knight)

#Create a game object
my_game = Game(my_monster_group, my_knight_group)

#Running game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill((0,0,0))

    my_monster_group.update()
    my_monster_group.draw(display_surface)

    my_knight_group.update()
    my_knight_group.draw(display_surface)

    my_game.update()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit