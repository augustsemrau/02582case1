import os
import argparse
import pandas as pd
import preprocessing

'''
This script can be called to preprocess data and save the preprocessed data
to a .csv file. The script will always save the preprocessed data to a file
in src > data > preprocessed.
'''

def main():

    file_path = os.path.dirname(os.path.abspath(__file__))
    available_strategies =  [name[:-3] for name in os.listdir(os.path.join(file_path, 'preprocessing', 'strategies')) 
                            if name[-3:].lower() == '.py' and name != '__init__.py' and name != 'Strategy.py']
    available_strategies = ', '.join(available_strategies)

    desc = f'''
            This script can be called to preprocess data and save the preprocessed data
            to a .csv file. The script will always save the preprocessed data to a file
            in src > data > preprocessed.
            '''

    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('--data', '-d', type=str, default=None, required=True,
                        help='Path to data saved as a .csv or .xlsx')
    parser.add_argument('--seperator', '-sep', type=str, default=';', required=False,
                        help='Seperator to use for reading data if the format is .csv, default is semi-colon(;)')
    parser.add_argument('--delimiter', '-del', type=str, default=',', required=False,
                        help='Delimiter to use for reading data if the format is .csv, default is comma(,)')
    parser.add_argument('--strategy', '-s', type=str, default=None, required=True,
                        help=f'Strategy/logic to use for preprocessing. Available strategies: {available_strategies}')
    parser.add_argument('--response', '-r', type=str, default=None, required=True,
                        help=f'Name of the response/target variable in the data a.k.a. "y"')

    args = parser.parse_args()
    print('Preprocessing data...')
    strategy = preprocessing.create_strategy(args.strategy, args.response)
    data = preprocessing.read_data(args.data, args.seperator, args.delimiter)
    preprocessed_data = strategy.process(data)
    preprocessed_data_path = strategy.save_data(preprocessed_data, args.data, 
                                args.strategy, args.seperator, args.delimiter)

    print(f'''Data loaded from: {args.data} \n
            Preprocessed using strategy: {args.strategy} \n
            Response/target variable:   {args.response}
            Preprocessed data saved to: {preprocessed_data_path}
            ''')



if __name__ == '__main__':
    main()