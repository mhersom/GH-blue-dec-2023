import boto3

vpc_id = 'vpc-06766c49e961331cf'

ec2 = boto3.client('ec2')

ec2.delete_vpc(
    VpcId=vpc_id,
)

