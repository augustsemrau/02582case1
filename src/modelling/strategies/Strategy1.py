import numpy as np
import pandas as pd
from tqdm import tqdm
from modelling.models import Model
from modelling.strategies import register, Strategy
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

@register
class Strategy1(Strategy.Strategy):
    def assess(self, model:Model.Model, data:pd.DataFrame):
        '''
        Assesses the given model on the given data based on the proceduce 
        suggested in Lecture 2 and selects the best found version.
        Saves the model and a summary to the models > model_store folder,
        and returns the best model.

        :param model:   Model to asses
        :param data:    Data to use for assessment

        :returns:       The best found version of the model and its mean 
        '''
        M = 30
        self.test_errors = []
        self.models = []

        for _ in tqdm(range(M)):
            model.set_features(data.columns.values)
            # Randomize data (permute)
            data = data.sample(frac=1).to_numpy()
            #Split data into input and response
            X = data[:,:-1]
            y = data[:, -1]

            # Split data in 3 (train, validation, test)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
            X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2)

            #Train model on range of tuning parameters using train data
            hyper_models = model.hyper_fit(X_train, y_train)

            #Select best model based on validation data
            best_val_model = hyper_models[0]
            best_val_score = mean_squared_error(y_val, best_val_model.predict(X_val))
            for i in range(1,len(hyper_models)):
                hmodel = hyper_models[i]
                pred_y_val = hmodel.predict(X_val)
                MSE = mean_squared_error(y_val, pred_y_val)
                if MSE < best_val_score:
                    best_val_model = hmodel
                    best_val_score = MSE
            
            self.models.append(best_val_model)

            #Test model to estimate the error on test set
            pred_y_test = best_val_model.predict(X_test)
            test_mse = mean_squared_error(y_test, pred_y_test)
            self.test_errors.append(test_mse)

        #Find model with lowest test error
        best_model_index = np.argmin(self.test_errors)
        best_model = self.models[best_model_index]

        return best_model

    def save_assessment_summary(self):
        '''
        Saves the assessment as a summary
        '''
        return