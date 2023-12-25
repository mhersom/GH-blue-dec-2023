import boto3

vpc_id = 'vpc-06766c49e961331cf'

ec2 = boto3.client('ec2')

routeTable = ec2.create_route_table(VpcId=vpc_id)

print(routeTable['RouteTable']['RouteTableId'])