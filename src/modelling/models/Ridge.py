from sklearn.linear_model import Ridge as RidgeRegression
from modelling.models import Model, register

@register
class Ridge(Model.Model):
    def __init__(self) -> None:
        self.__name = 'default_Ridge'
        self.__model = RidgeRegression()
        self.__hyper_param_grid = {
            'alpha': [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0],
            'fit_intercept': [True, False]
        }
        super().__init__(self.__name, self.__model, self.__hyper_param_grid)

    def fit(self, X ,y):
        return self.__model.fit(X, y)

    def predict(self, X):
        return self.__model.predict(X)
