import json

def lambda_handler(event, context):
    if event['rawPath'] == '/':
        message="Welcome to Lambda"
    elif event['rawPath'] == '/user':
        message="Welcome to User"
    elif event['rawPath'] == '/emp':
        message={"id":1,"name":"Raj","salary":10000}
    else:
        message="Invalid Path"

    return {
        'statusCode': 200,
        'body': json.dumps({"message":message})
    }
