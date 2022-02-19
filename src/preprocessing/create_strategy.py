from preprocessing.strategies import strategy_register

def create_strategy(strategy_type:str, response:str):
    '''
    Creates the given strategy and registers the
    given response as the response/target variable
    for the created strategy.

    :param strategy_type:   The type of strategy to create
    :param response:        The name of the variable to use as
                            response/target variable
    
    :returns:               The created strategy
    '''
    strategy = strategy_register[strategy_type.lower().strip()]()
    strategy.set_response(response)
    strategy.ask_for_params()
    return strategy