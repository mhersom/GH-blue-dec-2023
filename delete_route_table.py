import boto3

route_table_id = 'rtb-0f1bf104964af962e'

ec2 = boto3.client('ec2')

ec2.delete_route(
    DestinationCidrBlock='0.0.0.0/0',
    RouteTableId=route_table_id ,
)
