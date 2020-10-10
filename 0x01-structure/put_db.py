import boto3
from botocore.exceptions import ClientError

def add_user(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('example01')
    response = table.put_item(
       Item={
            'orderId': '001',
            'name': 'Jose'
        }
    )


def get_user(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('example01')

    try:
        response = table.get_item(Key={'orderId': 'hola'})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print(response['Item'])
        print(table)

add_user()
get_user()