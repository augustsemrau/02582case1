model_register = {}

def register(cls):
    model_register[cls.__name__.lower()] = cls
    return cls

from modelling.models.OLS import OLS