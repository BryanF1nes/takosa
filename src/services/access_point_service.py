from models.access_point import AccessPoint


class AccessPointService:
    def __init__(self, access_points: list[AccessPoint]):
        self.access_points = access_points

    def validate(self):
        invalid = []

        for ap in self.access_points:
            if (
                not ap.switch_name
                or not ap.access_point
                or ap.frequency not in (2.4, 5)
            ):
                invalid.append(ap)

        return invalid

    def summary(self):
        return {
            "total": len(self.access_points),
            "by_switch": {
                switch: len(aps)
                for switch, aps in self.index_by_switch().items()
            },
            "by_frequency": {
                freq: len(
                    [ap for ap in self.access_points if ap.frequency == freq])
                for freq in set(ap.frequency for ap in self.access_points)
            }
        }

    def by_switch(self, switch_name: str):
        return [ap for ap in self.access_points if ap.switch_name == switch_name]

    def by_frequency(self, frequency: int):
        return [ap for ap in self.access_points if ap.frequency == frequency]

    def index_by_switch(self):
        grouped = {}
        for ap in self.access_points:
            grouped.setdefault(ap.switch_name, []).append(ap)
        return grouped

    def index_by_key(self):
        return {
            (ap.switch_name, ap.access_point): ap for ap in self.access_points
        }
