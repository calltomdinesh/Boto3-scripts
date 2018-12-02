'''
Launch Ec2 using boto3
'''
import boto3
client = boto3.client('ec2')

'''
resp = client.run_instances(
    ImageId = 'ami-06bcd1131b2f55803',
    InstanceType = 't2.micro',
    MaxCount=1,
    MinCount=1        
)

for instance in resp['Instances']:
    inst_id=instance['InstanceId']
    print(inst_id)
'''

'''
Stopping EC2 instances
'''

response = client.stop_instances(
        InstanceIds=[''])