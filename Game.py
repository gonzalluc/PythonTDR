import pygame
from pygame.sprite import AbstractGroup
pygame.init() 

#2D vectors (prova)
vector = pygame.math.Vector2

#Display surface
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 480
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Beta 1")

#FPS AND CLOCK
FPS = 60
clock = pygame.time.Clock()

looking_left = True
launching_attack = False

#Clases

class Game():
    def __init__(self):
        pass

class Tile(pygame.sprite.Sprite):
    """A class to read and create individual tiles and place them in the display"""

    def __init__(self, x, y, image_int, main_group, sub_group=""):
        super().__init__()
        #Load in the correct image and add it to the correct sub groups
        if image_int == 1:
            self.image = pygame.image.load("Graphics/Knight_Game/Enviroment1/Tiles/Ground.png")
        elif image_int == 2:
            self.image = pygame.image.load("Graphics/Knight_Game/Enviroment1/Tiles/Ground_Left.png")
            self.mask = pygame.mask.from_surface(self.image)
            sub_group.add(self)
        elif image_int == 3:
            self.image = pygame.image.load("Graphics/Knight_Game/Enviroment1/Tiles/Ground_Right.png")
            sub_group.add(self)
        elif image_int == 4:
            self.image = pygame.image.load("Graphics/Knight_Game/Enviroment1/Tiles/LowGround_Left.png")
        elif image_int == 5:
            self.image = pygame.image.load("Graphics/Knight_Game/Enviroment1/Tiles/LowGround_Right.png")
        elif image_int == 6:
            self.image = pygame.image.load("Graphics/Knight_Game/Enviroment1/Tiles/LowGround.png")
        
        #Add every tile to the main tile group
        main_group.add(self)

        #Get the rect of the image and position within the grid
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        pygame.draw.rect(display_surface,(0,0,255), self.rect, 1)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, ground_tiles):
        super().__init__()

        #Animation Frames
        self.move_right_sprites = []
        self.move_left_sprites = []
        self.idle_right_sprites = []
        self.idle_left_sprites = []
        self.attack_right_sprites = []
        self.attack_left_sprites = []
        self.death_right_sprites = []
        self.death_left_sprites = []
        self.fall_right_sprites = []
        self.fall_left_sprites = []
        self.hit_right_sprites = []
        self.hit_left_sprites = []
        self.jump_right_sprites = []
        self.jump_left_sprites = []
        self.fall_right_sprites = []
        self.fall_left_sprites = []
        self.roll_right_sprites = []
        self.roll_left_sprites = []

        #Idle right
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Idle/1.png"), (120,80)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Idle/2.png"), (120,80)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Idle/3.png"), (120,80)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Idle/4.png"), (120,80)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Idle/5.png"), (120,80)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Idle/6.png"), (120,80)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Idle/7.png"), (120,80)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Idle/8.png"), (120,80)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Idle/9.png"), (120,80)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Idle/10.png"),(120,80)))

        #Idle left
        for sprite in self.idle_right_sprites:
            self.idle_left_sprites.append(pygame.transform.flip(sprite, True, False))
        
        #Move right
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Run/1.png"), (120,80)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Run/2.png"), (120,80)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Run/3.png"), (120,80)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Run/4.png"), (120,80)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Run/5.png"), (120,80)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Run/6.png"), (120,80)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Run/7.png"), (120,80)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Run/8.png"), (120,80)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Run/9.png"), (120,80)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Run/10.png"),(120,80)))

        #Move left
        for sprite in self.move_right_sprites:
            self.move_left_sprites.append(pygame.transform.flip(sprite, True, False))

        #Attack right
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Attack/1.png"), (120,80)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Attack/2.png"), (120,80)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Attack/3.png"), (120,80)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Attack/4.png"), (120,80)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Attack/5.png"), (120,80)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Attack/6.png"), (120,80)))
        
        #Attack left
        for sprite in self.attack_right_sprites:
            self.attack_left_sprites.append(pygame.transform.flip(sprite, True, False))
        
        #Death right
        self.death_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Death/1.png"), (120,80)))
        self.death_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Death/2.png"), (120,80)))
        self.death_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Death/3.png"), (120,80)))
        self.death_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Death/4.png"), (120,80)))
        self.death_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Death/5.png"), (120,80)))
        self.death_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Death/6.png"), (120,80)))
        self.death_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Death/7.png"), (120,80)))
        self.death_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Death/8.png"), (120,80)))
        self.death_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Death/9.png"), (120,80)))
        self.death_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Death/10.png"), (120,80)))

        #Death left
        for sprite in self.death_right_sprites:
            self.death_left_sprites.append(pygame.transform.flip(sprite,True,False))

        #Fall right
        self.fall_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Fall/1.png"), (120,80)))
        self.fall_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Fall/2.png"), (120,80)))
        self.fall_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Fall/3.png"), (120,80)))

        #Fall left
        for sprite in self.fall_right_sprites:
            self.fall_left_sprites.append(pygame.transform.flip(sprite,True,False))

        #Hit right
        self.hit_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Hit/1.png"), (120,80)))
        self.hit_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Hit/2.png"), (120,80)))
        
        #Fall left
        for sprite in self.hit_right_sprites:
            self.hit_left_sprites.append(pygame.transform.flip(sprite,True,False))

        #Jump right
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Jump/1.png"), (120,80)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Jump/2.png"), (120,80)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Jump/3.png"), (120,80)))
        
        #Jump left
        for sprite in self.jump_right_sprites:
            self.jump_left_sprites.append(pygame.transform.flip(sprite,True,False))

        #Roll right
        self.roll_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Roll/1.png"), (120,80)))
        self.roll_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Roll/2.png"), (120,80)))
        self.roll_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Roll/3.png"), (120,80)))
        self.roll_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Roll/4.png"), (120,80)))
        self.roll_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Roll/5.png"), (120,80)))
        self.roll_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Roll/6.png"), (120,80)))
        self.roll_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Roll/7.png"), (120,80)))
        self.roll_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Roll/8.png"), (120,80)))
        self.roll_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Roll/9.png"), (120,80)))
        self.roll_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Roll/10.png"), (120,80)))
        self.roll_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Roll/11.png"), (120,80)))
        self.roll_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Knight/Animations/Roll/12.png"), (120,80)))

        #Roll left
        for sprite in self.roll_right_sprites:
            self.roll_left_sprites.append(pygame.transform.flip(sprite,True,False))
        
        #Player values
        self.current_sprite = 0
        self.image = self.move_right_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect_bottomleft = (x,y)
        
        self.starting_x = x
        self.starting_y = y

        self.ground_tiles = ground_tiles

        self.position = vector(x, y)
        self.velocity = vector(0, 0)
        self.acceleration = vector(0, 0)

        self.HORITZONTAL_ACCELERATION = 0.7
        self.HORITZONTAL_FRICTION = 0.17
        self.VERTICAL_ACCELERATION = 0.5
        self.VERTICAL_JUMP_SPEED = 12


        self.attacking = False
        self.rolling = False
        self.gothit = False

    def update(self):

        #Create a mask
        self.mask = pygame.mask.from_surface(self.image)

        #Draw the mask
        mask_outline = self.mask.outline()
        pygame.draw.lines(self.image,(255,255,0), True, mask_outline)


        #self.animate_attack()

        self.move()
        self.hit()
        self.collisions()
        self.check_velocity()
        self.check_animations()
 

    def animate(self, sprite_list, speed):
        if self.current_sprite < len(sprite_list) - 1:
            self.current_sprite += speed
            if self.rolling:
                if looking_left == True:
                   self.velocity.x = -4
                else:
                    self.velocity.x = 4
            if self.gothit:
                if looking_left == True:
                   self.velocity.x = 10
                else:
                    self.velocity.x = -10

        else:
            self.current_sprite = 0
            if self.attacking:
                self.attacking = False
                global launching_attack
                launching_attack = False
            if self.rolling:
                self.rolling = False
            if self.gothit:
                self.gothit = False

        self.image = sprite_list[int(self.current_sprite)]

    def move(self):
        self.acceleration = vector(0, self.VERTICAL_ACCELERATION)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acceleration.x = -1*self.HORITZONTAL_ACCELERATION
            self.animate(self.move_left_sprites, 0.2)
            global looking_left 
            looking_left = True

        elif keys[pygame.K_RIGHT]:
            self.acceleration.x = self.HORITZONTAL_ACCELERATION
            self.animate(self.move_right_sprites, 0.2)
            looking_left = False

        else:
          if self.rolling == False and self.attacking == False and self.gothit == False:
            if self.velocity.x > 0:
               self.animate(self.idle_right_sprites, 0.1)
            elif self.velocity.x < 0:
                self.animate(self.idle_left_sprites, 0.1)

        self.acceleration.x -= self.velocity.x*self.HORITZONTAL_FRICTION
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5*self.acceleration
        
        if self.position.x < -72:
            self.position.x = WINDOW_WIDTH - 70
        elif self.position.x > WINDOW_WIDTH - 70:
            self.position.x = -60
        if self.position.y > 540:
            self.position.y = -20
        self.rect.bottomleft = self.position
    

    def collisions(self):
        collided_platforms = pygame.sprite.spritecollide(self, ground_tile_group, False, pygame.sprite.collide_mask)
        if collided_platforms:
            if self.velocity.y > 0:
                self.position.y = collided_platforms[0].rect.top + 2
                self.velocity.y = 0

        else:
            if self.rolling == False:
                if looking_left == True:
                   self.animate(self.fall_left_sprites, 0.2)
                if looking_left == False:
                   self.animate(self.fall_right_sprites, 0.2)


    def jump(self):
        if pygame.sprite.spritecollide(self, ground_tile_group, False): 
            self.velocity.y = -1*self.VERTICAL_JUMP_SPEED
    
    def attack(self):
        self.attacking = True
        self.current_sprite = 0
        global launching_attack
        launching_attack = True
    
    def roll(self):
        self.rolling = True
        self.current_sprite = 0
    
    def hit(self):
        collided_sprites = pygame.sprite.spritecollide(self, enemies_group, False, pygame.sprite.collide_mask)
        if collided_sprites:
            if launching_attack == False:
                self.gothit = True

                
 
    def check_animations(self):
        if self.attacking == True:
            if looking_left == True:
                self.animate(self.attack_left_sprites, 0.2)

            if looking_left == False:
                self.animate(self.attack_right_sprites, 0.2)
        
        if self.rolling == True:
            if looking_left == True:
                self.animate(self.roll_left_sprites, 0.3)

            if looking_left == False:
                self.animate(self.roll_right_sprites, 0.3)
        
        if self.gothit == True:
            if looking_left == True:
                self.animate(self.hit_left_sprites, 0.2)

            if looking_left == False:
                self.animate(self.hit_right_sprites, 0.2)
        
        
    def check_velocity(self):
        if self.velocity.y < 0:
            if looking_left == True:
                self.animate(self.jump_left_sprites, 0.2)

            else:
                self.animate(self.jump_right_sprites, 0.2)
              

class Eye(pygame.sprite.Sprite):
    def __init__(self, x, y, ground_tiles):
        super().__init__()

        #Animation frames
        self.run_right_sprites = []
        self.run_left_sprites = []
        self.gethit_right_sprites = []
        self.gethit_left_sprites = []
        
        #Run right
        self.run_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Eye/Flight/00.png"), (150,150)))
        self.run_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Eye/Flight/10.png"), (150,150)))
        self.run_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Eye/Flight/20.png"), (150,150)))
        self.run_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Eye/Flight/30.png"), (150,150)))
        self.run_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Eye/Flight/40.png"), (150,150)))
        self.run_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Eye/Flight/50.png"), (150,150)))
        self.run_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Eye/Flight/60.png"), (150,150)))
        self.run_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Eye/Flight/70.png"), (150,150)))

        #Run left
        for sprite in self.run_right_sprites:
            self.run_left_sprites.append(pygame.transform.flip(sprite, True, False))
        
        #Get hit right
        self.gethit_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Eye/Hit/00.png"), (150,150)))
        self.gethit_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Eye/Hit/10.png"), (150,150)))
        self.gethit_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Eye/Hit/20.png"), (150,150)))
        self.gethit_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Eye/Hit/30.png"), (150,150)))
        
        #Get hit left
        for sprite in self.gethit_right_sprites:
            self.gethit_left_sprites.append(pygame.transform.flip(sprite, True, False))
        
        #Monster values
        self.current_sprite = 0
        self.image = self.run_right_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect_midtop = (x,y)
        self.starting_x = x
        self.starting_y = y
        self.ground_tiles = ground_tiles
        self.position = vector(x, y)
        self.velocity = vector(0, 0)
        self.gothit = False
        self.lifes = 2
        self.dead = False
        self.attacking = False

    def update(self):
        #Create a mask
        self.mask = pygame.mask.from_surface(self.image)

        #Draw the mask
        mask_outline = self.mask.outline()
        pygame.draw.lines(self.image,(0,0,255), True, mask_outline)

        self.run()
        self.hit()
        self.check_lives()
        self.check_animations()
    
    def animate(self, sprite_list, speed):
        if self.current_sprite < len(sprite_list) - 1:
            self.current_sprite += speed
            if self.gothit or self.dead:
                if looking_left:
                   self.velocity.x = -4
                   self.velocity.y = -2
                elif looking_left == False:
                    self.velocity.x = 4
                    self.velocity.y = 2



        else:
            self.current_sprite = 0
            if self.gothit:
                self.gothit = False
            if self.dead:
                self.kill()
                self.dead = False

        self.image = sprite_list[int(self.current_sprite)]
    
    def run(self):
        if self.gothit == False and self.dead == False and self.attacking == False:
           if my_player.position.x  > self.position.x + 2:
               self.velocity.x = 1
           if my_player.position.x < self.position.x - 2:
               self.velocity.x = -1 
           if self.velocity.x < 0:
               self.animate(self.run_left_sprites, 0.2)
           else:
               self.animate(self.run_right_sprites, 0.2)
           if my_player.position.y > self.position.y + 35:
               self.velocity.y = 1
           if my_player.position.y < self.position.y - 30:
               self.velocity.y = -1 
        self.position += self.velocity 
        
        if self.position.x < -72:
            self.position.x = WINDOW_WIDTH - 70
        elif self.position.x > WINDOW_WIDTH - 70:
            self.position.x = -60
        elif self.position.y > WINDOW_HEIGHT + 48:
            self.position.y = 0
        self.rect.bottomleft = self.position
    
    def hit(self):
        collided_sprites = pygame.sprite.spritecollide(self, my_player_group, False, pygame.sprite.collide_mask)
        if collided_sprites:
            if launching_attack == True:
               self.gothit = True
               self.current_sprite = 0
               self.lifes -= 0.1
    
    def check_lives(self):
        if self.lifes <= 0:
            self.dead = True

    def check_animations(self):
        if self.gothit:
            self.animate(self.gethit_right_sprites, 0.1)   
    

class Goblin(pygame.sprite.Sprite):
    def __init__(self, x, y, ground_tiles):
        super().__init__()

        #Animation frames
        self.run_right_sprites = []
        self.run_left_sprites = []
        self.gethit_right_sprites = []
        self.gethit_left_sprites = []
        self.death_right_sprites = []
        self.death_left_sprites = []

        #Run right
        self.run_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Goblin/Run/00.png"), (120,80)))
        self.run_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Goblin/Run/10.png"), (120,80)))
        self.run_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Goblin/Run/20.png"), (120,80)))
        self.run_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Goblin/Run/30.png"), (120,80)))
        self.run_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Goblin/Run/40.png"), (120,80)))
        self.run_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Goblin/Run/50.png"), (120,80)))
        self.run_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Goblin/Run/60.png"), (120,80)))
        self.run_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Goblin/Run/70.png"), (120,80)))

        #Run left
        for sprite in self.run_right_sprites:
            self.run_left_sprites.append(pygame.transform.flip(sprite, True, False))

        #Get hit right
        self.gethit_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Goblin/Hit/00.png"), (120,80)))
        self.gethit_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Goblin/Hit/10.png"), (120,80)))
        self.gethit_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Goblin/Hit/20.png"), (120,80)))
        self.gethit_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Goblin/Hit/30.png"), (120,80)))
        
        #Get hit left
        for sprite in self.gethit_right_sprites:
            self.gethit_left_sprites.append(pygame.transform.flip(sprite, True, False))

        #Die right
        self.death_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Goblin/Death/00.png"), (120,80)))
        self.death_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Goblin/Death/10.png"), (120,80)))
        self.death_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Goblin/Death/20.png"), (120,80)))
        self.death_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Goblin/Death/30.png"), (120,80)))

        #Monster values
        self.current_sprite = 0
        self.image = self.run_right_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect_bottomleft = (x,y)
        self.starting_x = x
        self.starting_y = y
        self.ground_tiles = ground_tiles
        self.position = vector(x, y)
        self.velocity = vector(0, 0)
        self.gothit = False
        self.lifes = 2
        self.dead = False
    
    def update(self):
        #Create a mask
        self.mask = pygame.mask.from_surface(self.image)

        #Draw the mask
        mask_outline = self.mask.outline()
        pygame.draw.lines(self.image,(255,0,0), True, mask_outline)

        self.run()
        self.collisions()
        self.hit()
        self.check_lives()
        self.check_animations()

    def animate(self, sprite_list, speed):
        if self.current_sprite < len(sprite_list) - 1:
            self.current_sprite += speed
            if self.gothit:
                if looking_left and self.dead == False:
                   self.velocity.x = -4
                elif looking_left == False and self.dead == False:
                    self.velocity.x = 4
            if self.dead:
                self.velocity.x = 0


        else:
            self.current_sprite = 0
            if self.gothit:
                self.gothit = False
            if self.dead:
                self.kill()
                self.dead = False

        self.image = sprite_list[int(self.current_sprite)]

    def run(self):
        if self.gothit == False and self.dead == False:
           self.velocity.x = 2
           self.animate(self.run_right_sprites, 0.2)
        self.position += self.velocity 
        
        if self.position.x < -72:
            self.position.x = WINDOW_WIDTH - 70
        elif self.position.x > WINDOW_WIDTH - 70:
            self.position.x = -60
        elif self.position.y > WINDOW_HEIGHT + 48:
            self.position.y = 0
        self.rect.bottomleft = self.position

    def collisions(self):
        collided_platforms = pygame.sprite.spritecollide(self, ground_tile_group, False, pygame.sprite.collide_mask)
        if collided_platforms:
            if self.velocity.y > 0:
                self.position.y = collided_platforms[0].rect.top + 28
                self.velocity.y = 0
        else:
            self.velocity.y = 7
    
    def hit(self):
        collided_sprites = pygame.sprite.spritecollide(self, my_player_group, False, pygame.sprite.collide_mask)
        if collided_sprites:
            if launching_attack == True:
               self.gothit = True
               self.current_sprite = 0
               self.lifes -= 0.1
    
    def check_lives(self):
        if self.lifes <= 0:
            self.dead = True

    def check_animations(self):
        if self.gothit and self.dead == False:
            self.animate(self.gethit_right_sprites, 0.1)
        if self.dead:
            self.animate(self.death_right_sprites, 0.1)
            self.velocity.y = 0
            

class Mushroom(pygame.sprite.Sprite):
    pass

class Skeleton(pygame.sprite.Sprite):
    def __init__(self, x, y, ground_tiles):
        super().__init__()

    #Animation frames
        self.run_right_sprites = []
        self.run_left_sprites = []
        self.gethit_right_sprites = []
        self.gethit_left_sprites = []
        self.death_right_sprites = []
        self.death_left_sprites = []
        self.shield_sprites = []
        
        #Run right
        self.run_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Skeleton/Run/00.png"), (150,150)))
        self.run_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Skeleton/Run/10.png"), (150,150)))
        self.run_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Skeleton/Run/20.png"), (150,150)))
        self.run_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Skeleton/Run/30.png"), (150,150)))

        #Run left
        for sprite in self.run_right_sprites:
            self.run_left_sprites.append(pygame.transform.flip(sprite, True, False))
        
        #Get hit right
        self.gethit_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Skeleton/Hit/00.png"), (150,150)))
        self.gethit_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Skeleton/Hit/10.png"), (150,150)))
        self.gethit_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Skeleton/Hit/20.png"), (150,150)))
        self.gethit_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Skeleton/Hit/30.png"), (150,150)))
        
        #Get hit left
        for sprite in self.gethit_right_sprites:
            self.gethit_left_sprites.append(pygame.transform.flip(sprite, True, False))
        
        #Die right
        self.death_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Skeleton/Death/00.png"), (150,150)))
        self.death_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Skeleton/Death/10.png"), (150,150)))
        self.death_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Skeleton/Death/20.png"), (150,150)))
        self.death_right_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Skeleton/Death/30.png"), (150,150)))
        
        #Die left
        for sprite in self.gethit_right_sprites:
            self.death_left_sprites.append(pygame.transform.flip(sprite, True, False))

        #Shield
        self.shield_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Skeleton/Shield/00.png"), (150,150)))
        self.shield_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Skeleton/Shield/10.png"), (150,150)))
        self.shield_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Skeleton/Shield/20.png"), (150,150)))
        self.shield_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Monsters/Skeleton/Shield/30.png"), (150,150)))
        #Monster values
        self.current_sprite = 0
        self.image = self.run_left_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.midtop = (x,y)
        self.starting_x = x
        self.starting_y = y
        self.ground_tiles = ground_tiles
        self.position = vector(x, y)
        self.velocity = vector(0, 0)
        self.gothit = False
        self.lifes = 2
        self.dead = False
        self.attacking = False
        self.shield = False
        
    def update(self):
        #Create a mask
        self.mask = pygame.mask.from_surface(self.image)

        #Draw the mask
        mask_outline = self.mask.outline()
        pygame.draw.lines(self.image,(0,255,0), True, mask_outline)

        self.run()
        self.collisions()
        self.hit()
        self.check_lives()
        self.check_animations()

    def animate(self, sprite_list, speed):
        if self.current_sprite < len(sprite_list) - 1:
            self.current_sprite += speed
            if self.gothit:
                if looking_left and self.dead == False:
                   self.velocity.x = -4
                elif looking_left == False and self.dead == False:
                    self.velocity.x = 4
            if self.dead:
                self.velocity.x = 0
            if self.shield:
                self.velocity.x = -4


        else:
            self.current_sprite = 0
            if self.gothit:
                self.gothit = False
            if self.dead:
                self.kill()
                self.dead = False
            if self.shield:
                self.shield = False

        self.image = sprite_list[int(self.current_sprite)]

    def run(self):
        if self.gothit == False and self.dead == False:
           self.velocity.x = -1
           self.animate(self.run_left_sprites, 0.2)
        self.position += self.velocity 
        
        if self.position.x < -72:
            self.position.x = WINDOW_WIDTH - 70
        elif self.position.x > WINDOW_WIDTH - 70:
            self.position.x = -60
        elif self.position.y > WINDOW_HEIGHT + 48:
            self.position.y = 0
        self.rect.bottomleft = self.position

    def collisions(self):
        collided_platforms = pygame.sprite.spritecollide(self, ground_tile_group, False, pygame.sprite.collide_mask)
        if collided_platforms:
            if self.velocity.y > 0:
                self.position.y = collided_platforms[0].rect.top + 50
                self.velocity.y = 0
        else:
            self.velocity.y = 7
    
    def hit(self):
        collided_sprites = pygame.sprite.spritecollide(self, my_player_group, False, pygame.sprite.collide_mask)
        if collided_sprites:
            if launching_attack == True:
                if looking_left == False:
                  self.gothit = True
                  self.current_sprite = 0
                  self.lifes -= 0.1
                else:
                    self.shield = True
    
    def check_lives(self):
        if self.lifes <= 0:
            self.dead = True

    def check_animations(self):
        if self.gothit and self.dead == False:
            self.animate(self.gethit_right_sprites, 0.1)
        if self.dead:
            self.animate(self.death_right_sprites, 0.1)
        if self.shield:
            self.animate(self.shield_sprites, 0.1)
            
class Samurai(pygame.sprite.Sprite):
    pass

class Demon(pygame.sprite.Sprite):
    pass

class Wizard(pygame.sprite.Sprite):
    pass

class Portal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        #Portal sprites
        self.portal_sprites = []

        #Portal animation
        self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Portal/tile009.png"), (72,72)))
        self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Portal/tile010.png"), (72,72)))
        self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Portal/tile011.png"), (72,72)))
        self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Portal/tile012.png"), (72,72)))
        self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Portal/tile013.png"), (72,72)))
        self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Portal/tile014.png"), (72,72)))
        self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Portal/tile015.png"), (72,72)))
        self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Portal/tile016.png"), (72,72)))
        self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Portal/tile017.png"), (72,72)))
        self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Portal/tile018.png"), (72,72)))
        self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Portal/tile019.png"), (72,72)))
        self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Portal/tile020.png"), (72,72)))
        self.portal_sprites.append(pygame.transform.scale(pygame.image.load("Graphics/Knight_Game/Portal/tile021.png"), (72,72)))

        #Values
        self.current_sprite = 0
        self.image = self.portal_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.midtop = (x,y)
        

    def update(self):
        self.animate(self.portal_sprites, .2)

    def animate(self, sprite_list, speed):
        if self.current_sprite < len(sprite_list) -1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0
            self.kill()

        self.image = sprite_list[int(self.current_sprite)]



#Create sprite groups
main_tile_group = pygame.sprite.Group()
ground_tile_group = pygame.sprite.Group()
my_player_group = pygame.sprite.Group()
enemies_group = pygame.sprite.Group()
portal_group = pygame.sprite.Group()

#Create the tile map: 0 -> no tile, 1 -> ground, 2 -> groundleft, 3 -> groundright
#20 rows and 30 columns
tile_map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 4, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 0, 0, 0, 0, 0, 0],
    [2, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 3],
    [4, 6, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 6, 5],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 0, 0, 0],
    [0, 0, 0, 4, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3],
    [4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 5],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 0, 0]
]

#Create individual Tile objects from the tile map
#Loop through the 20 lists in tile_map (i moves us down the map)
for i in range(len(tile_map)):
    #Loop through the 30 elements in a given list (j moves us across the map)
    for j in range(len(tile_map[i])):
        if tile_map[i][j] == 1:
            tile_1 = Tile(j*24, i*24, 1, main_tile_group, ground_tile_group)
            ground_tile_group.add(tile_1)
        elif tile_map[i][j] == 2:
            Tile(j*24, i*24, 2, main_tile_group, ground_tile_group)
        elif tile_map[i][j] == 3:
            Tile(j*24, i*24, 3, main_tile_group, ground_tile_group)
        elif tile_map[i][j] == 4:
            Tile(j*24, i*24, 4, main_tile_group, ground_tile_group)
        elif tile_map[i][j] == 5:
            Tile(j*24, i*24, 5, main_tile_group, ground_tile_group)
        elif tile_map[i][j] == 6:
            Tile(j*24, i*24, 6, main_tile_group, ground_tile_group)
        elif tile_map[i][j] == 7:
            my_player = Player(j*24, i*24 + 24, ground_tile_group)
            my_player_group.add(my_player)
        elif tile_map[i][j] == 8:
            my_goblin = Goblin(j*24,i*24 + 24, ground_tile_group)
            enemies_group.add(my_goblin)
        elif tile_map[i][j] == 9:
            my_eye = Eye(j*24,i*24 + 24, ground_tile_group)
            enemies_group.add(my_eye)
        elif tile_map[i][j] == 10:
            my_skeleton = Skeleton(j*24,i*24 + 24, ground_tile_group)
            enemies_group.add(my_skeleton)
        elif tile_map[i][j] == 11:
            my_portal = Portal(j*24,i*24 + 24)
            portal_group.add(my_portal)


#Load in a background image
background_image = pygame.image.load("Graphics/Knight_Game/Enviroment2/background/background_1.png")
background_rect = background_image.get_rect()
background_rect.topleft = (0, 0)

#Running game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                my_player.jump()
            if event.key == pygame.K_a:
                my_player.attack()
            if event.key == pygame.K_r:
                my_player.roll()


 #Blit the background
    display_surface.blit(background_image, background_rect)

#Draw tiles
    main_tile_group.draw(display_surface)
    main_tile_group.update()
    
#Update and draw sprites
    my_player_group.update()
    my_player_group.draw(display_surface)
    enemies_group.update()
    enemies_group.draw(display_surface)
    portal_group.update()
    portal_group.draw(display_surface)
  
#Tick the clock
    pygame.display.update()
    clock.tick(FPS)

pygame.quit