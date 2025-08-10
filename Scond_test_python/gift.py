from abc import ABC, abstractmethod

class GiftAble(ABC):
    @abstractmethod
    def give_gift(self):
        pass


