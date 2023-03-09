import pickle
from os import path

basedir = path.abspath(path.dirname(__file__))
model = pickle.load(open(path.join(basedir, 'house_prediction.pkl'), 'rb'))


def make_prediction(data):
    if model is None:
        return 0
    return model.predict(data)
