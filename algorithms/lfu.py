from algorithms.base import PageReplacementAlgorithm
from controllers.events import SimulationEvent


class LFU(PageReplacementAlgorithm):

    def __init__(self, capacity: int):
        self.capacity = capacity

        self.frames = []

        # frequência de acesso
        self.frequency = {}

        # ordem de chegada (para desempate)
        self.arrival_order = []

    def access(self, page: int) -> SimulationEvent:

        # Hit
        if page in self.frames:

            self.frequency[page] += 1

            return SimulationEvent(
                algorithm="LFU",
                page=page,
                page_fault=False,
                removed_page=None,
                frames=self.frames.copy(),
                metadata={"frequency": self.frequency.copy()}
            )

        removed = None

        # Memória cheia
        if len(self.frames) >= self.capacity:

            min_freq = min(
                self.frequency[p]
                for p in self.frames
            )

            candidates = [
                p for p in self.arrival_order
                if p in self.frames
                and self.frequency[p] == min_freq
            ]

            removed = candidates[0]

            self.frames.remove(removed)
            self.arrival_order.remove(removed)

            del self.frequency[removed]

        self.frames.append(page)
        self.arrival_order.append(page)

        self.frequency[page] = 1

        return SimulationEvent(
            algorithm="LFU",
            page=page,
            page_fault=True,
            removed_page=removed,
            frames=self.frames.copy(),
            metadata={"frequency": self.frequency.copy()}
        )

    def get_frames(self) -> list[int]:
        return self.frames.copy()