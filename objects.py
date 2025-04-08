from dataclasses import dataclass


@dataclass
class Coordinate:
    x: int
    y: int


@dataclass
class Point:
    pos: Coordinate


@dataclass
class Line:
    pos1: Coordinate
    pos2: Coordinate


@dataclass
class Plane:
    width: int
    height: int

    locus: set
