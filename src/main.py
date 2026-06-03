from load_file import load_file
from services.access_point_service import AccessPointService

file_a_path = input("Enter path for File A: ")

aps_a = load_file(file_a_path)
service_a = AccessPointService(aps_a)

print(service_a)
