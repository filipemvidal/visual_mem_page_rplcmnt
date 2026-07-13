from dataclasses import dataclass
from typing import Any, Dict


'''
Eventos para a visualização em console. Representam o estado da memória, qual página está sendo procurada,
qual página foi removida, se houve page fault e qual algoritmo está sendo utilizado.
'''
@dataclass
class SimulationEvent:
    algorithm: str
    page: int
    page_fault: bool
    removed_page: int | None
    frames: list[int]
    metadata: dict[str, Any] | None = None


'''
Representa uma célula da memória para a visualização em PyGame. 
'''
@dataclass
class ViewSimCell():
    page: int
    detail: str

'''
Representa um evento da simulação para a visualização em PyGame.
Um SimulationEvent gera vários ViewSimulationEvent, para que a visualização seja mais clara.
'''
@dataclass
class ViewSimulationEvent():
    page: str | None
    frames: list[ViewSimCell]
    page_fault: bool