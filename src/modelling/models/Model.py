import os
import pickle as pkl

class Model:

    def get_name(self):
        return self.__name

    def set_name(self, name:str):
        ending = name[-4:]
        self.__name = name[:-4] if ending == '.pkl' else name

    def save(self):
        file_dir = os.path.dirname(os.path.abspath(__file__))
        model_folder = os.path.join(file_dir, 'model_store')

        if not os.path.exists(model_folder):
            os.mkdir(model_folder)

        file_path = os.path.join(model_folder, f'{self.__name}.pkl')
        with open(file_path, 'wb') as file:
            pkl.dump(self, file)

        return file_path

    def ask_for_params(self):
        '''
        Method for overwriting in subclasses
        '''
        return