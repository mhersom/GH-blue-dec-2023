import boto3

bucket = 'mhersom-boto3-12182023'
key = 'test_text_string.txt'

s3 = boto3.client('s3')

response = s3.delete_object(
    Bucket='bucket',
    Key='key',
)