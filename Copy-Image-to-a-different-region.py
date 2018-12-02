# Copying images from one region to other region
# Creating image
import boto3
source_region='ap-south-1'
ec2=boto3.resource('ec2', region_name=source_region)
instances=ec2.instances.filter(InstanceIds=['i-00110c74ee4289fcd'])
#ec2=boto3.resource('ec2')
#instances=ec2.instances.all()
print('instances {}'.format(instances))


image_ids = []
for instance in instances:
    image = instance.create_image(Name='Demo Boto-'+instance.id, Description= \
                               'Demo Boto-'+instance.id)
    image_ids.append(image.id)

print("images to be copied {}".format(image_ids))

# Waiting for the images to be available
# get waiter for the image-available

client=boto3.client('ec2', region_name=source_region)
waiter=client.get_waiter('image_available')

waiter.wait( Filters=[
        {
            'Name': 'image-id',
            'Values': 'image_ids'
            
        },
    ])
    
# Copy images to other region
    
destination_region = 'us-east-1'
client = boto3.client('ec2', region_name=destination_region)
for image_id in image_ids:
    client.copy_image(Name='Copy Image-'+image_id,
    SourceImageId=image_id,
    SourceRegion=source_region,)



