from models.access_point import AccessPoint


class AccessPointService:
    def __init__(self, access_points: list[AccessPoint]):
        self.access_points = access_points

        self.by_switch_index = {}
        self.by_ap_index = {}
        self.by_hop_index = {}

        self._build_indexes()

    def _build_indexes(self):
        for ap in self.access_points:
            self.by_switch_index.setdefault(ap.switch_name, []).append(ap)
            self.by_ap_index.setdefault(ap.access_point, []).append(ap)
            self.by_hop_index.setdefault(ap.frequency_hop_value, []).append(ap)

    def by_switch(self, switch_name: str):
        return self.by_switch_index.get(switch_name, [])

    def by_access_point(self, access_point: str):
        return self.by_ap_index.get(access_point, [])

    def by_hop_value(self, hop_value: str):
        return self.by_hop_index.get(hop_value, [])
