from typing import List

from vertyces.vertex.vertex2f import Vertex2f


class Rectangle:
    _p1: Vertex2f
    _dimensions: Vertex2f

    _p2: Vertex2f

    def __init__(self, position: Vertex2f, dimensions: Vertex2f) -> None:
        self._p1 = position.clone()
        self._p2 = position.translated(dimensions)
        self._dimensions = dimensions.clone()

    @staticmethod
    def from_points(p1: Vertex2f, p2: Vertex2f) -> "Rectangle":
        return Rectangle(p1, p2.translated(p1.inverted()))

    def get_all_points(self) -> List[Vertex2f]:
        return [
            self._p1.clone(),
            self._p1.translated(Vertex2f(self._dimensions.x, 0)),
            self._p2.clone(),
            self._p1.translated(Vertex2f(0, self._dimensions.y)),
        ]

    def contains(self, point: Vertex2f, strict: bool = True) -> bool:
        if strict:
            return (
                self._p1.x <= point.x <= self._p2.x
                and self._p1.y <= point.y <= self._p2.y
            )
        return self._p1.x < point.x < self._p2.x and self._p1.y < point.y < self._p2.y

    def collides(self, rectangle: "Rectangle", strict: bool = True) -> bool:
        if self == rectangle:
            return True

        collides = False
        for point in self.get_all_points():
            collides = collides or rectangle.contains(point, strict)
        for point in rectangle.get_all_points():
            collides = collides or self.contains(point, strict)
        return collides

    def translated(self, v: Vertex2f) -> "Rectangle":
        return Rectangle(self._p1.translated(v), self._dimensions)

    def at_position(self, position: Vertex2f) -> "Rectangle":
        return Rectangle(position, self._dimensions)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Rectangle):
            return self._p1 == other._p1 and self._p2 == other._p2
        return False

    @property
    def position(self) -> Vertex2f:
        return self._p1.clone()

    @property
    def dimensions(self) -> Vertex2f:
        return self._dimensions.clone()
