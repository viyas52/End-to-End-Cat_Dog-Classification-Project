from src.constants import *
from src.utils.common import read_yaml, create_directories
import os 
import logging
from pathlib import Path
from src.entity import DataIngestionConfig,PrepareBaseModelConfig

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
    
    
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        params = self.params
        
        create_directories([config.root_dir])
        
        logging.info("base model directory created")
        
        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=params.IMAGE_SIZE,
            params_learning_rate=params.LEARNING_RATE,
            params_include_top=params.INCLUDE_TOP,
            params_weights=params.WEIGHTS,
            params_classes=params.CLASSES
        )
        logging.info("successfully returned the PrepareBaseModelConfig")
        
        logging.info("ConfigurationManager for base model done")
        
        return prepare_base_model_config
    