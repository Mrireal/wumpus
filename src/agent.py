import dataclass
import auto

coordenadas = tuple[int, int]


class Move:
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()


@dataclass
class agente:
    posicion: coordenadas

    def MovimientoAgente(self, movimiento: Move) -> None:
        x, y = self.posicion
        if movimiento == Move.UP:
            self.posicion = (x, y - 1)
        elif movimiento == Move.DOWN:
            self.posicion = (x, y + 1)
        elif movimiento == Move.LEFT:
            self.posicion = (x - 1, y)
        elif movimiento == Move.RIGHT:
            self.posicion = (x + 1, y)
