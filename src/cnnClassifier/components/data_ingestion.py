import os
import gdown
from src.cnnClassifier.entity.entity_config import DataIngestionConfig
import zipfile
from src.cnnClassifier import logger


class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config

    def download_data(self):
        try:
            dataset_url = self.config.source_URL
            zip_download_path = self.config.local_data_file
            os.makedirs('artifacts/data_ingestion',exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_path}")

            

            file_id = dataset_url.split('/')[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id, zip_download_path)

            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_path}")
            
        except Exception as e:
            raise e
            
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)         