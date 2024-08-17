from dataclasses import dataclass


@dataclass
class Vertex2f:
    _x: float
    _y: float

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Vertex2f):
            return self._x == other._x and self._y == other._y
        return False

    def __hash__(self) -> int:
        return hash((self._x, self._y))

    def clone(self) -> "Vertex2f":
        return Vertex2f(self._x, self._y)

    def translated(self, v: "Vertex2f") -> "Vertex2f":
        return Vertex2f(self._x + v._x, self._y + v._y)

    def multiplied(self, mult: float) -> "Vertex2f":
        return Vertex2f(self._x * mult, self._y * mult)

    def divided(self, div: float, floor: bool = False) -> "Vertex2f":
        if floor:
            return Vertex2f(self._x // div, self._y // div)
        return Vertex2f(self._x / div, self._y / div)

    def inverted(self) -> "Vertex2f":
        return Vertex2f(-self._x, -self._y)

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @property
    def norm(self) -> float:
        return float((self._x**2 + self._y**2) ** 0.5)

    @property
    def unit_vertex(self) -> "Vertex2f":
        if norm := self.norm != 0:
            return self.multiplied(1 / norm)
        return Vertex2f(0, 0)
