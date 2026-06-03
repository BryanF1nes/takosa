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

    def by_access_point(self, access_point: str):
        result = []

        for ap in self.access_points:
            if ap.access_point == access_point:
                result.append(ap)

        return result

    def by_hop_value(self, hop_value: str):
        result = []

        for ap in self.access_points:
            if ap.frequency_hop_value == hop_value:
                result.append(ap)

        return result
