
import boto3
client = boto3.client('ec2')


responses = client.describe_instances(Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                'stopped',
            ]
        },
])

for response in responses['Reservations']:
    for instance in response['Instances']:
        print("Instances {}".format(instance['InstanceId']))
        
responses = client.describe_instances(Filters=[
        {
            'Name': 'tag:Env',
            'Values': [
                'Prod',
            ]
        },
])

for response in responses['Reservations']:
    for instance in response['Instances']:
        print("Instances in Prod {}".format(instance['InstanceId']))    



