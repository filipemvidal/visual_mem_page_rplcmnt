import pygame
import sys
import pygame_classes.table as table
from pygame_classes.basics import Scene, Object, Sprite
from algorithms import *
from controllers.simulator import Simulator


def run_simulation(algorithm_class, capacity: int, references: list[int], table_obj: table.Table):
    algo = algorithm_class(capacity=capacity)
    simulator = Simulator(algo)
    events = simulator.run(references)
    table_obj.handle_simulation_events(events)

pygame.init()

_width, _height = 1280, 720
screen = pygame.display.set_mode((_width, _height))
pygame.display.set_caption("Simulador de Algoritmos de Substituição de Páginas")

running = True
clock = pygame.time.Clock()

scene = Scene(screen)

FCFS_table = table.Table(160, 80, "FCFS/FIFO", 3)
LRU_table = table.Table(540, 80, "LRU", 3)
LFU_table = table.Table(960, 80, "LFU", 3)

scene.add_object(FCFS_table)
scene.add_object(LRU_table)
scene.add_object(LFU_table)

references = [1, 2, 3, 1, 4, 2, 5, 1]
run_simulation(FCFS, capacity=3, references=references, table_obj=FCFS_table)
run_simulation(LRU, capacity=3, references=references, table_obj=LRU_table)
run_simulation(LFU, capacity=3, references=references, table_obj=LFU_table)

FCFS_table.add_to_page_events(0)
LRU_table.add_to_page_events(0)
LFU_table.add_to_page_events(0)

index = 0
max_events_tracked = max(len(FCFS_table.events_tracked), len(LRU_table.events_tracked), len(LFU_table.events_tracked))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                index += 1
                if index >= max_events_tracked:
                    index = max_events_tracked - 1
                FCFS_table.add_to_page_events(index)
                LRU_table.add_to_page_events(index)
                LFU_table.add_to_page_events(index)
            elif event.key == pygame.K_LEFT:
                index -= 1
                if index < 0:
                    index = 0
                FCFS_table.add_to_page_events(index)
                LRU_table.add_to_page_events(index)
                LFU_table.add_to_page_events(index)

    screen.fill((255, 255, 255))

    scene.update(clock.get_time() / 1000.0)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()