import pygame
import sys
import pygame_classes.table as table
from pygame_classes.basics import Scene, Object, Sprite

pygame.init()

_width, _height = 1280, 720
screen = pygame.display.set_mode((_width, _height))
pygame.display.set_caption("Simulador de Algoritmos de Substituição de Páginas")

running = True
clock = pygame.time.Clock()

scene1 = Scene(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    scene1.update(clock.get_time() / 1000.0)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()