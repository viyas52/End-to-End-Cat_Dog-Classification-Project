from src.pipeline.stage_01_data_ingestion import DataIngestiontrainingPipeline
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