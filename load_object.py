import boto3

s3 = boto3.client('s3')

s3.download_file('mhersom-boto3-12182023', 'test_text_string.txt', 'test_text_string.txt')