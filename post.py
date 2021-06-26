import boto3
dynamoDB = boto3.resource('dynamodb')
table= dynamoDB.Table('todo')

def lambda_handler(event, context):
    table.put_item(
        Item = {
            'yearmonth': event['yearmonth'],
            'daytime': event['daytime'],
            'untilTime': event['untilTime'],
            'title': event['title'],
            'detail': event['detail'],
        }
    )
    
    return "success"