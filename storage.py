import json
from pathlib import Path
from typing import Any

FILE_PATH = Path(__file__).parent / "students.json"


def read_students() -> list[dict[str, Any]]:
    """Read all students from the JSON file."""

    if not FILE_PATH.exists():
        return []

    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def write_students(students: list[dict[str, Any]]) -> None:
    """Write students to the JSON file."""

    with open(FILE_PATH, "w") as file:
        json.dump(students, file, indent=4)