import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employees')

with table.batch_writer() as batch:
    for x in range(100):
        '''
        batch.put_item(
            Item={
                'emp_id': str(x),
                'name': 'Name-{}'.format(x)
            }
        )
        '''
        batch.delete_item(
            Key={
                'emp_id': str(x),
                
            }
        )

