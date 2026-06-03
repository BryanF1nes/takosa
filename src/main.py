import sys
from pathlib import Path

from parser import load_access_points
from services.search_service import SearchService
from services.comparison_service import ComparisonService
from services.excel_exporter import ExcelExporter


def main():
    args = sys.argv

    if len(args) not in (4, 5):
        print("Usage:")
        print("  python main.py <file1> <file2> <output.xlsx>")
        print("  python main.py <file1> <file2> <search.txt> <output.xlsx>")
        sys.exit(1)

    file1_path = Path(args[1])
    file2_path = Path(args[2])

    if len(args) == 4:
        search_file_path = None
        output_path = Path(args[3])
    else:
        search_file_path = Path(args[3])
        output_path = Path(args[4])

    for path in [file1_path, file2_path]:
        if not path.exists():
            print(f"File not found: {path}")
            sys.exit(1)

    if search_file_path and not search_file_path.exists():
        print(f"Search file not found: {search_file_path}")
        sys.exit(1)

    file1_data = load_access_points(file1_path)
    file2_data = load_access_points(file2_path)

    if search_file_path:
        with open(search_file_path, "r") as f:
            raw_search_values = [
                line.strip()
                for line in f
                if line.strip()
            ]
    else:
        # fallback: union of both datasets
        raw_search_values = list({
            ap.access_point
            for ap in (file1_data + file2_data)
        })

    search_service = SearchService(raw_search_values)
    search_values = search_service.get_clean_search_values()

    comparison_service = ComparisonService(file1_data, file2_data)
    results = comparison_service.compare(search_values)

    print(f"Search values: {len(search_values)}")
    print(f"File1 records: {len(file1_data)}")
    print(f"File2 records: {len(file2_data)}")
    print(f"Results: {len(results)}")

    ExcelExporter(results).export(str(output_path))

    print(f"Report generated successfully: {output_path}")


if __name__ == "__main__":
    main()
