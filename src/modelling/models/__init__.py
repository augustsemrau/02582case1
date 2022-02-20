model_register = {}

def register(cls):
    model_register[cls.__name__.lower()] = cls
    return cls

from modelling.models.KNN import KNN
from modelling.models.OLS import OLS
from modelling.models.LDA import LDA
from modelling.models.Ridge import Ridge