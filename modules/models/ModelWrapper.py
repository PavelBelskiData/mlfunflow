from abc import ABC, abstractmethod

class ModelWrapper(ABC):
    def __init__(self, model):
        self._model = model

    @abstractmethod
    def predict(self, X):
        pass