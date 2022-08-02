"""
Basic example showing how to create objects from data using a dynamic factory with
register/unregister methods.
"""

import json
from dataclasses import dataclass

from game import factory
from plugins import loader

@dataclass
class Sorcerer:

    name: str

    def make_a_noise(self) -> None:
        print("Aaaargh!")


@dataclass
class Wizard:

    name: str

    def make_a_noise(self) -> None:
        print("Boohh!")


@dataclass
class Witcher:

    name: str

    def make_a_noise(self) -> None:
        print("Hmmm!")


def main():
    """Creates game characters from a file containg a level definition.
    """

    # register a couple of character types
    factory.register("sorcerer", Sorcerer)
    factory.register("witcher", Witcher)
    factory.register("wizard", Wizard)

    # read data from a JSON file
    with open("code_organization\plugin_architeture\level_with_plugins.json") as file:
        data = json.load(file)

        # load the plugins
        loader.load_plugins(data["plugins"])

        # create the characters
        characters = [factory.create(item) for item in data["characters"]]
                
        # do something with the characters
        for character in characters:
            print(character, end="\t")
            character.make_a_noise()


if __name__ == '__main__':
    main()
