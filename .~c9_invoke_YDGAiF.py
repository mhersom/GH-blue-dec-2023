import boto3

ami_id = ''
key p

ec2 = boto3.client('ec2')

response = ec2.run_instances(
    ImageId='ami-abc12345',
    InstanceType='t2.micro',
    KeyName='my-key-pair',
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=[
        'sg-1a2b3c4d',
    ],
    SubnetId='subnet-6e7f829e',
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Purpose',
                    'Value': 'test',
                },
            ],
        },
    ],
)

print(response)