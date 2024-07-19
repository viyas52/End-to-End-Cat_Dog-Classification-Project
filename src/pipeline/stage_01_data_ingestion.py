from src.config import ConfigurationManager
from src.components import DataIngestion
import logging
import sys
from src.exception import CustomException

STAGE_NAME = "data ingestion stage"


class DataIngestiontrainingPipeline:
    def __init__(self):
        pass
    
    def main(self): 
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.unzip_and_clean()
        
if __name__ == "__main__":
    try:
        logging.info(f'>>>>>>> stage {STAGE_NAME} started <<<<<<<<')
        obj = DataIngestiontrainingPipeline()
        obj.main()
        logging.info(f'>>>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<< \n\n x=========================x')
                    
    except Exception as e :
        raise CustomException(e,sys)
        