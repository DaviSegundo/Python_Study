from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Vector:
    x: float
    y: float

    def __truediv__(self, other: float) -> Vector:
        return Vector(self.x / other, self.y / other)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)


def main() -> None:
    point = Vector(1, 2)
    print(point / 2)
    print(point + point)


if __name__ == "__main__":
    main()
