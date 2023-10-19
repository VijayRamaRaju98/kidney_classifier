from src.cnnClassifier.entity.entity_config import DataIngestionConfig
from src.cnnClassifier.components.data_ingestion import DataIngestion
from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier import logger

STAGE_NAME = 'Data Ingestion State'

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    
    def main(self):
        try:

            config = ConfigurationManager()
            data_ingestion_config =config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_data()
            data_ingestion.extract_zip_file()
        
        except Exception as e:
            raise e

# if __name__=="__main__":
#     try:
#         obj = DataIngestionTrainingPipeline()
#         obj.main()
#     except Exception as e:
#         raise e