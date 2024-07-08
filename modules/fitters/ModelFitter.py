from abc import ABC, abstractmethod

class ModelFitter(ABC):
    @abstractmethod
    def getModel(self, model) -> ModelWrapper:
        pass