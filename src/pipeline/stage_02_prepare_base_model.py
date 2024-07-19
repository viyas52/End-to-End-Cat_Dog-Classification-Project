from src.config import ConfigurationManager
from src.components import PrepareBaseModel
import logging
import sys
from src.exception import CustomException

STAGE_NAME = "base model creation stage"


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self): 
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()
        
if __name__ == "__main__":
    try:
        logging.info(f'>>>>>>> stage {STAGE_NAME} started <<<<<<<<')
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logging.info(f'>>>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<< \n\n x=========================x')
                    
    except Exception as e :
        raise CustomException(e,sys)