import boto3

ami_id = 'ami-0babc3bcde45d15a4'
key_pair_name = 'Key from boto3'
sg_id = 'sg-0870a565c09b3cb09'


ec2 = boto3.client('ec2')

response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType='t2.micro',
    KeyName=key_pair_name,
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=[sg_id],
)

print(response['Instances'][0]['InstanceId'])