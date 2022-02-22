from modelling.models import Model, register
from sklearn.neighbors import KNeighborsRegressor

@register
class KNN(Model.Model):
    def __init__(self) -> None:
        self.__name = 'default_KNN'
        self.__model = KNeighborsRegressor()
        self.__hyper_param_grid = {
            'n_neighbors': [1,2,5,7,10,15,20],
            # 'weights': ['uniform', 'distance'],
            # 'algorithm': ['ball_tree', 'kd_tree'],
            # 'leaf_size': [20, 25, 30, 35, 40, 50, 60]
        }
        super().__init__(self.__name, self.__model, self.__hyper_param_grid)

    def fit(self, X ,y):
        return self.__model.fit(X, y)

    def predict(self, X):
        return self.__model.predict(X)
