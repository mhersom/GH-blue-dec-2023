import boto3

subnet_id = 'subnet-029d7184331bc06f9'

ec2 = boto3.client('ec2')

ec2.delete_subnet(
    SubnetId=subnet_id,
)
