from abc import ABC
from abc import abstractmethod


class BaseUpdater(ABC):

    @abstractmethod
    def update(self, *args, **kwargs):

        pass