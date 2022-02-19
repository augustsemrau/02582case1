import pandas as pd
from preprocessing.strategies import register, Strategy

@register
class Preprocess1(Strategy.Strategy):
    def __init__(self) -> None:
        self.__date_cols = []

    def __split_date_cols(self, data):
        for col in self.__date_cols:
            data[f'{col} minute'] =  data[col].dt.minute
            data[f'{col} hour'] =  data[col].dt.hour
            data[f'{col} day'] =  data[col].dt.day
            data[f'{col} month'] =  data[col].dt.month
            data[f'{col} year'] =  data[col].dt.year

        data = data.drop(self.__date_cols, axis=1)
        return data

    def __set_response_last(self, data):
        new_order_cols = data.columns.tolist()
        new_order_cols.remove(self.get_response())
        new_order_cols = sorted(new_order_cols)
        new_order_cols.append(self.get_response())
        return data.reindex(columns=new_order_cols)

    def process(self, data):
        data = self.__split_date_cols(data)
        data = pd.get_dummies(data)
        data = self.__set_response_last(data)

        return data


    def ask_for_params(self):
        date_cols = input('Date column names seperated by comma e.g. col1, col2, col3: ')
        self.__date_cols = [dc.lower().strip() for dc in date_cols.split(',')]