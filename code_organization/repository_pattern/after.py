import contextlib
import sqlite3
from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class Post:
    id: int
    title: str
    content: str


class Repository(ABC):
    @abstractmethod
    def get(self, id: int) -> Any:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> list[Any]:
        raise NotImplementedError

    @abstractmethod
    def add(self, **kwargs: object) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self, id: int, **kwargs: object) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: int) -> None:
        raise NotImplementedError


class PostRepository(Repository):
    def __init__(self, db_path: str) -> None:
        self.db_path = db_path
        self.create_table()

    @contextlib.contextmanager
    def connect(self):
        with sqlite3.connect(self.db_path) as conn:
            yield conn.cursor()

    def create_table(self) -> None:
        with self.connect() as cursor:
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS posts (id INTERGER PRIMARY KEY, title TEXT, content TEXT)"
            )

    def get(self, id: int) -> Any:
        with self.connect() as cursor:
            cursor.execute("SELECT * FROM posts WHERE id=?", (id,))
            post = cursor.fetchone()
            if post is None:
                raise ValueError(f"Post with id {id} does not exists")

            return Post(*post)

    def get_all(self) -> list[Any]:
        with self.connect() as cursor:
            cursor.execute("SELECT * FROM posts")

            return [Post(*post) for post in cursor.fetchall()]

    def add(self, **kwargs: object) -> None:
        if "title" in kwargs and "content" in kwargs:
            with self.connect() as cursor:
                cursor.execute(
                    "INSERT INTO posts (title, content) VALUES (?, ?)",
                    (kwargs["title"], kwargs["content"]),
                )

            return
        raise ValueError("Must provide title and content")

    def update(self, id: int, **kwargs: object) -> None:
        return None

    def delete(self, id: int) -> None:
        with self.connect() as cursor:
            cursor.execute("DELETE FROM posts WHERE id=?", (id))


def main() -> None:
    PATH = Path().absolute()
    FOLDER_PATH = PATH / "code_organization" / "repository_pattern"
    DB_PATH = str(FOLDER_PATH / "posts.db")

    repo = PostRepository(db_path=DB_PATH)

    repo.add(title="Hello", content="World")
    repo.add(title="Foo", content="Bar")
    print(repo.get_all())
    repo.delete(1)
    print(repo.get_all())


if __name__ == "__main__":
    main()
