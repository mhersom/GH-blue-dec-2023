import boto3

# Define a function to stop an EC2 instance.
def stop_instance(client, instance_id):
    # Use the stop_instances() method to stop the specified EC2 instance.
    response = client.stop_instances(InstanceIds=[instance_id])
    print(instance_id, 'stopped')

# Create an EC2 client using boto3.
ec2 = boto3.client('ec2')

# Use the describe_instances() method to retrieve information about EC2 instances.
response = ec2.describe_instances()

# Iterate through the reservations in the response.
for reservation in response['Reservations']:
    # Iterate through the instances in each reservation.
    for instance in reservation['Instances']:
        # Check if the instance is in the 'running' state before printing its information.
        if instance['State']['Name'] == 'running':
            # Print instance information.
            print(instance['InstanceId'], instance['State']['Name'])
            
            # Stop the running instance using the stop_instance function.
            stop_instance(ec2, instance['InstanceId'])