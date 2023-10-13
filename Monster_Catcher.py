import pygame,random
pygame.init() 

#Display surface
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Monster Catcher")

#Set FPS and Clock
FPS = 60
clock = pygame.time.Clock()

#Define classes
class Game():
    def __init__(self, player, monster_group):
        self.score = 0
        self.round_number = 0

        self.round_time = 0
        self.frame_count = 0

        self.player = player
        self.monster_group = monster_group

        self.next_level_sound = pygame.mixer.Sound("Graphics/next_level.wav")

        self.font = pygame.font.Font("Graphics/Abrushow.ttf", 24)

        blue_image = pygame.image.load("Graphics/Blue_Monster.png")
        green_image = pygame.image.load("Graphics/Green_Monster.png")
        purple_image = pygame.image.load("Graphics/Purple_Monster.png")
        orange_image = pygame.image.load("Graphics/Orange_Monster.png")

        self.target_images = [blue_image, green_image, purple_image, orange_image]
        self.target_type = random.randint(0,3)
        self.target_image = self.target_images[self.target_type]

        self.target_rect = self.target_image.get_rect()
        self.target_rect.centerx = WINDOW_WIDTH//2
        self.target_rect.top = 30


    def update(self):
        self.frame_count += 1
        if self.frame_count == FPS:
            self.round_time += 1 
            self.frame_count = 0

        self.check_collisions()


    def draw(self):
        WHITE = (255,255,255)
        BLUE = (20,176,235)
        GREEN = (87,201,47)
        PURPLE = (226,73,243)
        ORANGE = (255,165,0)

        colors = [BLUE, GREEN, PURPLE, ORANGE]

        catch_text = self.font.render("Current Catch", True, WHITE)
        catch_rect = catch_text.get_rect()
        catch_rect.centerx = WINDOW_WIDTH//2
        catch_rect.top = 5

        score_text = self.font.render("Score: " + str(self.score), True, WHITE)
        score_rect = score_text.get_rect()
        score_rect.topleft = (5,5)

        lives_text = self.font.render("Lives: " + str(self.player.lives), True, WHITE)
        lives_rect = lives_text.get_rect()
        lives_rect.topleft = (5,35)

        round_text = self.font.render("Current Round:" + str(self.round_number), True, WHITE)
        round_rect = round_text.get_rect()
        round_rect.topleft = (5,65)

        time_text = self.font.render("Round Time: " + str(self.round_time), True, WHITE)
        time_rect = time_text.get_rect()
        time_rect.topright = (WINDOW_WIDTH - 10, 5)

        warp_text = self.font.render("Warps: " + str(self.player.warps), True, WHITE)
        warp_rect = warp_text.get_rect()
        warp_rect.topright = (WINDOW_WIDTH - 10, 35)

        display_surface.blit(catch_text, catch_rect)
        display_surface.blit(score_text, score_rect)
        display_surface.blit(round_text, round_rect)
        display_surface.blit(lives_text, lives_rect)
        display_surface.blit(warp_text, warp_rect)
        display_surface.blit(time_text, time_rect)
        display_surface.blit(self.target_image, self.target_rect)

        pygame.draw.rect(display_surface, colors[self.target_type], (WINDOW_WIDTH//2 - 32, 30, 64, 64), 2)
        pygame.draw.rect(display_surface, colors[self.target_type], (0, 100, WINDOW_WIDTH, WINDOW_HEIGHT-200), 4)

    def check_collisions(self):
        collided_monster = pygame.sprite.spritecollideany(self.player, self.monster_group)

        if collided_monster:
            if collided_monster.type == self.target_type:
                self.score += 100*self.round_number
                collided_monster.remove(self.monster_group)
                if (self.monster_group):
                    self.player.catch_sound.play()
                    self.new_target()
                else:
                    self.player.reset()
                    self.start_new_round()
        
            else:
                self.player.die_sound.play()
                self.player.lives -= 1
                self.player.reset()

                if self.player.lives <= 0:
                   self.pause("Final Score: " + str(self.score), "Press 'Enter' to play again")
                   self.reset()
                   self.player.reset()

    def start_new_round(self):
        self.score += int(10000*self.round_number/(1 + self.round_time))

        self.round_time = 0
        self.frame_count = 0
        self.round_number += 1
        self.player.warps += 1

        for monster in self.monster_group:
            self.monster_group.remove(monster)
        
        for i in range (self.round_number):
            self.monster_group.add(Monster(random.randint(0,WINDOW_WIDTH - 64 ), random.randint(100, WINDOW_HEIGHT - 164), self.target_images[0], 0))
            self.monster_group.add(Monster(random.randint(0,WINDOW_WIDTH - 64 ), random.randint(100, WINDOW_HEIGHT - 164), self.target_images[1], 1))
            self.monster_group.add(Monster(random.randint(0,WINDOW_WIDTH - 64 ), random.randint(100, WINDOW_HEIGHT - 164), self.target_images[2], 2))
            self.monster_group.add(Monster(random.randint(0,WINDOW_WIDTH - 64 ), random.randint(100, WINDOW_HEIGHT - 164), self.target_images[3], 3))

        self.new_target()

        self.next_level_sound.play()

    def new_target(self):
        global running

        target_monster = random.choice(self.monster_group.sprites())
        self.target_type = target_monster.type
        self.target_image = target_monster.image

    def pause(self, main_text, sub_text):
        WHITE = (255,255,255)
        main_text = self.font.render(main_text, True, WHITE)
        main_rect = main_text.get_rect()
        main_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT//2)

        sub_text = self.font.render(sub_text, True, WHITE)
        sub_rect = sub_text.get_rect()
        sub_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)

        display_surface.fill((0,0,0))
        display_surface.blit(main_text, main_rect)
        display_surface.blit(sub_text, sub_rect)
        pygame.display.update()

        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        is_paused = False
                        self.player.lives = 5
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    def reset(self):
        self.score = 0
        self.round_number = 0

        self.player.lives = 5
        self.player.warps = 2
        self.player.reset()

        self.start_new_round()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Graphics/Knight.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH//2
        self.rect.bottom = WINDOW_HEIGHT

        self.lives = 5
        self.warps = 2
        self.velocity = 8

        self.catch_sound = pygame.mixer.Sound("Graphics/catch.wav")
        self.die_sound = pygame.mixer.Sound("Graphics/die.wav")
        self.warp_sound = pygame.mixer.Sound("Graphics/warp.wav")

    def update(self):
        keys = pygame.key.get_pressed()

        if keys [pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys [pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.velocity
        if keys [pygame.K_UP] and self.rect.top > 100:
            self.rect.y -= self.velocity
        if keys [pygame.K_DOWN] and self.rect.bottom < WINDOW_HEIGHT - 100:
            self.rect.y += self.velocity

    def warp(self):
        if self.warps > 0:
            self.warps -= 1
            self.warp_sound.play()
            self.rect.bottom = WINDOW_HEIGHT

    def reset(self):
        self.rect.centerx = WINDOW_WIDTH//2
        self.rect.bottom = WINDOW_HEIGHT

class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, image, monster_type):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # 0 blue 1 green 2 purple 3 orange
        self.type = monster_type

        #Random motion
        self.dx = random.choice([-1,1])
        self.dy = random.choice([-1,1])
        self.velocity = random.randint(1, 5)

    def update(self):
        self.rect.x += self.dx*self.velocity
        self.rect.y += self.dy*self.velocity

        #Bounce the monsters
        if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
            self.dx = -1*self.dx
        if self.rect.top <= 100 or self.rect.bottom >= WINDOW_HEIGHT - 100:
            self.dy = -1*self.dy

#Create a player group
my_player_group = pygame.sprite.Group()
my_player = Player()
my_player_group.add(my_player)

#Create a monster group
my_monster_group = pygame.sprite.Group()

#Create a game object
my_game = Game(my_player, my_monster_group)
my_game.pause("Monster Wrangler", "Press 'Enter' to begin")
my_game.start_new_round()

#Running game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                my_player.warp()
    
    display_surface.fill((0,0,0))

    my_player_group.update()
    my_player_group.draw(display_surface)

    my_monster_group.update()
    my_monster_group.draw(display_surface)

    my_game.update()
    my_game.draw()




    pygame.display.update()
    clock.tick(FPS)

pygame.quit