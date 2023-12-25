import boto3

route_table_id = 'rtb-0f1bf104964af962e'
internet_gateway_id = 'igw-0e854c3da182c952c'

ec2 = boto3.client('ec2')

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internet_gateway_id,
    RouteTableId=route_table_id,)
