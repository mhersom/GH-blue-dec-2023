import boto3

internet_gateway_id = 'igw-0e854c3da182c952c'

ec2 = boto3.client('ec2')

ec2.delete_internet_gateway(
    InternetGatewayId=internet_gateway_id,
)


