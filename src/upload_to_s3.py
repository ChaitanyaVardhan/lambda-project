import pandas as pd

import boto3

import json

import os

def lambda_handler(event, context):
    # print values to see if lambda_handler triggered
    print (str(event))

    s3_client = boto3.client('s3',
                aws_access_key_id=os.environ.get('aws_access_key_id'),
                aws_secret_access_key=os.environ.get('aws_secret_access_key'))

    print("reading excel")
    data_frame = pd.read_excel('https://s3.amazonaws.com/json-file-bucket/ISO10383_MIC.xls'
, sheet_name='MICs Modifications', engine=None)

    row_list = data_frame.to_dict(orient='row')

    print('num of rows: %d ' % len(row_list))

    with open('data.json', 'w') as outfile:
        json.dump(row_list, outfile)

    bucket_name = 'json-file-bucket'

    file_name = 'data.json'

    file_object = s3_client.put_object(Bucket=bucket_name, Key=file_name)    

    return 'Returning from Lambda'

if __name__ == "__main__":

    # simulate the event and context object for testing locally out of Lambda
    class Event:
        def __init__(self):
            self.key1 = 'val1'
            self.key2 = 'val2'
            self.key3 = 'val3'
        
        def __getitem__(self, item):
            return getattr(self, item)

    event = Event()
    context = {'key': 'dummy context'}

    print(lambda_handler(event, context))
            
