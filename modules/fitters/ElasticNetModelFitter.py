class ElasticNetModelFitter(ModelFitter):
    def getModel(self, method: ElasticNet, X, y):
        model = method.fit(X, y)
        return ElasticNetModelWrapper(model)