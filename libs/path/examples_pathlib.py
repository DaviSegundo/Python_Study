from os import chdir
from pathlib import Path


def main() -> None:
    print(f"Current working directory: {Path.cwd()}")
    print(f"Home directory: {Path.home()}")

    path = Path.cwd() / "libs" / "path" / "settings.yaml"
    print(path.exists())

    print(path.read_text())

    with path.open() as file:
        print(file.read())

    resolve_path = Path("settings.yaml")
    print(resolve_path.resolve())
    print(f"Parent: {path.parent}")

    new_file = path.parent / "new_file.txt"
    new_file.touch()
    new_file.write_text("Davi")

    new_file.unlink()


if __name__ == "__main__":
    main()
