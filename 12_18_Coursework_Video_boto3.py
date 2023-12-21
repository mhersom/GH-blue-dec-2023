import boto3

#client = boto3.client('s3')
#don't set variable to client

s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket='mhersom-boto3-12182023'
)

print(response)