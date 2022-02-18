from modelling.strategies.assessment import strategy_register

def create_assessment_strategy(strategy:str):
    '''
    Creates a strategy to be used for assessing model performance on training and test data.

    :param strategy:    Type of strategy which should correspond to the name of one of the
                        .py files in the 'strategies > assessment' folder.
    
    :returns:           The created strategy object.
    '''
    strategy = strategy_register[strategy.lower().strip()]()
    strategy.ask_for_params()
    return strategy