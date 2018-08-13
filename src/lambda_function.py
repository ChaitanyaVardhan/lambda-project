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
, sheet_name='MICs List by CC', engine=None)

    row_list = data_frame.to_dict(orient='row')

    print('num of rows: %d ' % len(row_list))

    with open('/tmp/data.json', 'w') as outfile:
        json.dump(row_list, outfile)

    bucket_name = 'json-file-bucket'

    file_name = 'data.json'

    with open('/tmp/data.json', 'rb') as data:
        s3_client.upload_fileobj(data, bucket_name, file_name)

    return 'Returning from Lambda'

