import pygame  # load pygame keywords
import sys     # let  python use your file system
import os      # help python identify your OS

'''
Variables
'''

# put variables here
worldx = 960
worldy = 720
fps   = 60  # frame rate
ani   = 4   # animation cycles

# Colors
BLUE  = (25, 25, 200)
BLACK = (0, 0, 0)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)

main = True

'''
Objects
'''

# put Python classes and functions here
class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0 # move along X
        self.movey = 0 # move along Y
        self.frame = 0 # count frames

        self.images = []
        for i in range(1, 5):
            img = pygame.image.load(os.path.join('images', 'hero' + str(i) + '.png')).convert()
            #img.convert_alpha()  # optimise alpha
            #img.set_colorkey(BLACK)  # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.speed = 16
            self.rect = self.image.get_rect()
    
    def control(self, x, y):
        """
        control player movement
        """
        self.movex = x
        self.movey = y
    
    def update(self):
        self.rect.x += self.movex
        self.rect.y += self.movey

        frame = self.rect.x % (self.speed * len(self.images))
        self.image = self.images[int(frame / self.speed)]


'''
Setup
'''

# put run-once code here
clock = pygame.time.Clock()
pygame.init()
world = pygame.display.set_mode([worldx, worldy])
bg = pygame.image.load(os.path.join('images', 'stage.png'))
bgbox = world.get_rect()

player = Player()   # spawn player
player.rect.x = 0   # go to x
player.rect.y = worldy / 2   # go to y
player_list = pygame.sprite.Group()
player_list.add(player)

'''
Main Loop
'''

# put game loop here
while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('stop left')
                player.movex = 0
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('stop right')
                player.movex = 0
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[ord('a')]:
                player.control(-1, 0)
    if keys[pygame.K_RIGHT] or keys[ord('d')]:
                player.control(1, 0)
    if keys[pygame.K_UP] or keys[ord('w')]:
                print('jump')

    world.blit(bg, bgbox)
    player_list.update()
    player_list.draw(world) # draw player
    pygame.display.flip()
    clock.tick(fps)