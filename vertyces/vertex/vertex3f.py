from dataclasses import dataclass


@dataclass
class Vertex3f:
    _x: float
    _y: float
    _z: float

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Vertex3f):
            return self._x == other._x and self._y == other._y and self._z == other._z
        return False

    def __hash__(self) -> int:
        return hash((self._x, self._y, self._z))

    def clone(self) -> "Vertex3f":
        return Vertex3f(self._x, self._y, self._z)

    def translated(self, v: "Vertex3f") -> "Vertex3f":
        return Vertex3f(self._x + v._x, self._y + v._y, self._z + v._z)

    def multiplied(self, mult: float) -> "Vertex3f":
        return Vertex3f(self._x * mult, self._y * mult, self._z * mult)

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @property
    def z(self) -> float:
        return self._z

    @property
    def norm(self) -> float:
        return float((self._x**2 + self._y**2 + self._z**2) ** 0.5)

    @property
    def unit_vertex(self) -> "Vertex3f":
        if norm := self.norm != 0:
            return self.multiplied(1 / self.norm)
        return Vertex3f(0, 0, 0)
