import boto3

ec2 = boto3.client('ec2')

route_table_id = 'rtb-0f1bf104964af962e'
subnet_id = 'subnet-029d7184331bc06f9'

association = ec2.associate_route_table(RouteTableId=route_table_id,SubnetId=subnet_id)

print(association['AssociationId'])