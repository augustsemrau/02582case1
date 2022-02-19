from modelling.strategies import register, Strategy

@register
class Strategy1(Strategy.Strategy):
    def assess(self, model, data):
        '''
        Assesses the given model on the given data and selects the best found version.
        Saves the model and a summary to the models > model_store folder,
        and returns the best model.

        :param model:   Model to asses
        :param data:    Data to use for assessment

        :returns:       The best found version of the model
        '''
        raise Exception('Not implemented')