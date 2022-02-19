import os
from pandas import DataFrame

class Strategy:
    def __init__(self) -> None:
        self.__response = None
        self.__date_cols = []
        
    def set_date_cols(self, date_cols):
        self.__date_cols = date_cols

    def get_date_cols(self):
        return self.__date_cols

    def _split_date_cols(self, data):
        date_cols = data.select_dtypes(include=['datetime64']).columns
        for col in date_cols:
            data[f'{col} minute'] =  data[col].dt.minute
            data[f'{col} hour'] =  data[col].dt.hour
            data[f'{col} day'] =  data[col].dt.day
            data[f'{col} month'] =  data[col].dt.month
            data[f'{col} year'] =  data[col].dt.year

        data = data.drop(date_cols, axis=1)
        return data

    def _set_response_last(self, data):
        new_order_cols = data.columns.tolist()
        new_order_cols.remove(self.get_response())
        new_order_cols = sorted(new_order_cols)
        new_order_cols.append(self.get_response())
        return data.reindex(columns=new_order_cols)

    def set_response(self, response:str):
        '''
        :param response:    The response/target variable of the strategy
        '''
        self.__response = response

    def get_response(self):
        '''
        :returns: The response/target variable of the strategy
        '''

        return self.__response

    def save_data(self, data:DataFrame, org_filename:str, strategy:str, sep:str, delimiter:str):
        file_dir = os.path.dirname(os.path.abspath(__file__))
        data_folder = os.path.join(file_dir, '..', '..', 'data', 'preprocessed')

        if not os.path.exists(data_folder):
            os.makedirs(data_folder)

        file_path = os.path.join(data_folder, f'{strategy}.csv')
        data.to_csv(file_path, sep=sep, decimal=delimiter)

        return file_path

    def ask_for_params(self):
        '''
        Method for overwriting in subclasses
        '''
        return