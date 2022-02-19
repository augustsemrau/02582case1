import os
from pandas import DataFrame

class Strategy:
    def __init__(self) -> None:
        self.__response = None

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

    def save_data(self, data:DataFrame, org_filename:str, strategy:str):
        file_dir = os.path.dirname(os.path.abspath(__file__))
        data_folder = os.path.join(file_dir, '..', '..', 'data', 'preprocessed')

        if not os.path.exists(data_folder):
            os.makedirs(data_folder)

        file_path = os.path.join(data_folder, f'{strategy}.csv')
        data.to_csv(file_path)

        return file_path

    def ask_for_params(self):
        '''
        Method for overwriting in subclasses
        '''
        return