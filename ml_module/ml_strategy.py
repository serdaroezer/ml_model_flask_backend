from abc import ABCMeta, abstractmethod


class MLStrategy(metaclass=ABCMeta):
    @abstractmethod
    def perform_predict(self, data):
        pass

    @abstractmethod
    def load_model(self, model_path, model_name):
        pass
