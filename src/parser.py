from models.access_point import AccessPoint
import re


def parse_frequency(line: str) -> int:
    match = re.search(r"\d+", line)
    return int(match.group()) if match else 0


def parse_hop_value(line: str) -> str:
    return line.replace("Frequency Hop Value:", "").strip()


def load_access_points(file_path: str) -> list[AccessPoint]:
    access_points = []

    with open(file_path, "r") as f:
        raw_lines = [line.rstrip("\n") for line in f]

    lines = [line.strip() for line in raw_lines if line.strip()]

    i = 0
    while i + 3 < len(lines):
        switch_name = lines[i]
        access_point = lines[i + 1]
        frequency_line = lines[i + 2]
        hop_line = lines[i + 3]

        frequency = int(''.join(c for c in frequency_line if c.isdigit()))
        hop_value = hop_line.replace("Frequency Hop Value:", "").strip()

        access_points.append(
            AccessPoint(
                switch_name=switch_name,
                access_point=access_point,
                frequency=frequency,
                frequency_hop_value=hop_value
            )
        )

        i += 4

    return access_points
