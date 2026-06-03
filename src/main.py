from pathlib import Path
from pprint import pprint
from parser import load_access_points
from services.access_point_service import AccessPointService


BASE_DIR = Path(__file__).parent
input_dir = BASE_DIR / "input" / "access_points_sample.txt"

aps = load_access_points(input_dir)
service = AccessPointService(aps)
