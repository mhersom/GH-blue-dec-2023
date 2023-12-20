import boto3

s3 = boto3.client('s3')


#Put object
response = s3.put_object(
    Body='Hey this is a string',
    Bucket='mhersom-boto3-12182023',
    ContentType='text/plain',
    Key='test_text_string.txt',
)
