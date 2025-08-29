from cnnClassifier.config.configuration import CofigurationManager
from cnnClassifier.components.model_evaluation_mlflow import Evaluation
from cnnClassifier import logger 


STAGE_NAME = "Evaluation stage"


class EvaluationPipeline:
        def __init__(self):
            pass


        def main(self):
            config = CofigurationManager()
            eval_config = config.get_evaluation_config()
            evaluation = Evaluation(eval_config)
            evaluation.evaluation()
            evaluation.log_into_mlflow()
        
if __name__ == "__main__":
     try:
          logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
          obj = EvaluationPipeline()
          obj.main()
          logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
     except Exception as e:
          logger.error(f">>>>> stage {STAGE_NAME} failed <<<<<")
          logger.error(e)