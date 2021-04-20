import pygame  # load pygame keywords
import sys     # let  python use your file system
import os      # help python identify your OS

'''
Variables
'''

# put variables here
worldx = 960
worldy = 720
fps   = 40  # frame rate
ani   = 4   # animation cycles

# Colors
BLUE  = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)

main = True

'''
Objects
'''

# put Python classes and functions here


'''
Setup
'''

# put run-once code here
clock = pygame.time.Clock()
pygame.init()
world = pygame.display.set_mode([worldx, worldy])
world.fill(BLUE)

'''
Main Loop
'''

# put game loop here
while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
            try:
                sys.exit()
            finally:
                main = False
    pygame.display.flip()
    clock.tick(fps)