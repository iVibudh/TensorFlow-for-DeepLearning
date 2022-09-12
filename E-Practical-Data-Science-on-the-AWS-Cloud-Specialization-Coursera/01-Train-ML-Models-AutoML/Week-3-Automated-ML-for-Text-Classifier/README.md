### Week 3:
- Introduction
- Automated Machine Learning (AutoML)
    - The concept of using ML combined with automation to automate the process of building a model.
- AutoML Workflow
    - typical Machine Learning workflow and some of the common tasks performed. 
- Amazon Sagemaker **Autopilot**
    - automate the data exploration and analysis, selecting the right algorithm and performing feature engineering, then automating and training your tuning experiments until you have that model that is performing well or a model that can be used as a staring point.  
    - allows to experiment at scale without manual constraints and computing resources. 
- Running experiments with Amazon Sagemaker Autopilot
    - Review and understand the output resources and artifacts that are automatically produced:
- Amazon SageMaker Autopilot: evaluating output
- VideoAmazon SageMaker Autopilot demo
- Model hosting
    - using a Sagemaker managed endpoint

### Additional reading material
- [Amazon SageMaker Autopilot](https://aws.amazon.com/sagemaker/autopilot/)
- [Amazon Science Publication](https://www.amazon.science/publications/amazon-sagemaker-autopilot-a-white-box-automl-solution-at-scale)

### Lab
You will train a text classification model using Amazon SageMaker Autopilot. The lab will include the following sections:
- Dataset review
- Configure the Autopilot job
- Launch Autopilot job
- Track Autopilot job progress
- Feature engineering
- Model training and tuning
- Review all output
- Deploy and test best candidate model

# Amazon SageMaker Autopilot demo UI

Configure and launch an autopilot job UI version 
- Open "Amazon SageMaker Studio"
- Open "New Autopilot experiment"
- Defrine Configuration options 
    - Experiment name
    - Project 
    - Connect your data (Find S3 bucket or Enter S3 bucket location)
    - Dataset file name
    - ML problem type 
    -.....
    - etc, 
- then click on "Create Experiment"


Now you have created the Experiment and want to look at the rescources and artifacts produced from the autopilot job. All of the tasks that happened within an autopilot job happened within an experiment. 
- To view this, last icon on the console called "Components and registries"
- In the dropdown select "Experiments and trials"
- Right click the experiment previously created
- Select "Describe AutoML Job"
- You will now see the trials run as a part of this experiment. You might see that all the jobs have been completed and "Best" job too. 
    - a trial is a tuning job - one candidate pipeline - with data pre-processing code and your algorithm with hyperparameter ranges for that algorithm + Hyperparameter tuning 
    - Click on the "Best" job and then select "Open model trials" 
        - model explainability, hyperparameters chosen, training and validation error. 
        - inputs, artifacts, and rescources can be seen under the "Artifacts" tab

Data Exploration Notebook and the Candidate Generation notebook. 
- Go back to the experiments with the "Best job.
- Select "Open data exploration notebook" or "Open candidate generation notebook". This will be in "Read-only mode".
- create a local copy of the notebook by selecting "Import notebook".
- Select Kernel. let's say "Python 3 Data Science kernel". 
- Run the code to download the generated data transformation models from S3 to our local studio notebook environment. 
- Click on the folder "automl-dm-1234-artifacts". It has 2 sub-folders:
    - generated_module (contains the candidate data processors)
        - Candidate_data_processors folder contains
            - dpp0.py: 
                - MultiColoumnTfidfVectorizer(max_df = 0.9941, mindf = 0.0007, analyzer = 'word', max_features = 10000)
                - Merges the features that are generated and applies robust standard scalar ('robuststandardscalar')
            - dpp1.py
                - MultiColoumnTfidfVectorizer(max_df = 0.99, mindf = 0.0021, analyzer = 'char-wb', max_features = 10000)
                - Merges the features that are generated and applies Robust PCA('robustpca'), followed by robust standard scalar ('robuststandardscalar')
            - dpp2.py
    - sagemaker_automl (a notbook helper library)
        - code for candidate ML models are in the andidate generation notebook
            - dpp0-xgboost
            - dpp1-xgboost
            - dpp2-xgboost
            - Additional info on hyperparameter tuning job inputs and rages that were identified by autopilot.
            - Result of the tuning jobs
            - details on model selection, and 
            - configuration code to deploy the best performing model to a hosted Sagemaker endpoint. 
            





















