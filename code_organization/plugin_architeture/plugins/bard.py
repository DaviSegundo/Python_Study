"""
Game extension thats adds a bard character.
"""

from dataclasses import dataclass
from game import factory

@dataclass
class Bard:

    name: str

    def make_a_noise(self) -> None:
        print("Toss a coin to your Witcher!")


def initialize() -> None:
    factory.register("bard", Bard)