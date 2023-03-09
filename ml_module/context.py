class Context:
    def __init__(self):
        self.ml_strategy = None

    def predict(self, data):
        return self.ml_strategy.perform_predict(data)

    def set_strategy(self, strategy):
        self.ml_strategy=strategy
