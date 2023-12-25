import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_security_groups()

for sg in response['SecurityGroups']:
    print(sg['GroupId'], sg['VpcId'], sg['GroupName'], sg['Description'])
    
    for permission in sg['IpPermissions']:
        if 'FromPort' in permission:
            print(permission['FromPort'])
            
        if 'IpProtocal' in permission:
            print(permission['IpProtocol'])
        
        if 'ToPort' in permission:
            print(permission['ToPort'])
            
        if 'IpIRanges' in permission:
            for iprange in permission('IpRanges'):
                print(iprange['CidrIp'])
