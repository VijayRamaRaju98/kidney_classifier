from src.cnnClassifier.pipeline.state_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier import logger
STAGE_NAME = "Data Ingestion Stage"





try:
    logger.info(f">>>>> {STAGE_NAME} Started <<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
    raise e
