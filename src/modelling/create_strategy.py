from modelling.strategies import strategy_register

def create_strategy(strategy:str):
    '''
    Creates a strategy to be used for selecting between models or tuning hyper parameters.

    :param strategy:    Type of strategy which should correspond to the name of one of the
                        .py files in the 'strategies > assessment' folder.
    
    :returns:           The created strategy object.
    '''
    strategy = strategy_register[strategy.lower().strip()]()
    strategy.ask_for_params()
    return strategy