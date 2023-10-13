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
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, monster_group):
        super().__init__()
        self.image = pygame.image.load("Graphics/Knight.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.Velocity = 10
        self.monster_group = monster_group

    def update(self):
        self.move()
        self.collisions()

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.Velocity
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.Velocity
        if keys[pygame.K_UP]:
            self.rect.y -= self.Velocity
        if keys[pygame.K_DOWN]:
            self.rect.y += self.Velocity

    def collisions(self):
        if pygame.sprite.spritecollide(self, self.monster_group, True):
            print(len(self.monster_group))
        
class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Graphics/Blue_Monster.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.Velocity = random.randint(1, 5)

    def update(self):
        self.rect.y += self.Velocity

#Create a monster group
my_monster_group = pygame.sprite.Group()
for i in range(10):
    monster = Monster(i*64, 10)
    my_monster_group.add(monster)

#Create a player group
player_group = pygame.sprite.Group()
player = Player(500, 500, my_monster_group)
player_group.add(player)

#Running game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    display_surface.fill((0, 0, 0))

    #Draw assets
    player_group.update()
    player_group.draw(display_surface)

    my_monster_group.update()
    my_monster_group.draw(display_surface)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit