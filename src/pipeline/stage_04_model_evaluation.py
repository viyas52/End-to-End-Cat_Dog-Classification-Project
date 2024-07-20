from src.config import ConfigurationManager
from src.components import Evaluation
import logging
import sys
from src.exception import CustomException

STAGE_NAME = "model evaluation stage"

class EvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()
        
        
if __name__ == "__main__":
    try:
        logging.info(f'>>>>>>> stage {STAGE_NAME} started <<<<<<<<')
        obj = EvaluationPipeline()
        obj.main()
        logging.info(f'>>>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<< \n\n x=========================x')
                    
    except Exception as e :
        raise CustomException(e,sys)