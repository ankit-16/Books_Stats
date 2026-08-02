import json
from pathlib import Path

from pydantic import ValidationError

from books_stats.models import Book


class BookLoaderError(Exception):
    """Raised when book loading fails."""


def load_books(file_path: str | Path) -> list[Book]:
    try:
        with open(file_path, encoding="utf-8") as file:
            data = json.load(file)

        return [Book(**book_data) for book_data in data]

    except FileNotFoundError as e:
        raise BookLoaderError(
            f"Book file '{file_path}' does not exist."
        ) from e

    except json.JSONDecodeError as e:
        raise BookLoaderError(
            f"'{file_path}' is not valid JSON."
        ) from e

    except ValidationError as e:
        raise BookLoaderError(
            f"Book data in '{file_path}' failed validation."
        ) from e