from sklearn.linear_model import Ridge
from modelling.models import Model, register

@register
class Ridge(Model):
    def __init__(self) -> None:
        self.__name = 'default_Ridge'
        self.__model = Ridge()

    def fit(self, X ,y):
        return self.__model.fit(X, y)

    def predict(self, X):
        return self.__model.predict(X)