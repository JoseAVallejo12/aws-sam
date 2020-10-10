import json
import boto3


def lambda_handler(event, context):

    return {
        "statusCode": 200,
        "body": json.dumps({
            "userNew": get_user()
        })
    }


def get_user(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('customers')
    response2 = table.scan()
    items = response2['Items']
    return items