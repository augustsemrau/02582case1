import pandas as pd
from preprocessing.strategies import register, Strategy

@register
class Preprocess2(Strategy.Strategy):

    def process(self, data):


        data = self._split_date_cols(data)
        data = pd.get_dummies(data)
        data = self._set_response_last(data)

        return data


        