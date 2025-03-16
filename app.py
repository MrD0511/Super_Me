import pygame
import sys
from player import Player
from cloud import Cloud
from camera import Camera
from ground_block import Ground_Block, Block, Treasure_Block, Stone
from tube import Tube
from mountain import Mountain
from big_mountain import Big_Mountain
from bush import Bush
from bush import Small_Bush
from cloud import Small_Cloud
from goombas import Goombas
from castle import Castle
from flag import Pillar
import os
import sys

def resource_path(relative_path):
    """Return the absolute path, ensuring it's inside the correct directory."""
    base_path = os.getcwd()  # Get current working directory
    return os.path.join(base_path, relative_path)


pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(resource_path("assets/music/bg.mp3"))
pygame.mixer.music.play(-1, 6)  # -1 makes it loop indefinitely
pygame.mixer.music.set_volume(0.5)  # Adjust volume if needed (0.0 to 1.0)

SCREEN_HEIGHT = 32*14
SCREEN_WIDTH = 32*25
FPS = 30

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Super Marco")

all_sprites = pygame.sprite.Group()
# Initialize Pygame
clouds = pygame.sprite.Group()

clock = pygame.time.Clock()
# Main game loop
running = True

ground_blocks = pygame.sprite.Group()
blocks = pygame.sprite.Group()
treasure_blocks = pygame.sprite.Group()
tubes = pygame.sprite.Group()
mountains = pygame.sprite.Group()
bushes = pygame.sprite.Group()
coins = pygame.sprite.Group()
collidable_objs = pygame.sprite.Group()
collidable_enimies = pygame.sprite.Group()
goomabases = pygame.sprite.Group()
stones = pygame.sprite.Group()
castle_group = pygame.sprite.Group()
flag = pygame.sprite.Group()
pillar = pygame.sprite.Group()

level_map = [ 
    "                              c                                                      C                                                                                                                                                                          ",
    "      C                                C         c                     c                                                                             C                                                                                                          ",
    "                     C                              C                                                                       C                                                                                           F                            C          ",
    "          c                                                                                                  C                        c                                      c                                 ss                    c                          ",
    "                      T                                   C             C           g g                           c                                                                              C            sss                                          c    ",
    "                                                                                   llllllll   lllT                     T             llll    lTTl                                                            ssss                                               ",
    "                                                                                                                                                                                                            sssss               E                               ",
    "                 T  lTlTl                         P          P                                                                                         s  s          ss  s                                 ssssss                                               ",
    "M                                       P           M                          lTl                    l   M   ll    T  T  T       l           ll      ss  ss        sss  ss               llTl            sssssss  M                                            ",
    "               M            P                                       M                                                     M                          sss  sss M    ssss  sss   M   P                  P  ssssssss                      M                        ",
    "          B    g       b                   B  g       g  g     B            b               b             g g        B         g g  b    g g  g g   ssssB ssss    sssss  ssss             b     g g     sssssssss       s        B           b                  ",
    "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG  GGGGGGGGGGGGGG   GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG  GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",
    "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG  GGGGGGGGGGGGGG   GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG  GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",
]

camera = Camera(len(level_map[0]) * 32, len(level_map) * 32, SCREEN_WIDTH, SCREEN_HEIGHT)
for row_index,row in enumerate(level_map):
    for col_index, col in enumerate(row):
        if col == 'G':
            block = Ground_Block(col_index*32, row_index*32)
            collidable_objs.add(block)
            ground_blocks.add(block)
        
        elif col == 'C':
            cloud = Cloud(col_index*32, row_index*32)
            clouds.add(cloud)

        elif col == 'c':
            cloud = Small_Cloud(col_index*32, row_index*32)
            clouds.add(cloud)

        elif col == 'm':
            mountain = Mountain(col_index*32, row_index*32)
            mountains.add(mountain)

        elif col == 'M':
            mountain = Big_Mountain(col_index*32, row_index*32)
            mountains.add(mountain)
        
        elif col == 'B':
            bush = Bush(col_index*32, row_index*32)
            bushes.add(bush)
        
        elif col == 'b':
            bush = Small_Bush(col_index*32, row_index*32)
            mountains.add(bush)
        
        elif col == 'P':
            tube = Tube(col_index*32, row_index*32)
            collidable_objs.add(tube)
            tubes.add(tube)

        elif col == 'E':
            castle = Castle(col_index*32, row_index*32)
            castle_group.add(castle)

        elif col == 'l':
            block = Block(col_index*32, row_index*32)
            collidable_objs.add(block)
            blocks.add(block)

        elif col == 'T':
            block = Treasure_Block(col_index*32, row_index*32)
            collidable_objs.add(block)
            treasure_blocks.add(block)

        elif col == 'F':
            pillar_class = Pillar(col_index*32 + 5, row_index*32 - 15)
            pillar.add(pillar_class)
            collidable_objs.add(pillar_class)
            flag.add(pillar_class.flag)

        elif col == 's':
            stone = Stone(col_index*32, row_index*32)
            collidable_objs.add(stone)
            stones.add(stone)

        elif col == 'g':
            goomabas = Goombas(col_index*32, row_index*32)
            collidable_enimies.add(goomabas)
            goomabases.add(goomabas)


player = Player(300, SCREEN_HEIGHT - 4 * 32 )

pygame.font.init()  # Initialize fonts
font = pygame.font.Font(None, 36)  # Create font object
big_font = pygame.font.Font(None, 55)

def draw_score(screen, player):
    """Displays the player's score"""
    score_text = font.render(f"Score: {player.score}", True, (255, 255, 255))
    screen.blit(score_text, (20, 20))  # Display in top-left corner
    coins_text = font.render(f"Coins: {player.coins}", True, (255, 255, 255))
    screen.blit(coins_text, (680, 20))

def draw_game_status(screen, player):
    if player.mario_dead:
        status_text = big_font.render(f"Game Over", True, (255, 255, 255))
        text_rect = status_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(status_text, text_rect)
    elif player.game_over:
        status_text = big_font.render(f"Game Finished", True, (255, 255, 255))
        text_rect = status_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(status_text, text_rect)

    
def restart_game():
    global player, all_sprites, collidable_objs, collidable_enimies, ground_blocks, blocks, treasure_blocks, tubes, mountains, bushes, coins, goomabases, stones, castle_group, flag, pillar

    pygame.mixer.stop()

    # Restart background music
    pygame.mixer.music.load(resource_path("assets/music/bg.mp3"))  # Load your background music file
    pygame.mixer.music.play(-1, 6)  # Loop music indefinitely
    pygame.mixer.music.set_volume(0.5)
    # Clear all sprite groups
    all_sprites.empty()
    collidable_objs.empty()
    collidable_enimies.empty()
    ground_blocks.empty()
    blocks.empty()
    treasure_blocks.empty()
    tubes.empty()
    mountains.empty()
    bushes.empty()
    coins.empty()
    goomabases.empty()
    stones.empty()
    castle_group.empty()
    flag.empty()
    pillar.empty()

    # Reinitialize player
    player = Player(300, SCREEN_HEIGHT - 4 * 32)
    all_sprites.add(player)

    # Reinitialize level
    for row_index, row in enumerate(level_map):
        for col_index, col in enumerate(row):
            if col == 'G':
                block = Ground_Block(col_index * 32, row_index * 32)
                collidable_objs.add(block)
                ground_blocks.add(block)
            elif col == 'C':
                cloud = Small_Cloud(col_index * 32, row_index * 32)
                clouds.add(cloud)
            elif col == 'm':
                mountain = Mountain(col_index * 32, row_index * 32)
                mountains.add(mountain)
            elif col == 'M':
                mountain = Big_Mountain(col_index * 32, row_index * 32)
                mountains.add(mountain)
            elif col == 'B':
                bush = Bush(col_index * 32, row_index * 32)
                bushes.add(bush)
            elif col == 'b':
                bush = Small_Bush(col_index * 32, row_index * 32)
                mountains.add(bush)
            elif col == 'P':
                tube = Tube(col_index * 32, row_index * 32)
                collidable_objs.add(tube)
                tubes.add(tube)
            elif col == 'E':
                castle = Castle(col_index * 32, row_index * 32)
                castle_group.add(castle)
            elif col == 'l':
                block = Block(col_index * 32, row_index * 32)
                collidable_objs.add(block)
                blocks.add(block)
            elif col == 'T':
                block = Treasure_Block(col_index * 32, row_index * 32)
                collidable_objs.add(block)
                treasure_blocks.add(block)
            elif col == 'F':
                pillar_class = Pillar(col_index * 32 + 5, row_index * 32 - 15)
                pillar.add(pillar_class)
                collidable_objs.add(pillar_class)
                flag.add(pillar_class.flag)
            elif col == 's':
                stone = Stone(col_index * 32, row_index * 32)
                collidable_objs.add(stone)
                stones.add(stone)
            elif col == 'g':
                goomabas = Goombas(col_index * 32, row_index * 32)
                collidable_enimies.add(goomabas)
                goomabases.add(goomabas)

# Set up display
all_sprites.add(player)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            if pygame.key.get_mods() & pygame.KMOD_CTRL:
                restart_game()

    # Update everything
    player.update(collidable_objs, collidable_enimies)
    camera.update(player)
    blocks.update()
    treasure_blocks.update(coins)
    coins.update()
    goomabases.update(collidable_objs, player)
    pillar.update()

    # Draw everything
    screen.fill((0, 140, 250)) 

    # Draw background elements (mountains, clouds, bushes)
    for group in [bushes, mountains, clouds, coins]:
        for sprite in group:
            screen.blit(sprite.image, camera.apply(sprite))

    # Draw castle, flag, and pillar
    for group in [castle_group, pillar, flag]:
        for sprite in group:
            screen.blit(sprite.image, camera.apply(sprite))

    # Draw collidable objects (ground, tubes, blocks, stones, etc.)
    for sprite in collidable_objs:
        screen.blit(sprite.image, camera.apply(sprite))

    # Draw enemies
    for enemy in collidable_enimies:
        screen.blit(enemy.image, camera.apply(enemy))

    # Draw all other sprites (like Mario)
    for sprite in all_sprites:
        screen.blit(sprite.image, camera.apply(sprite))

    draw_score(screen, player)
    draw_game_status(screen, player)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
