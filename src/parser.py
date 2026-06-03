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
        lines = [line.strip() for line in f if line.strip()]

    for i in range(0, len(lines), 4):
        chunk = lines[i:i + 4]

        if len(chunk) < 4:
            continue

        switch_name = chunk[0]
        access_point = chunk[1]
        frequency_line = chunk[2]
        hop_line = chunk[3]

        frequency = parse_frequency(frequency_line)
        hop_value = parse_hop_value(hop_line)

        access_points.append(
            AccessPoint(
                switch_name=switch_name,
                access_point=access_point,
                frequency=frequency,
                frequency_hop_value=hop_value
            )
        )

        return access_points
