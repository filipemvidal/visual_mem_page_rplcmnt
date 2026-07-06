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

memoria_principal = table.Table(200, 50, "Memória Principal")
cell1 = memoria_principal.create_cell("Página 1")
cell2 = memoria_principal.create_cell("Página 2")
cell3 = memoria_principal.create_cell("Página 3")
cpu = Sprite(200, _height/2, "./views/images/CPU_icon.png", scale=0.5)

scene1.add_object(memoria_principal)
scene1.add_object(cell1)
scene1.add_object(cell2)
scene1.add_object(cell3)
scene1.add_object(cpu)

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