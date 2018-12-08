# This Lambda function runs EC2 instnaces in schedule


import boto3

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    filter = [
        {
            'Name': 'tag:Type', 
            'Values': ['Scheduled']
            
        }
    ]   
    instances = ec2.instances.filter(Filters=filter)

    for instance in instances:
        print(instance)
        instance.start()

    return str(instance)

