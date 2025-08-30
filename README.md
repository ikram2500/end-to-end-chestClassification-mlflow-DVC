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

AWS-CICD-Deployment-with-Github-Actions
1. Login to AWS console.
2. Create IAM user for deployment
#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
3. Create ECR repo to store/save docker image
- Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken
4. Create EC2 machine (Ubuntu)
5. Open EC2 and Install docker in EC2 Machine:
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
6. Configure EC2 as self-hosted runner:
setting>actions>runner>new self hosted runner> choose os> then run command one by one
7. Setup github secrets:
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = simple-app