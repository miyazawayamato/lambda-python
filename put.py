def lambda_handler(event, context):
    table.delete_item(
        Key = {
            'yearmonth': event['yearmonth'],
            'daytime': event['daytime'],
        }
    )
    table.put_item(
        Item = {
            'yearmonth': event['newearmonth'],
            'daytime': event['daytime'],
            'untilTime': event['untilTime'],
            'title': event['title'],
            'detail': event['detail'],
        }
    )
    
    return "success"