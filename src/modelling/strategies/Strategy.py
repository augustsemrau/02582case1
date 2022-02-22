import os
from datetime import datetime, timezone

class Strategy:

    def __init__(self) -> None:
        self.__results = {}
        self.__summary_path = None

    def add_result(self, key, val):
        self.__results[key] = val

    def ask_for_params(self):
        '''
        Method for overwriting in subclasses
        '''
        return

    def get_summary_path(self):
        return self.__summary_path

    def save_assessment_summary(self, model):
        '''
        Saves the assessment as a summary text to the folder "assessment_summaries".
        The method creates the folder if it does not already exists.
        The assessment summary is created based on the key,value pairs in the 
        "__results" variable in the Strategy object.
        '''
        # Add model info
        self.add_result('model name', model.get_name())
        self.add_result('model params', model.get_params())
        self.add_result('model path', model.get_path())
        self.add_result('model features', model.get_features())

        if len(self.__results.keys()) == 0:
            print('No results saved')
        else:
            current_folder = os.path.dirname(os.path.abspath(__file__))
            save_folder = os.path.join(current_folder, 'assessment_summaries')

            # Create local folder for assessements if not already created
            if not os.path.exists(save_folder):
                os.makedirs(save_folder)

            now = datetime.now(timezone.utc)
            date = now.date()
            time = now.time()
            save_path = os.path.join(save_folder, f'{model.get_name()}_summary_{date.day}_{date.month}_{date.year} \
                                                    _{time.hour}_{time.minute}.txt')
            self.__summary_path = save_path
            with open(save_path, 'w') as summary:
                lines = []
                for k, v in self.__results.items():
                    desc = f'{k}: {v}\n'
                    lines.append(desc)
                
                summary.writelines(lines)