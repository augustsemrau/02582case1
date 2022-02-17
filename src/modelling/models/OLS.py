import os
import pickle as pkl
from modelling.models import register
from sklearn.linear_model import LinearRegression

@register
class OLS(LinearRegression):
    def __init__(self) -> None:
        self.__name = 'default_OLS'

    def get_name(self):
        return self.__name

    def set_name(self, name:str):
        ending = name[-4:]
        self.__name = name[:-4] if ending == '.pkl' else name

    def save(self):
        file_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(file_dir, 'model_store', f'{self.__name}.pkl'), 'wb') as file:
            pkl.dump(self, file)