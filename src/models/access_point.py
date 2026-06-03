from dataclasses import dataclass


@dataclass
class AccessPoint:
    switch_name: str
    access_point: str
    frequency: int
    frequency_hop_value: str
