import pygame

# initialize pygame
pygame.init()

# create display
width = 640
height = 480
display = pygame.display.set_mode((width, height))

# run update
pygame.display.update()
pygame.display.set_caption("Snake 2D")

# start loop
game_end = False

while not game_end:
    # game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_end = True

# close app, if required
pygame.quit()
quit()