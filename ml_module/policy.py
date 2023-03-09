from ml_module.polynomial_regression import PolynomialRegression
class Policy:
    def __init__(self, context):
        self.context = context

    def configure(self, configure_criteria):
        if configure_criteria == 'polynomial':
            self.context.set_strategy(PolynomialRegression())
