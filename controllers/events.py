from dataclasses import dataclass

@dataclass
class SimulationEvent:
    page: int
    page_fault: bool
    removed_page: int | None
    frames: list[int]