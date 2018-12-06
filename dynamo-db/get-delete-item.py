import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employees')

table.put_item(
   Item={
        'emp_id': '3',
        'name': 'Din',
        'salary': 250000
    }
)


response = table.get_item(
    Key = {
        'emp_id' : '2'
    }
)

item = response['Item']
print(item)

response = table.delete_item(
    Key = {
        'emp_id' : '2'
    }
)


