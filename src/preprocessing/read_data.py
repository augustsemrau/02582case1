import os
import json
from unicodedata import decimal
import pandas as pd

def read_data(data_path:str, sep:str, delimiter:str):
    '''
    Loads data from the given path as a pandas DataFrame

    :param data_path:    Path to the data file, which should be .csv or .xlsx
    :param sep:          Seperator to use for reading data if the format is .csv
    :param delimiter:    Delimiter to use for reading data if the format is .csv

    :returns:       The data loaded into a pandas DataFrame
    '''
    if data_path[-4:] == '.csv':
        data = pd.read_csv(data_path, sep=sep, decimal=delimiter)
    elif data_path[-5:] == '.xlsx':
        data = pd.read_excel(data_path, decimal=delimiter)
    elif data_path[-4:] == '.xls':
        data = pd.read_excel(data_path, decimal=delimiter)
    else:
        raise Exception(f'Invalid data format for file {data_path}')

    data.columns = [c.strip().lower() for c in data.columns]

    return data