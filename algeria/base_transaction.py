from abc import ABC, abstractmethod

class BaseTransaction(ABC):
    @abstractmethod
    def calculate_fees(self)-> float:
        pass