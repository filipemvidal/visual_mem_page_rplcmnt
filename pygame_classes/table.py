import pygame
from pygame_classes.basics import Object, Text
from controllers.events import SimulationEvent, ViewSimulationEvent, ViewSimCell

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Table(Object):
    # São static, para evitar alteração do tamanho da célula quando mudar.
    cell_width = 100
    cell_height = 50

    def __init__(self, x, y, title, max_cells=5):
        super().__init__(x, y)
        self.title = title
        self.cells = []
        self.max_cells = max_cells
        self.page_fault_text = Text(self.x, self.y - 30, "Page Fault!", font_size=20, color=(255, 0, 0))
        self.procurando_text = Text(self.x, self.y - 60, "Procurando página...", font_size=20, color=(0, 0, 255))
        self.page_fault_text.set_visible(False)
        self.procurando_text.set_visible(False)
        self.events_tracked = []

    def set_scene(self, scene):
        super().set_scene(scene)
        self.scene.add_object(self.page_fault_text)
        self.scene.add_object(self.procurando_text)

    def create_cell(self, text):
        if len(self.cells) >= self.max_cells:
            raise ValueError("Maximum number of cells reached")
        y = (len(self.cells) + 1) * self.cell_height
        cell = Cell(0, y, self, text, self.cell_width, self.cell_height)
        self.add_cell(cell)
        self.scene.add_object(cell)
        return cell

    def add_cell(self, cell):
        if not isinstance(cell, Cell):
            raise TypeError("cell must be an instance of Cell class")
        if len(self.cells) >= self.max_cells:
            raise ValueError("Maximum number of cells reached")
        self.cells.append(cell)

    def clear_cells(self):
        for cell in self.cells:
            self.scene.remove_object(cell)
        self.cells.clear()

    def update(self, surface, delta_time):
        self.draw(surface)

    def draw(self, surface):
        rect = pygame.Rect(self.x, self.y + self.cell_height, self.cell_width, self.max_cells * self.cell_height)
        pygame.draw.rect(surface, BLACK, rect, 2)
        font = pygame.font.Font(None, 36)
        title_surface = font.render(self.title, True, BLACK, None)
        surface.blit(title_surface, (self.x, self.y))

    def handle_simulation_events(self, events: list[SimulationEvent]):
        new_events = []
        new_events.append(ViewSimulationEvent(
            page=None,
            frames=[],
            page_fault=False
        ))
        old_view_cells = {}
        for event in events:
            if not isinstance(event, SimulationEvent):
                raise TypeError("event must be an instance of SimulationEvent class")

            frames_values = old_view_cells.copy()
            for page in frames_values:
                frames_values[page] = ViewSimCell(page=frames_values[page].page if frames_values[page].page is not None else None, detail="")

            new_events.append(ViewSimulationEvent(
                page=str(event.page) if event.page is not None else None,
                frames=list(frames_values.values()),
                page_fault=False
            ))


            view_cells = {}
            if event.page_fault:
                new_events.append(ViewSimulationEvent(
                    page=str(event.page) if event.page is not None else None,
                    frames=list(old_view_cells.values()),
                    page_fault=True
                ))

            for page in event.frames:
                view_cells[page] = ViewSimCell(page=page if page is not None else None, detail="")
            if event.removed_page is not None:
                old_view_cells_2 = old_view_cells.copy()
                old_view_cells_2[event.removed_page].detail = "removed"
                new_events.append(ViewSimulationEvent(
                    page=str(event.page) if event.page is not None else None,
                    frames=list(old_view_cells_2.values()),
                    page_fault=False
                ))

            view_cells[event.page].detail = "selected"

            #Grava na lista
            view_event = ViewSimulationEvent(
                page=str(event.page) if event.page is not None else None,
                frames=list(view_cells.values()),
                page_fault=False
            )
            new_events.append(view_event)

            #Limpa old_view_cells
            old_view_cells = view_cells.copy()
            for key in old_view_cells:
                old_view_cells[key] = ViewSimCell(page=old_view_cells[key].page, detail="")

        self.events_tracked = new_events

    def handle_view_event(self, event):
        if not isinstance(event, ViewSimulationEvent):
            raise TypeError("event must be an instance of ViewSimulationEvent class")
        self.clear_cells()
        self.page_fault_text.set_visible(event.page_fault)
        if event.page is not None:
            self.procurando_text.set_visible(True)
            self.procurando_text.set_text(f"Procurando página {event.page}...")
        else:
            self.procurando_text.set_visible(False)
        for view_cell in event.frames:
            cell_text = f"Página {view_cell.page}" if view_cell.page is not None else ""
            cell = self.create_cell(cell_text)
            cell.set_selected(view_cell.detail)

    def add_to_page_events(self, index):
        if index < 0:
            index = 0
        elif index >= len(self.events_tracked):
            index = len(self.events_tracked) - 1
        self.handle_view_event(self.events_tracked[index])


class Cell(Object):
    def __init__(self, _x, _y, table : Table, text, width=100, height=50):
        super().__init__(_x, _y)
        self.text = text
        self.table = table
        self.width = width
        self.height = height
        self.border_color = BLACK
        self.border_width = 1

    def set_selected(self, value):
        if value == "selected":
            self.border_color = (0, 255, 0)  # Verde
            self.border_width = 3
        elif value == "removed":
            self.border_color = (255, 0, 0)  # Vermelho
            self.border_width = 3
        else:
            self.border_color = BLACK
            self.border_width = 1

    def set_table(self, table):
        if not isinstance(table, Table):
            raise TypeError("table must be an instance of Table class")
        self.table = table

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
        pygame.draw.rect(surface, self.border_color, cell_rect, self.border_width)

        # Desenha o texto da célula
        font = pygame.font.Font(None, 24)
        text_surface = font.render(self.text, True, self.border_color)
        text_rect = text_surface.get_rect(center=cell_rect.center)
        surface.blit(text_surface, text_rect)