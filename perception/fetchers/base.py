from abc import ABC, abstractmethod


class BaseFetcher(ABC):

    @abstractmethod
    def fetch_events(self):
        pass