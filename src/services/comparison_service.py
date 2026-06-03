from models.access_point import AccessPoint
from models.comparison_result import ComparisonResult


class ComparisonService:
    def __init__(self, file1_data: list[AccessPoint], file2_data: list[AccessPoint]):
        self.file1_data = file1_data
        self.file2_data = file2_data

        self.file1_index = self._build_index(file1_data)
        self.file2_index = self._build_index(file2_data)

    def _build_index(self, data: list[AccessPoint]) -> dict:
        index = {}

        for ap in data:
            index[ap.access_point] = ap

        return index

    def _format(self, ap: AccessPoint) -> str:
        return (
            f"Switch={ap.switch_name}, "
            f"Access_Point={ap.access_point}, "
            f"Frequency={ap.frequency}, "
            f"Hop_Value={ap.frequency_hop_value}"
        )

    def _get_mismatches(self, ap1: AccessPoint, ap2: AccessPoint) -> list[str]:
        mismatches = []

        if ap1.switch_name != ap2.switch_name:
            mismatches.append("switch_name")

        if ap1.frequency != ap2.frequency:
            mismatches.append("frequency")

        if ap1.frequency_hop_value != ap2.frequency_hop_value:
            mismatches.append("frequency_hop_value")

        return mismatches

    def compare(self, search_values: list[str]) -> list[ComparisonResult]:
        results = []

        for value in search_values:
            ap1 = self.file1_index.get(value)
            ap2 = self.file2_index.get(value)

            # CASE 1: exists in both files
            if ap1 and ap2:
                mismatch_fields = self._get_mismatches(ap1, ap2)

                status = "MATCH" if not mismatch_fields else "MISMATCH"

                results.append(
                    ComparisonResult(
                        search_value=value,
                        file1_value=self._format(ap1),
                        file2_value=self._format(ap2),
                        status=status,
                        mismatch_fields=mismatch_fields,
                    )
                )

            # CASE 2: only in file 1
            elif ap1 and not ap2:
                results.append(
                    ComparisonResult(
                        search_value=value,
                        file1_value=self._format(ap1),
                        file2_value=None,
                        status="MISSING_FILE2",
                        mismatch_fields=[],
                    )
                )

            # CASE 3: only in file 2
            elif ap2 and not ap1:
                results.append(
                    ComparisonResult(
                        search_value=value,
                        file1_value=None,
                        file2_value=self._format(ap2),
                        status="MISSING_FILE1",
                        mismatch_fields=[],
                    )
                )

            # CASE 4: not found anywhere
            else:
                results.append(
                    ComparisonResult(
                        search_value=value,
                        file1_value=None,
                        file2_value=None,
                        status="NOT_FOUND",
                        mismatch_fields=[],
                    )
                )

        return results
