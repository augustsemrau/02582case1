import os
import argparse
import modelling
import preprocessing

'''
This script can be called to create a model of the given model_type with the given model_name.
The model will be trained on the given train_data using the given strategy.
Afterwards the model will be saved as a .pkl file to the model_store folder.
From there it can be fetched and used in the select.py or predict.py scripts.
'''

def main():

    file_path = os.path.dirname(os.path.abspath(__file__))
    available_models = [name[:-3] for name in os.listdir(os.path.join(file_path, 'modelling', 'models')) 
                        if name[-3:].lower() == '.py' and name != '__init__.py' and name != 'Model.py']
    available_models = ', '.join(available_models)
    available_strategies = [name[:-3] for name in os.listdir(os.path.join(file_path, 'modelling', 'strategies'))
                            if name[-3:].lower() == '.py' and name != '__init__.py']
    available_strategies = ', '.join(available_strategies)

    desc = f'''This script can be called to create a model of the given model_type with the given model_name.
            The model will be trained on the given train_data using the given strategy.
            Afterwards the model will be saved as a .pkl file to the model_store folder.
            From there it can be fetched and used in the select.py or predict.py scripts.
            '''

    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('--model_name', '-mn', type=str, default=None, required=True,
                        help='Name of new model to create e.g. "my_model"')
    parser.add_argument('--model_type', '-mt', type=str, default=None, required=True,
                        help=f'Type of new model to create. Available types: {available_models}')
    parser.add_argument('--data', '-d', type=str, default=None, required=True,
                        help='Path to data saved as a .csv"')
    parser.add_argument('--seperator', '-sep', type=str, default=';', required=False,
                        help='Seperator to use for reading train data .csv, default is semi-colon(;)')
    parser.add_argument('--delimiter', '-del', type=str, default=',', required=False,
                        help='Delimiter to use for reading decimals in train data .csv, default is comma(,)')
    parser.add_argument('--strategy', '-s', type=str, default=None, required=True,
                        help=f'''Strategy/logic to use for training and assessing model. 
                                Available strategies: {available_strategies}''')
    

    args = parser.parse_args()
    print('Building model...')
    data = preprocessing.read_data(args.data, args.seperator, args.delimiter)
    model = modelling.create_model(args.model_name, args.model_type)
    strategy = modelling.create_strategy(args.strategy)
    best_model = strategy.assess(model, data)


    print(f'''Model saved to: {best_model.get_path()} \n
            Model performance summary saved to: {best_model.get_summary_path()} \n
            Data used: {args.data} \n
            ''')

    '''
        for 1:M
        Randomize data (permute)
        Split data in 3 (train, validation, test)
        Train model on range of tuning parameters using train data
        Select best model based on validation data
        Test model to estimate the error on test set
        end
        Calculate mean and std error over M test errors
    '''



if __name__ == '__main__':
    main()