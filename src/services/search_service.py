from typing import Iterable


class SearchService:
    def __init__(self, raw_search_values: Iterable[str]):
        self.raw_search_values = raw_search_values

    def get_clean_search_values(self) -> list[str]:
        seen = set()
        cleaned = []

        for value in self.raw_search_values:
            if value is None:
                continue

            value = value.strip()

            if not value:
                continue

            if value in seen:
                continue

            seen.add(value)
            cleaned.append(value)

        return cleaned
