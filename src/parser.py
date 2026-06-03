from models.access_point import AccessPoint


def load_access_points(file_path: str) -> list[AccessPoint]:
    access_points = []

    with open(file_path, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    for i in range(0, len(lines), 4):
        switch_name = lines[i]
        access_point = lines[i + 1]

        frequency_line = lines[i + 2]
        frequency = int(
            ''.join(char for char in frequency_line if char.isdigit())
        )

        hop_value = (
            lines[i + 3]
            .replace("Frequency Hop Value:", "")
            .strip()
        )

        access_points.append(
            AccessPoint(
                switch_name=switch_name,
                access_point=access_point,
                frequency=frequency,
                frequency_hop_value=hop_value
            )
        )

    return access_points
