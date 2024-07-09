from abc import ABC, abstractmethod
from modules.models.ModelWrapper import ModelWrapper

class ModelFitter(ABC):
    @abstractmethod
    def getModel(self, model) -> ModelWrapper:
        pass