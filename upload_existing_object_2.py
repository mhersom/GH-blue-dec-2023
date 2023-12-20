import boto3

s3 = boto3.client('s3')

#Upload File
s3.upload_file('test_text.txt', 'mhersom-boto3-12182023', 'test_text_upload.txt', ExtraArgs={'ContentType':'text/plain'})