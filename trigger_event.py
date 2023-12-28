import boto3

# Create an EventBridge client
event_client = boto3.client('events')

# Define a rule and schedule it to trigger at 7 PM every day using a correct cron expression
response = event_client.put_rule(
    Name='NightyNight',  # Specify the name of the rule
    ScheduleExpression='cron(0 19 * * ? *)'  # Set the cron expression for 7 PM every day
)

# Retrieve and print the ARN from the response
rule_arn = response['RuleArn']
print(rule_arn)

# Create an event source mapping for the Lambda function
function_name = 'stopInstances'

# Create an EventBridge target for the rule
event_client.put_targets(
    Rule='NightyNight',
    Targets=[
        {
            'Id': 'NightyNight7',  # Unique ID for the target
            'Arn': 'arn:aws:lambda:us-east-1:578218733538:function:stopInstances'
        },
    ]
)
