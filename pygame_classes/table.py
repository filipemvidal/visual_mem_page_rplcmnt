import pygame
from pygame_classes.basics import Object

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Table(Object):
    # São static, para evitar alteração do tamanho da célula quando mudar.
    cell_width = 100
    cell_height = 50

    def __init__(self, x, y, title, cells = []):
        super().__init__(x, y)
        self.title = title
        self.cells = cells

    def create_cell(self, text):
        cell = Cell(0, (len(self.cells) + 1) * self.cell_height, self, text, self.cell_width, self.cell_height)
        self.add_cell(cell)
        return cell

    def add_cell(self, cell):
        if not isinstance(cell, Cell):
            raise TypeError("cell must be an instance of Cell class")
        self.cells.append(cell)

    def update(self, surface, delta_time):
        self.draw(surface)

    def draw(self, surface):
        font = pygame.font.Font(None, 36)
        title_surface = font.render(self.title, True, BLACK, None)
        surface.blit(title_surface, (self.x, self.y))

class Cell(Object):
    def __init__(self, _x, _y, table : Table, text, width=100, height=50):
        super().__init__(_x, _y)
        self.text = text
        self.table = table
        self.width = width
        self.height = height

    def set_table(self, table):
        if not isinstance(table, Table):
            raise TypeError("table must be an instance of Table class")
        self.table = table
        # TODO: Implementar movimentação da célula para a tabela

    def get_position(self):
        return (self.table.x + self.x, self.table.y + self.y)

    def set_position(self, _x, _y):
        self.x = _x
        self.y = _y

    def update(self, surface, delta_time):
        self.draw(surface)

    def draw(self, surface):
        # Desenha a célula
        cell_rect = pygame.Rect(self.table.x + self.x, self.table.y + self.y, self.width, self.height)
        pygame.draw.rect(surface, WHITE, cell_rect)
        pygame.draw.rect(surface, BLACK, cell_rect, 1)

        # Desenha o texto da célula
        font = pygame.font.Font(None, 24)
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=cell_rect.center)
        surface.blit(text_surface, text_rect)