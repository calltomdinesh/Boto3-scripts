# Create Snapshots, send email and delete snapshots
from datetime import datetime, timedelta, timezone
import boto3
ec2 = boto3.resource('ec2')

# Creating SNS client to send mail
sns_client = boto3.client('sns')

backup_filter =  Filters=[
        {
            'Name': 'tag:Backup',
            'Values': [
                'Yes',
            ]
        },
    ]
        
instances = ec2.instances.filter(Filters=backup_filter)

snapshot_ids = []

# Looping thorugh list of Ec2 instances
for instance in instances:
    for vol in instance.volumes.all():
        snapshot = vol.create_snapshot(Description='Volume created by \
                            Boto3')
        
        snapshot_ids.append(snapshot.snapshot_id)
        

for snap in snapshot_ids:
    print(snap)
    
# Sending email thorugh SNS

sns_client.publish(
    TopicArn='arn:aws:sns:ap-south-1:106547729051:sns-demo',
    Message=str(snapshot_ids),
    Subject='EBS Snapshots'
)

# Deleting snapshots in the account by collecting them
# Delete the snapshots which are older than 15 days

ec2 = boto3.resource('ec2')
snapshots=ec2.snapshots.filter(OwnerIds=['self'])
for snapshot in snapshots:
    print(snapshot.snapshot_id)
start_time=snapshot.start_time
delete_time=datetime.now(tz=timezone.utc) - timedelta(days=15)
if delete_time > start_time:
    snapshot.delete()
    print('snapshot with id {} deleted'.format(snapshot.snapshot_id))

                               
    