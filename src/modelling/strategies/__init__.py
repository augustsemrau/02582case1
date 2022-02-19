strategy_register = {}

def register(cls):
    strategy_register[cls.__name__.lower()] = cls
    return cls

from modelling.strategies.Strategy1 import Strategy1