import pandas as pd
from modelling.models import model_register

def create_model(model_name:str, model_type:str, train_data:pd.DataFrame):
    '''
    Creates a model and saves it as a .pkl file to the 'model_store' folder.

    :param model_name:      Name of model to create. This name will be used for the
                            file in which the model is saved to in the model_store folder
    :param model_type:      Type of model which should correspond to the name of one of the
                            .py files in the 'models' folder.
    :param train_data:      Taining data, the last column in the training data must be 
                            the target/response variable i.e. 'y'
    
    :returns:               The created model object
    '''
    model = model_register[model_type.lower().strip()]()
    model.set_name(model_name.strip())
    model.ask_for_params()

    model.set_features(train_data.columns)
    train_data = train_data.to_numpy()
    X = train_data[:, :-1]
    y = train_data[:, -1]

    model.fit(X, y)
    model.save()

    return model