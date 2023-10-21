from src.cnnClassifier.pipeline.state_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_02_prepare_basemodel import PrepareBaseModelTrainingPipeline



STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> {STAGE_NAME} Started <<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
    raise e



STAGE_NAME = "Prepare Base Model"

try:
    logger.info(f"*********************")
    logger.info(f">>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<<<<<<<")
except Exception as e:
    raise e