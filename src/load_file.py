from pathlib import Path
from parser import load_access_points
from models.access_point import AccessPoint


def load_file(file_path: str) -> list[AccessPoint]:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"{file_path} does not exist")

    return load_access_points(path)
