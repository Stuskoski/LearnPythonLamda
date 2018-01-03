from __future__ import print_function  # Python 2/3 compatibility
import json
import datetime
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('PythonlearningTable')


def handler(event, context):
    data = {
        'output': 'Hello World',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}


def getItemsInDynamoTable(event, context):

    response = table.get_item(
        Key={
            'UNQIUE_ID': "testing123"
        }
    )

    data = {
        'output': response['Item']
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
