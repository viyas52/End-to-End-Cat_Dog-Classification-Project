from src.constants import *
from src.utils.common import read_yaml, create_directories
import os 
import logging
from pathlib import Path
from src.entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        
        logging.info("paths of the yaml files are assinged")
        
        create_directories([self.config.artifacts_root])
        
        logging.info("aritifacts folder created")
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])
        
        logging.info("data ingestion folder  created")
        
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        
        logging.info("successfully returned the DataIngestionConfig")
        
        logging.info("ConfigurationManager for data ingestion done")
        return data_ingestion_config