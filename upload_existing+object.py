import boto3

s3 = boto3.client('s3')


#Put object
with open('test_text.txt', 'rb') as file:
    file_contents = file.read()

response = s3.put_object(
    Body=file_contents,
    Bucket='mhersom-boto3-12182023',
    ContentType='text/plain',
    Key='test_text.txt',
)
