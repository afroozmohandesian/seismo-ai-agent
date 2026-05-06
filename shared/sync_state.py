import json
from pathlib import Path


STATE_FILE = Path("sync_state.json")


class SyncStateManager:

    def __init__(self):

        if not STATE_FILE.exists():

            self.save_last_event_time(0)

    def get_last_event_time(self) -> int:

        with open(STATE_FILE, "r") as file:

            state = json.load(file)

        return state["last_event_time"]

    def save_last_event_time(self, timestamp: int):

        with open(STATE_FILE, "w") as file:

            json.dump(
                {
                    "last_event_time": timestamp
                },
                file,
                indent=2,
            )