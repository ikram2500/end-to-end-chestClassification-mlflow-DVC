from cnnClassifier import logger 
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline



STAGE_NAME = "data ingestion stage"

try:
      logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
      obj = DataIngestionTrainingPipeline()
      obj.main()
      logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")    
except Exception as e:
          logger.error(f">>>>> stage {STAGE_NAME} failed <<<<<")
          logger.error(e)  




STAGE_NAME = "prepare base model"
try:
          logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
          obj = PrepareBaseModelTrainingPipeline()
          obj.main()
          logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
          logger.error(f">>>>> stage {STAGE_NAME} failed <<<<<")
          logger.error(e)

STAGE_NAME = "training"

try:
          logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
          obj = ModelTrainingPipeline()
          obj.main()
          logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
          logger.error(f">>>>> stage {STAGE_NAME} failed <<<<<")
          logger.error(e)

STAGE_NAME = "evaluation"



try:
          logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
          obj = EvaluationPipeline()
          obj.main()
          logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
          logger.error(f">>>>> stage {STAGE_NAME} failed <<<<<")
          logger.error(e)