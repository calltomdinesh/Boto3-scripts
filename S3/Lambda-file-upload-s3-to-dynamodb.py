# Trigger Lambda function when json file is uplodaed to s3
# The lambda function has to process json file and store it in dynamodb

import boto3
import json

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
        bucket = event['Records'][0]['s3']['bucket']['name']
        json_file_name = event['Records'][0]['s3']['object']['key']
        json_object = s3_client.get_object(Bucket=bucket,Key=json_file_name)
        jsonFileReader = json_object['Body'].read()
        # Convert file into a dictionary
        jsonDict = json.loads(jsonFileReader)
        table = dynamodb.Table('employees')
        table.put_item(Item=jsonDict)
        
        
        #print(bucket)
        #print(json_file_name)
        #print(str(event))
        return 'hello from lambda'
        
