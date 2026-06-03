from models.access_point import AccessPoint


class AccessPointService:
    def __init__(self, access_points: list[AccessPoint]):
        self.access_points = access_points

    def by_switch(self, switch_name: str):
        result = []

        for ap in self.access_points:
            if ap.switch_name == switch_name:
                result.append(ap)

        return result

    def by_frequency(self, frequency: int):
        result = []

        for ap in self.access_points:
            if ap.frequency == frequency:
                result.append(ap)

        return result

    def index_by_switch(self):
        grouped = {}

        for ap in self.access_points:
            if ap.switch_name not in grouped:
                grouped[ap.switch_name] = []

            grouped[ap.switch_name].append(ap)

        return grouped

    def index_by_key(self):
        result = {}

        for ap in self.access_points:
            key = (ap.switch_name, ap.access_point)
            result[key] = ap

        return result
