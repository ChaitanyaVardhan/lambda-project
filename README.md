# lambda-project
This repository contains a lambda function that reads a tab in an xls file stored in a S3 repository and writes a json file back
to the S3 repository.
### Deployment
The easiest way to deploy this lambda function is by using the AWS Cloud 9 environment. Below are the steps to deploy this function in
AWS Lamda:
* Create an AWS Cloud 9 environment.
* Create an empty python 3.6 lambda function in that environment.
* copy the code in this lambda function to the empty lambda function created above.
* Install all the dependencies **locally** in the repository containing the lambda_function. Use the -t flag to install the packages
locally
* Deploy the lambda function.
