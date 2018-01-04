from __future__ import print_function  # Python 2/3 compatibility
import json
import datetime
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Testing')


def handler(event, context):
    data = {
        'output': 'Hello World',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}


def add_item_to_dynamo_db(event, context):
    print(context)
    return {'statusCode': 200,
            'body': json.dumps(event),
            'headers': {'Content-Type': 'application/json'}}


def get_all_items_in_db(event, context):

    response = table.scan()

    data = {
        'output': response['Items']
    }

    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}


def get_test_html(event, context):

    f = open("public/index.html")
    data = f.read()
    f.close()

    return {'statusCode': 200,
            'body': data,
            'headers': {'Content-Type': 'text/html'}}