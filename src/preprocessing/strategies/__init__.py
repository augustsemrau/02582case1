strategy_register = {}

def register(cls):
    strategy_register[cls.__name__.lower()] = cls
    return cls

from preprocessing.strategies.Preprocess1 import Preprocess1