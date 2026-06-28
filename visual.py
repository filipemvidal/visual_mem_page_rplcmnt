import pygame
import sys
import pygame_classes.table as table
import pygame_classes.basics as basics

pygame.init()

_width, _height = 1280, 720
screen = pygame.display.set_mode((_width, _height))
pygame.display.set_caption("Simulador de Algoritmos de Substituição de Páginas")

running = True
clock = pygame.time.Clock()

objects = []

memoria_principal = table.Table(screen, 200, 50, "Memória Principal")
memoria_secundaria = table.Table(screen, 500, 50, "Memória Secundária")
cell1 = memoria_principal.create_cell("Página 1")
cell2 = memoria_principal.create_cell("Página 2")
cell3 = memoria_principal.create_cell("Página 3")

objects.extend([cell1, cell2, cell3])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    for obj in objects:
        obj.draw()

    memoria_principal.draw()
    memoria_secundaria.draw()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()