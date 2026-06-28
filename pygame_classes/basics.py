import pygame

# Classe objeto, que será herdada por todas as outras classes, para que todas tenham a mesma estrutura básica.
class Object:
    def __init__(self, surface, x, y):
        self.surface = surface
        self.x = x
        self.y = y

    def update(self, delta_time):
        raise NotImplementedError("Subclasses must implement this method.")

    def set_position(self, x, y):
        self.x = x
        self.y = y