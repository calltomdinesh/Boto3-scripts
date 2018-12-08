import boto3
client = boto3.client('ec2')

instances= client.describe_instances()
used_amis = []

for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        used_amis.append(instance['ImageId'])

print(used_amis)

# Remove duplicate amis

def remove_duplicates(amis):
    unique_amis = []
    for ami in amis:
        if ami not in  unique_amis:
            unique_amis.append(ami)
    return  unique_amis


unique_amis = remove_duplicates(used_amis)
print(unique_amis)

# Get custom amis from the account

custom_images = client.describe_images(
    Filters=[
        {
            'Name': 'state',
            'Values': [
                'available'
            ]
        }
    ],
    Owners=['self']
        
)

custom_amis = []
for image in custom_images['Images']:
    custom_amis.append(image['ImageId'])

print(custom_amis)

# Delete custom amis if they are not present in used amis

for ami in custom_amis:
    if ami not in unique_amis:
        client.deregister_image(
            ImageId=ami
        )
    