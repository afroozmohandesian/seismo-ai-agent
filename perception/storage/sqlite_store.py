import sqlite3

from perception.models.event import SeismicEvent
from shared.logger import logger
from perception.deduplication import (
    are_potential_duplicates,
)


class SQLiteStore:

    def __init__(self, db_path: str = "seismic_events.db"):

        self.connection = sqlite3.connect(db_path)

        self.create_table()

    def create_table(self):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS events (

                eid TEXT,
                timestamp TEXT,

                lat REAL,
                lon REAL,

                depth REAL,

                Mw REAL,

                PRIMARY KEY (eid, timestamp)
            )
            """
        )

        self.connection.commit()

    def fetch_existing_events(self):

        cursor = self.connection.cursor()

        rows = cursor.execute(
            """
            SELECT
                eid,
                timestamp,
                lat,
                lon,
                depth,
                Mw
            FROM events
            """
        ).fetchall()

        events = []

        for row in rows:

            event = SeismicEvent(
                eid=row[0],
                timestamp=row[1],
                lat=row[2],
                lon=row[3],
                depth=row[4],
                Mw=row[5],
                dist=0.0,
                azi=0.0,
                loclat=row[2],
                loclon=row[3],
            )

            events.append(event)

        return events

    def save_event(self, event: SeismicEvent):

        cursor = self.connection.cursor()
        
        existing_events = (
            self.fetch_existing_events()
        )

        for existing_event in existing_events:

            if are_potential_duplicates(
                event,
                existing_event,
            ):

                logger.warning(
                    "Scientific duplicate detected"
                )

                return

        try:

            cursor.execute(
                """
                INSERT INTO events (
                    eid,
                    timestamp,
                    lat,
                    lon,
                    depth,
                    Mw
                )
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    event.eid,
                    event.timestamp.isoformat(),
                    event.lat,
                    event.lon,
                    event.depth,
                    event.Mw,
                ),
            )

            self.connection.commit()

            logger.info(
                f"Stored event {event.eid}"
            )

        except sqlite3.IntegrityError:

            logger.warning(
                f"Duplicate event skipped: "
                f"{event.eid}"
            )