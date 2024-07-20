from src.config import ConfigurationManager
from src.components import PrepareCallback,Training
import logging
import sys
from src.exception import CustomException

STAGE_NAME = "model trainer stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list=callback_list
        )
        
        
if __name__ == "__main__":
    try:
        logging.info(f'>>>>>>> stage {STAGE_NAME} started <<<<<<<<')
        obj = ModelTrainingPipeline()
        obj.main()
        logging.info(f'>>>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<< \n\n x=========================x')
                    
    except Exception as e :
        raise CustomException(e,sys)
            
  