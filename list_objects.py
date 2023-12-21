import boto3

def filter_objects_extension(client, bucket, extension):
    keys = []
    response = s3.list_objects_v2(
        Bucket='bucket',
#       Delimiter='string',
#       EncodingType='url',
#       MaxKeys=123,
#       Prefix='folder_a/folder_3/', #input desired folder name to filter
#       ContinuationToken='string',
#       FetchOwner=True|False,
#       StartAfter='string',
#       RequestPayer='requester',
#       ExpectedBucketOwner='string',
#       OptionalObjectAttributes=[
#            'RestoreStatus',
#       ]
)
    for content in response["Contents"]:
        if(extension in content['Key'][(-len(extension)):]):
            keys.append(content['Key'])

    return keys

def list_objects_keys(client, bucket, prefix=""):
    keys = []
    response = s3.list_objects_v2(
        Bucket='bucket',
#       Delimiter='string',
#       EncodingType='url',
#       MaxKeys=123,
        Prefix='prefix' #input desired folder name to filter
#       ContinuationToken='string',
#       FetchOwner=True|False,
#       StartAfter='string',
#       RequestPayer='requester',
#       ExpectedBucketOwner='string',
#       OptionalObjectAttributes=[
#            'RestoreStatus',
#       ]
)
    for content in response["Contents"]:
        keys.append(content['Key'])

    return keys

if __name__ == '__main__':
    s3 = boto3.client('s3')
    
    response = list_objects_keys(s3, 'mhersom-boto3-12182023', 'folder_a/')
    print(response)
    
    response = filter_objects_extension(s3, 'mhersom-boto3-12182023', '.txt')
    print(response)
