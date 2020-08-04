import pygame
import random
import time

pygame.init()
display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('BEST 3D PLATFORMER FPS GAME!')  # Yeah, exactly :)

clock = pygame.time.Clock()

display.fill((255, 255, 255))


def newposition():
    randx = random.randrange(100, 700)
    randy = random.randrange(100, 500)
    return randx, randy  # Output the generated values


rand_coords = newposition()  # Get rand coords

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Quit pygame if window in closed
        # if event.ty why is that here?

    clock.tick(60)  # This needs to be in the loop

    display.fill((255, 255, 255))  # You need to refill the screen with white every frame.
    # display.blit((rand_coords[0],rand_coords[1])) # Take our generated values
    pygame.display.update()
