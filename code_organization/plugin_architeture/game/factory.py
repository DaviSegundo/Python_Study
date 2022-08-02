from typing import Any, Callable, Dict
from .character import GameCharacter


character_creation_functions: Dict[str, Callable[..., GameCharacter]] = {}

def register(character_type: str, creation_func: Callable[..., GameCharacter]):
    """Register a new game character type.

    Args:
        character_type (str): type of the character
        creation_func (Callable[..., GameCharacter]): function thats create the character
    """

    character_creation_functions[character_type] = creation_func

def unregister(character_type: str):
    """Unregister a game character type.

    Args:
        character_type (str): type of the character
    """

    character_creation_functions.pop(character_type, None)

def create(arguments: Dict[str, Any]) -> GameCharacter:
    """Create a game character of a specific type, given a dictionary of arguments.

    Args:
        arguments (Dict[str, Any]): informations about how to create the character

    Returns:
        GameCharacter: a character for the game
    """

    args_copy = arguments.copy()
    character_type = args_copy.pop("type")
    try:
        create_func = character_creation_functions[character_type]
        return create_func(**args_copy)
    except KeyError:
        raise ValueError(f"Unknown character type {character_type!r}")