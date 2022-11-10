import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLUMNS = 8, 8
SQUARE_SIZE = WIDTH//COLUMNS

TAN = (210, 180, 140)
BROWN = (245, 225, 175)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
GREEN = (0, 255, 0)
GREY = (128, 128, 128)

CROWN = pygame.transform.scale(pygame.image.load("assets/crown.png"), (45, 25))
