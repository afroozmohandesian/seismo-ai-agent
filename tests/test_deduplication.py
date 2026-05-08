from datetime import datetime
from datetime import timezone

from perception.deduplication import (
    haversine_distance_km,
    are_potential_duplicates,
)

from perception.models.event import (
    SeismicEvent,
)


def test_haversine_distance():

    distance = haversine_distance_km(
        0,
        0,
        0,
        1,
    )

    assert distance > 100
    assert distance < 120


def test_scientific_duplicate_detection():

    event_a = SeismicEvent(
        eid="a",
        timestamp=datetime.now(
            timezone.utc
        ),
        lat=10.0,
        lon=20.0,
        depth=-5.0,
        Mw=4.5,
        dist=0.0,
        azi=0.0,
        loclat=10.0,
        loclon=20.0,
    )

    event_b = SeismicEvent(
        eid="b",
        timestamp=datetime.now(
            timezone.utc
        ),
        lat=10.01,
        lon=20.01,
        depth=-5.2,
        Mw=4.6,
        dist=0.0,
        azi=0.0,
        loclat=10.01,
        loclon=20.01,
    )

    assert are_potential_duplicates(
        event_a,
        event_b,
    )