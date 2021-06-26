import boto3
dynamoDB = boto3.resource('dynamodb')
table= dynamoDB.Table('todo')

def lambda_handler(event, context):
    response = table.query(
        KeyConditionExpression=boto3.dynamodb.conditions.Key('yearmonth').eq(event['month'])
    )
    
    return response["Items"]