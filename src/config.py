from dataclasses import dataclass


@dataclass()
class TileInfo:
    stink: bool
    wumpus: bool
    breeze: bool
    gold: bool


Floor = TileInfo(
    False,
    False,
    False,
    False,
)

"""WUMPUS = TileInfo('Wumpus', 'W', True)
HOLE = TileInfo('Hole', 'H', True)
GOLD = TileInfo('Gold', 'G', True)
"""
