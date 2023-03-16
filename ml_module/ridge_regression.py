import pickle
from os import path
from ml_module.ml_strategy import MLStrategy


class RidgeRegression(MLStrategy):
    def __init__(self):
        self.model = None
        basedir = path.abspath(path.dirname(__file__))
        model_name = 'house_prediction.pkl'
        self.load_model(basedir, model_name)

    def load_model(self, model_path, model_name):
        self.model = pickle.load(open(path.join(model_path, model_name), mode='rb'))

    def perform_predict(self, data):
        return self.model.predict(data)
