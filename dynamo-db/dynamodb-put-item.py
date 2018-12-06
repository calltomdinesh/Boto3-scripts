import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employees')

table.put_item(
   Item={
        'emp_id': '2',
        'name': 'Dinesh',
        'salary': 250000
    }
)
