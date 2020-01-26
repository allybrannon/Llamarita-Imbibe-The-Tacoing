import pygame
import random
import os

WIDTH = 1000
HEIGHT = 800
FPS = 30

BLUE_COLOR = (97, 159, 182)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set-up assests (art/sound) folders - use this to load graphics
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
       # self.image = pygame.image.load(os.path.join(img_folder, llama_img)).convert()
        self.image = pygame.transform.scale(llama_img, (90, 120))
        self.rect = self.image.get_rect()
        self.image.set_colorkey(WHITE)
        self.radius = 60
        self.rect.centerx = int(WIDTH / 10)
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.lives = 3
        self.points = 0
        #self.y_speed = 5
        # self.lives = 3
        # self.hidden = False
        # self.hide_timer = pygame.time_ticks()

    #Causes the player to move
    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left <= 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(taco_img, (50, 34))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 25
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1,8)

class Marg(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(marg_img, (60, 40))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.radius = 25
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1,8)

class Cactus(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(cactus_img, (50, 70))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 5
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1,8)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 30

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
        

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("It's Raining Tacos")
clock = pygame.time.Clock()

# Load all game graphics
background = pygame.image.load(os.path.join(img_folder, "Daytime_Background.png")).convert()
background_rect = background.get_rect()
#background_grass = pygame.image.load(os.path.join(img_folder, "Grass_bar.png")).convert()
#background_grass_rect = background_grass.get_rect()
taco_img = pygame.image.load(os.path.join(img_folder, "taco.png")).convert()
llama_img = pygame.image.load(os.path.join(img_folder, "llama.png")).convert()
#llama_mini_img = pygame.transform.scale(llama_img, (25, 19))
marg_img = pygame.image.load(os.path.join(img_folder, "margarita.png")).convert()
cactus_img = pygame.image.load(os.path.join(img_folder, "new_cactus.png")).convert()

explosion_anim = {}
explosion_anim['lg'] = []
for i in range(5):
    filename = 'explosiongreen%d.png' % i
    img = pygame.image.load(os.path.join(img_folder, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (200, 200))
    explosion_anim['lg'].append(img_lg)

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
marg = pygame.sprite.Group()
cactus = pygame.sprite.Group()
all_sprites.add(player)

for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

for i in range(8):
    n = Marg()
    all_sprites.add(n)
    marg.add(n)

for i in range(8):
    o = Cactus()
    all_sprites.add(o)
    cactus.add(o)

def main():

    # Game initialization

    stop_game = False
    while not stop_game:
        #keep loop runningat the right speed
        #clock.tick(FPS)
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()

        all_sprites.update()
        # Check to see if a bullet hit a mob
        hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
        for hit in hits:
            m = Mob()
            all_sprites.add(m)
            mobs.add(m)

        # check to see if a mob hit a player
        hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
        for hit in hits:
            player.points += 1
        if player.points == 10:
            stop_game = True

        # Check to see if a bullet hit a marg
        hits_2 = pygame.sprite.groupcollide(marg, bullets, True, True)
        for hit in hits_2:
            n = Marg()
            all_sprites.add(n)
            marg.add(n)

        # check to see if a cactus hit a player
        hits_3 = pygame.sprite.spritecollide(player, cactus, True)
        for hit in hits_3:
            player.lives -= 1
        if player.lives <= 0:
            death_explosion = Explosion(player.rect.center, 'lg')
            all_sprites.add(death_explosion)
            player.kill()
        
        #if the player died and the explosion has finished
        if not player.alive() and not death_explosion.alive():
            stop_game = True


        # check to see if a marg hit a players
        hits_2 = pygame.sprite.spritecollide(player, marg, True)
        for hit in hits_2:
            player.points += 1
        if player.points == 10:
            stop_game = True



        # Game logic

        # Draw background
        screen.fill(BLUE_COLOR)
        screen.blit(background, background_rect)
        #screen.blit(background_grass, background_grass_rect)
        all_sprites.draw(screen)

        # Game display

        pygame.display.update()
        clock.tick(60)
        #pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
