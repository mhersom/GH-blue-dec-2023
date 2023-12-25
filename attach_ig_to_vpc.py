import boto3

internet_gateway_id = 'igw-0e854c3da182c952c'
vpc_id = 'vpc-06766c49e961331cf'


ec2 = boto3.client('ec2')

ec2.attach_internet_gateway(InternetGatewayId=internet_gateway_id, VpcId=vpc_id)
