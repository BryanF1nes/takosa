from services.access_point_service import AccessPointService
from models.access_point import AccessPoint

access_points = [
    AccessPoint('GRX01-A', 'AP-1', 755, 'BX01A'),
    AccessPoint('GRX22-C', 'AP-8', 680, 'GX04A'),
    AccessPoint('GRX01-A', 'AP-1', 755, 'ZCT1B'),
    AccessPoint('LO0A2-A', 'AP-1', 755, 'KXX10'),
    AccessPoint('ZHR05-A', 'AP-1', 755, 'MX02A'),
]


def service_by_ap_index():
    access_point_service = AccessPointService(access_points)

    return access_point_service.by_ap_index


def service_by_hop_index():
    access_point_service = AccessPointService(access_points)

    return access_point_service.by_hop_index


def test_answer():
    assert service_by_ap_index() == {
        'AP-1': [AccessPoint(switch_name='GRX01-A', access_point='AP-1', frequency=755, frequency_hop_value='BX01A'),
                 AccessPoint(switch_name='GRX01-A', access_point='AP-1', frequency=755, frequency_hop_value='ZCT1B'),
                 AccessPoint(switch_name='LO0A2-A', access_point='AP-1', frequency=755, frequency_hop_value='KXX10'),
                 AccessPoint(switch_name='ZHR05-A', access_point='AP-1', frequency=755, frequency_hop_value='MX02A')],
        'AP-8': [AccessPoint(switch_name='GRX22-C', access_point='AP-8', frequency=680, frequency_hop_value='GX04A')]
    }

    assert service_by_hop_index() == {
        'BX01A': [AccessPoint(switch_name='GRX01-A', access_point='AP-1', frequency=755, frequency_hop_value='BX01A')],
        'GX04A': [AccessPoint(switch_name='GRX22-C', access_point='AP-8', frequency=680, frequency_hop_value='GX04A')],
        'KXX10': [AccessPoint(switch_name='LO0A2-A', access_point='AP-1', frequency=755, frequency_hop_value='KXX10')],
        'MX02A': [AccessPoint(switch_name='ZHR05-A', access_point='AP-1', frequency=755, frequency_hop_value='MX02A')],
        'ZCT1B': [AccessPoint(switch_name='GRX01-A', access_point='AP-1', frequency=755, frequency_hop_value='ZCT1B')]
    }
