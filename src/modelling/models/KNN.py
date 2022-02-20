from modelling.models import Model, register
from sklearn.neighbors import KNeighborsRegressor

@register
class KNN(Model.Model):
    def __init__(self) -> None:
        self.__name = 'default_KNN'
        self.__model = KNeighborsRegressor()

    def fit(self, X ,y):
        return self.__model.fit(X, y)

    def predict(self, X):
        return self.__model.predict(X)