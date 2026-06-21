from collections import deque

from algorithms.base import PageReplacementAlgorithm
from controllers.events import SimulationEvent


class FCFS(PageReplacementAlgorithm):

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.frames = []
        self.queue = deque()

    def access(self, page: int) -> SimulationEvent:

        # Hit
        if page in self.frames:
            return SimulationEvent(
                algorithm="FIFO",
                page=page,
                page_fault=False,
                removed_page=None,
                frames=self.frames.copy()
            )

        removed = None

        # Memória cheia
        if len(self.frames) >= self.capacity:

            removed = self.queue.popleft()

            self.frames.remove(removed)

        self.frames.append(page)
        self.queue.append(page)

        return SimulationEvent(
            algorithm="FIFO",
            page=page,
            page_fault=True,
            removed_page=removed,
            frames=self.frames.copy()
        )

    def get_frames(self) -> list[int]:
        return self.frames.copy()