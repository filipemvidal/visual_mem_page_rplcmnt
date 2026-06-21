from abc import ABC, abstractmethod
from controllers.events import SimulationEvent


class PageReplacementAlgorithm(ABC):

    @abstractmethod
    def access(self, page: int) -> SimulationEvent:
        pass

    @abstractmethod
    def get_frames(self) -> list[int]:
        pass