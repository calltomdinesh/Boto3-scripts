# When EC2 instance stops send Email by publishing message to SNS topic

import boto3
sns = boto3.client('sns')

def lambda_handler(event, context):
    
    sns.publish(
        TopicArn='arn:aws:sns:ap-south-1:106547729051:sns-demo',
        Message = 'Prod server stopped, pls take action'
    )
    
