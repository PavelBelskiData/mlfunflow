from sklearn.linear_model import ElasticNet
from modules.algorithms import AlgorithmGenerator

class ElasticNetAlgorithmGenerator(AlgorithmGenerator):
    def getAlgorithm(self, alpha=0.5, l1_ratio=0.5):
        return ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)