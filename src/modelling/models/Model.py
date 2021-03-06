import os
import copy
import pickle as pkl
from sklearn.model_selection import ParameterGrid

class Model:
    def __init__(self, name, model, hyper_param_grid) -> None:
        self.__name = name
        self.__model = model
        self.__hyper_param_grid = hyper_param_grid
        self.__path = None
        self.__features = None

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_hyper_params(self):
        return self.__hyper_param_grid

    def get_path(self):
        return self.__path

    def set_features(self, features):
        self.__features = features

    def get_features(self):
        return self.__features

    def get_params(self):
        return self.__model.get_params()

    def get_name(self):
        return self.__name

    def set_name(self, name:str):
        ending = name[-4:]
        self.__name = name[:-4] if ending == '.pkl' else name

    def save(self):
        file_dir = os.path.dirname(os.path.abspath(__file__))
        model_folder = os.path.join(file_dir, 'model_store')

        if not os.path.exists(model_folder):
            os.mkdir(model_folder)

        file_path = os.path.join(model_folder, f'{self.__name}.pkl')
        with open(file_path, 'wb') as file:
            pkl.dump(self, file)

        self.__path = file_path
        return file_path

    def ask_for_params(self):
        '''
        Method for overwriting in subclasses
        '''
        return

    def hyper_fit(self, X, y):
        '''
        Method for fitting multiple versions of the model
        based on different hyper parameters. Should be 
        implemented for each sub class of the Model class.
        '''
        models = []

        hyper_param_combs = list(ParameterGrid(self.__hyper_param_grid))
        for param_comb in hyper_param_combs:
            fitted_model = self.__model.set_params(**param_comb).fit(X, y)
            hyper_model = copy.deepcopy(self)
            hyper_model.set_model(fitted_model)
            models.append(hyper_model)

        return models