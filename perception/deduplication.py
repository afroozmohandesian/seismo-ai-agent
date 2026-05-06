from math import radians
from math import sin
from math import cos
from math import sqrt
from math import atan2

from perception.models.event import (
    SeismicEvent,
)


EARTH_RADIUS_KM = 6371


def haversine_distance_km(
    lat1,
    lon1,
    lat2,
    lon2,
):

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1))
        * cos(radians(lat2))
        * sin(dlon / 2) ** 2
    )

    c = 2 * atan2(
        sqrt(a),
        sqrt(1 - a),
    )

    return EARTH_RADIUS_KM * c


def are_potential_duplicates(
    event_a: SeismicEvent,
    event_b: SeismicEvent,
) -> bool:

    time_difference = abs(
        (
            event_a.timestamp
            - event_b.timestamp
        ).total_seconds()
    )

    spatial_distance = (
        haversine_distance_km(
            event_a.lat,
            event_a.lon,
            event_b.lat,
            event_b.lon,
        )
    )

    magnitude_difference = abs(
        event_a.Mw - event_b.Mw
    )

    return (
        time_difference <= 8
        and spatial_distance <= 8
        and magnitude_difference <= 0.7
    )