from modelling.models import model_register

def create_model(model_name:str, model_type:str):
    '''
    Creates a model and saves it as a .pkl file to the 'model_store' folder.

    :param model_name:      Name of model to create. This name will be used for the
                            file in which the model is saved to in the model_store folder
    :param model_type:      Type of model which should correspond to the name of one of the
                            .py files in the 'models' folder.
    
    :returns:               Path to the created model
    '''
    model = model_register[model_type.lower().strip()]()
    model.set_name(model_name.strip())
    model.save()