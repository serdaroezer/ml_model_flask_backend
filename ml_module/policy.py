from ml_module.ridge_regression import RidgeRegression
class Policy:
    def __init__(self, context):
        self.context = context

    def configure(self, configure_criteria):
        if configure_criteria == 'ridge_regression':
            self.context.set_strategy(RidgeRegression())
