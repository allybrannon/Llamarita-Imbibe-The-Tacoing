# import pygame
# import random
# import os

# WIDTH = 1000
# HEIGHT = 800
# FPS = 60

# BLUE_COLOR = (97, 159, 182)
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)

# # Set-up assests (art/sound) folders - use this to load graphics
# game_folder = os.path.dirname(__file__)
# img_folder = os.path.join(game_folder, "img")

def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y
        surf.blit(img, img_rect)

# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#        # self.image = pygame.image.load(os.path.join(img_folder, llama_img)).convert()
#         self.image = pygame.transform.scale(llama_img, (90, 120))
#         self.rect = self.image.get_rect()
#         self.image.set_colorkey(WHITE)
#         self.radius = 60
#         self.rect.centerx = int(WIDTH / 10)
#         self.rect.bottom = HEIGHT - 10
#         self.speedx = 0
#         self.lives = 5
#         self.points = 0

#     #Causes the player to move
#     def update(self):
#         self.speedx = 0
#         keystate = pygame.key.get_pressed()
#         if keystate[pygame.K_LEFT]:
#             self.speedx = -8
#         if keystate[pygame.K_RIGHT]:
#             self.speedx = 8
#         self.rect.x += self.speedx
#         if self.rect.right > WIDTH:
#             self.rect.right = WIDTH
#         if self.rect.left <= 0:
#             self.rect.left = 0
        
# Load all game graphics
# background = pygame.image.load(os.path.join(img_folder, "Daytime_Background.png")).convert()
# background_rect = background.get_rect()
#background_grass = pygame.image.load(os.path.join(img_folder, "Grass_bar.png")).convert()
#background_grass_rect = background_grass.get_rect()
#taco_img = pygame.image.load(os.path.join(img_folder, "taco.png")).convert()
#llama_img = pygame.image.load(os.path.join(img_folder, "llama.png")).convert()
llama_mini_img = pygame.transform.scale(llama_img, (28, 22))
llama_mini_img.set_colorkey(BLACK)
#marg_img = pygame.image.load(os.path.join(img_folder, "margarita.png")).convert()
#cactus_img = pygame.image.load(os.path.join(img_folder, "new_cactus.png")).convert()


#def main():

    # Game initialization

    # stop_game = False
    # while not stop_game:
    #     #keep loop runningat the right speed
    #     #clock.tick(FPS)
    #     for event in pygame.event.get():

    #         # Event handling

    #         if event.type == pygame.QUIT:
    #             stop_game = True
    #         elif event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_SPACE:
    #                 player.shoot()

    #     all_sprites.update()
    #     # Check to see if a bullet hit a mob
    #     hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    #     for hit in hits:/
    #         m = Mob()
    #         all_sprites.add(m)
    #         mobs.add(m)

    #     # check to see if a mob hit a player
    #     hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
    #     for hit in hits:
    #         player.points += 1
    #     if player.points == 10:
    #         stop_game = True

        # Check to see if a bullet hit a marg
        # hits_2 = pygame.sprite.groupcollide(marg, bullets, True, True)
        # for hit in hits_2:
        #     n = Marg()
        #     all_sprites.add(n)
        #     marg.add(n)

        # # check to see if a marg hit a players
        # hits_2 = pygame.sprite.spritecollide(player, marg, True)
        # for hit in hits_2:
        #     player.points += 1
        # if player.points == 10:
        #     stop_game = True

        # # check to see if a cactus hit a player
        # hits_3 = pygame.sprite.spritecollide(player, cactus, True)
        # for hit in hits_3:
        #     player.lives -= 1
        # if player.lives <= 0:
        #     death_explosion = Explosion(player.rect.center, 'lg')
        #     all_sprites.add(death_explosion)
        #     player.kill()
        #     # player.hide()
        #     # player.lives -= 1

        
        #if the player died and the explosion has finished
        # if not player.alive() and not death_explosion.alive():
        #     stop_game = True

        # Game logic

        # Draw background
        # screen.fill(BLUE_COLOR)
        # screen.blit(background, background_rect)
        #screen.blit(background_grass, background_grass_rect)
       # all_sprites.draw(screen)
        draw_lives(screen, WIDTH - 200, 5, player.lives, llama_mini_img)

        # Game display

        # pygame.display.update()
        # clock.tick(60)
        #pygame.display.flip()

#     pygame.quit()

# if __name__ == '__main__':
#     main()
