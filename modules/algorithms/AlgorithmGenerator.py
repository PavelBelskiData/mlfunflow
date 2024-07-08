from abc import ABC, abstractmethod

class AlgorithmGenerator(ABC):
    @abstractmethod
    def getAlgorithm(self):
        pass