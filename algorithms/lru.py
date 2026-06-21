from algorithms.base import PageReplacementAlgorithm
from controllers.events import SimulationEvent


class LRU(PageReplacementAlgorithm):

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.frames = []
        self.recency = []

    def access(self, page: int) -> SimulationEvent:

        # Hit
        if page in self.frames:

            self.recency.remove(page)
            self.recency.append(page)

            return SimulationEvent(
                algorithm="LRU",
                page=page,
                page_fault=False,
                removed_page=None,
                frames=self.frames.copy(),
                metadata={"recency": self.recency.copy()}
            )

        removed = None

        # Memória cheia
        if len(self.frames) >= self.capacity:

            removed = self.recency.pop(0)

            self.frames.remove(removed)

        self.frames.append(page)
        self.recency.append(page)

        return SimulationEvent(
            algorithm="LRU",
            page=page,
            page_fault=True,
            removed_page=removed,
            frames=self.frames.copy(),
            metadata={"recency": self.recency.copy()}
        )

    def get_frames(self) -> list[int]:
        return self.frames.copy()