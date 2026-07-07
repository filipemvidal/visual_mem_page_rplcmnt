from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class SimulationEvent:
    algorithm: str
    page: int
    page_fault: bool
    removed_page: int | None
    frames: list[int]
    metadata: dict[str, Any] | None = None

@dataclass
class ViewSimCell():
    page: int
    detail: str

@dataclass
class ViewSimulationEvent():
    page: str | None
    frames: list[ViewSimCell]
    page_fault: bool