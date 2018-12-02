# -*- coding: utf-8 -*-
"""
Start,Stop,terminate EC2 instances
"""


import boto3
client = boto3.client('ec2')

response = client.terminate_instances(
        InstanceIds=['i-0401f0367bd0a8f72','i-0772b9e08c7cc6bf9'])

for instance in response['TerminatingInstances']:
    print(instance['InstanceId'])

