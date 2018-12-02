# -*- coding: utf-8 -*-
import boto3
ec2 = boto3.resource('ec2')

for instance in ec2.instances.filter(Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                'stopped'
            ]
        }
    ]):
    print('Instance Id {} Instace type {}'.format(instance.instance_id,instance.instance_type))

# To stop the instances
# Just give as below
    
    ec2.instances.filter(Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                'stopped'
            ]
        }
    ]).stop()
