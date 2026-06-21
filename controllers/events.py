from dataclasses import dataclass
from typing import Any

@dataclass
class SimulationEvent:
    algorithm: str
    page: int
    page_fault: bool
    removed_page: int | None
    frames: list[int]
    metadata: dict[str, Any] | None = None