import pickle
from os import path

basedir = path.abspath(path.dirname(__file__))
model = pickle.load(open(path.join(basedir, '../ml_module/house_prediction.pkl'), 'rb'))


def make_prediction(data):
    if model is None:
        return
    return model.predict(data)
