from modelling.models import Model, register
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

@register
class LDA(Model.Model):
    def __init__(self) -> None:
        self.__name = 'default_LDA'
        self.__model = LinearDiscriminantAnalysis()

    def fit(self, X ,y):
        return self.__model.fit(X, y)

    def predict(self, X):
        return self.__model.predict(X)