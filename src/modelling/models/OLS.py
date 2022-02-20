from modelling.models import register, Model
from sklearn.linear_model import LinearRegression

@register
class OLS(Model.Model):
    def __init__(self) -> None:
        self.__name = 'default_OLS'
        self.__model = LinearRegression()

    def fit(self, X ,y):
        return self.__model.fit(X, y)

    def predict(self, X):
        return self.__model.predict(X)
