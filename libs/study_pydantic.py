import json
import pydantic
from typing import Optional, List


class ISBN10FormatError(Exception):
    """Custom error that is raised when ISBN10 doesnt have the right format"""

    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)


class ISBNMissingError(Exception):
    """Custom error that is raised when both ISBN10 and ISBN13 are missing"""

    def __init__(self, title: str, message: str) -> None:
        self.title = title
        self.message = message
        super().__init__(message)


class Book(pydantic.BaseModel):
    title: str
    author: str
    publisher: str
    price: float
    isbn_10: Optional[str]
    isbn_13: Optional[str]
    subtitle: Optional[str]

    class Config:
        """Pydantic config class"""

        allow_mutation = False
        anystr_lower = True

    @pydantic.root_validator(pre=True)
    @classmethod
    def check_isbn10_or_isbn13(cls, values):
        """Make sure there is either an isbn10 or isbn13 value defined."""

        if "isbn_10" not in values and "isbn_13" not in values:
            raise ISBNMissingError(
                value=values["title"], message="Document should have either an ISBN10 or ISBN13.")
        return values

    @pydantic.validator("isbn_10")
    @classmethod
    def isbn_10_valid(cls, value):
        """Validator to check whether ISBN10 has a valid value."""

        chars = [c for c in value if c in '0123456789Xx']
        if len(chars) != 10:
            raise ISBN10FormatError(
                value=value, message="ISBN10 should be 10 digits.")

        def char_to_int(char: str) -> int:
            if char in 'Xx':
                return 10
            return int(char)

        weighted_sum = sum((10-i) * char_to_int(x)
                           for i, x in enumerate(chars))
        if weighted_sum % 11 != 0:
            raise ISBN10FormatError(
                value=value, message="ISBN10 digit sum should be divisible by 11.")

        return value


def main() -> None:
    """Load data from json and create list of books"""
    with open('libs/data.json') as file:
        data: List[dict] = json.load(file)
        books_valid: List[Book] = []
        books_invalid: List[Book] = []

        for book in data:
            try:
                book_valid = Book(**book)
                books_valid.append(book_valid)
            except ISBN10FormatError or ISBNMissingError:
                books_invalid.append(book)

        print(books_valid)
        print()
        print(books_invalid)


if __name__ == '__main__':
    main()
