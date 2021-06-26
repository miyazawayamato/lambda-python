import boto3
dynamoDB = boto3.resource('dynamodb')
table= dynamoDB.Table('todo')

def lambda_handler(event, context):
    
    res = table.delete_item(
        Key = {
            'yearmonth': event['yearmonth'],
            'daytime': event['daytime'],
        }
    )
    
    return res