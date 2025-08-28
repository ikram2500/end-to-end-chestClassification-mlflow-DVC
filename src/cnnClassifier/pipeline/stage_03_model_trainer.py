from cnnClassifier.config.configuration import CofigurationManager
from cnnClassifier.components.model_trainer import Training
from cnnClassifier import logger 




STAGE_NAME = "Training"


class ModelTrainingPipeline:
      def __init__(self):
             pass 
      
      def main(self):
        config = CofigurationManager()
        training_config = config.get_training_config()
        training = Training(config = training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()




if __name__ == "__main__":
     try:
          logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
          obj = ModelTrainingPipeline()
          obj.main()
          logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
     except Exception as e:
          logger.error(f">>>>> stage {STAGE_NAME} failed <<<<<")
          logger.error(e)