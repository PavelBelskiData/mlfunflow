from modules.fitters.ModelFitter import ModelFitter
from sklearn.linear_model import ElasticNet
from modules.models.ElasticNetModelWrapper import ElasticNetModelWrapper

class ElasticNetModelFitter(ModelFitter):
    def getModel(self, method: ElasticNet, X, y):
        model = method.fit(X, y)
        return ElasticNetModelWrapper(model)