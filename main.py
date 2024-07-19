from src.pipeline.stage_01_data_ingestion import DataIngestiontrainingPipeline
from src.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
import logging
from src.exception import CustomException
import sys


STAGE_NAME = "data ingestion stage"
try:
    logging.info(f'>>>>>>> stage {STAGE_NAME} started <<<<<<<<')
    data_ingestion = DataIngestiontrainingPipeline()
    data_ingestion.main()
    logging.info(f'>>>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<< \n\n x=========================x')
                    
except Exception as e :
    logging.exception(e)
    raise CustomException(e,sys)


STAGE_NAME = "base model creation stage"
try:
    logging.info(f'>>>>>>> stage {STAGE_NAME} started <<<<<<<<')
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logging.info(f'>>>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<< \n\n x=========================x')
                    
except Exception as e :
    raise CustomException(e,sys)