# end-to-end-chestClassification-mlflow-DVC
Perform chest classification using deeplearning tensorflow 
1. Create a template file and sepup.py 
2. Then create code in src/cnnClassifier/__init__.py  a logger creation. to check the working of logger create main.py and after import of logger module by from cnnClassifier import logger. and add a single line of code logger.info("welcome to the main script")
3. Working in utilts folder and create common.py and add the following functions 
    1. read_yaml    2. create_directories   3. save_json    4.load_json     5.save_bin      6.  load_bin    7.  get_size


4. load data from the source. in this project i source data from gdrive using gdown module. 
5. then update config.yaml file with data_ingestion key with four value pairs like 'root_dir','source_url', 'local_data_file', 'unzip_dir'
6. then update constants/__init__.py with configuration files added. config and params file.
7. Update the configuration manager in src with class configurationManager that contains method name get_data_ingestion_config 
8. Update the components with DataIngestion class containing download_file and extract_zip_file methods


## Workflows

1. Update config.yaml 
2. Update secrets.yaml [Optional]
3. Update params.yaml 
4. Update the entity 
5. Update the cofuguration manager in src config
6. Update the cmponents 
7. Update the pipeline 
8. Update the main.py 
9. Update the dvc.yaml 


export MLFLOW_TRACKING_URI=https://dagshub.com/ikram2500/end-to-end-chestClassification-mlflow-DVC.mlflow
export MLFLOW_TRACKING_USERNAME=ikram2500
export MLFLOW_TRACKING_PASSWORD=bc4a05ef4f1a8239f5992d3a59f226a7d0c22822