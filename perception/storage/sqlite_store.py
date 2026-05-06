import sqlite3

from perception.models.event import SeismicEvent
from shared.logger import logger


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

    def save_event(self, event: SeismicEvent):

        cursor = self.connection.cursor()

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