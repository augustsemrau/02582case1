import os
import argparse
import modelling

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
    available_strategies = [name[:-3] for name in os.listdir(os.path.join(file_path, 'modelling', 'strategies', 'assessment'))
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
    parser.add_argument('--strategy', '-s', type=str, default=None, required=True,
                        help=f'''Type of assessment strategy to train and test the model.
                                Available strategies: {available_strategies}''')
    parser.add_argument('--train_data', '-train', type=str, default=None, required=True,
                        help='Path to training data saved as a .csv"')
    parser.add_argument('--test_data', '-test', type=str, default=None, required=True,
                        help='Path to test data saved as a .csv"')

    args = parser.parse_args()
    model_path = modelling.create_model(args.model_name, args.model_type)
    modelling.assess_model(model_path, args.strategy)



if __name__ == '__main__':
    main()