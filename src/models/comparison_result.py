from dataclasses import dataclass
from typing import Optional


@dataclass
class ComparisonResult:
    search_value: str

    file1_value: Optional[str]
    file2_value: Optional[str]

    status: str

    mismatch_fields: list[str]
