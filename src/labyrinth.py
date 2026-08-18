from src.config import Floor
from dataclasses import dataclass


class Labyrinth:
    def limites(self, x: int, y: int) -> bool:
        return 0 <= x < 4 and 0 <= y < 4
