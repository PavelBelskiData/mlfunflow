class ElasticNetModelWrapper(ModelWrapper):
    def __init__(self, model):
        super().__init__(model)
        
    def predict(self, X):
        return self._model.predict(X)