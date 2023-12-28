import boto3

# Create an AWS Lambda client
lambda_client = boto3.client('lambda')

# Define the IAM role ARN
role = 'arn:aws:iam::578218733538:role/LambdaFullAccess'

# Create a Lambda function
response = lambda_client.create_function(
    FunctionName='stopInstances',  # Specify the function name
    Runtime='python3.8',  # Set the runtime environment
    Role=role,  # Provide the IAM role ARN
    Handler='Stop_Instance_Script.stopInstances',  # Specify the handler in the format 'filename.function'
    Code={'S3Bucket': 'luit-blue-week-15-project', 'S3Key': 'Stop_Instance_Script.zip'},  # Define the code source in an S3 bucket
    Description='Stop all instances at end of day',  # Add a description for the function
)

# Print the function name and ARN
print(response['FunctionName'], response['FunctionArn'])