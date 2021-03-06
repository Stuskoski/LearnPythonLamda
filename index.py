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
            'headers': {'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers':'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Methods': 'DELETE,GET,HEAD,OPTIONS,PATCH,POST,PUT'}}


def add_item_to_dynamo_db(event, context):
    print(context)
    return {'statusCode': 200,
            'body': json.dumps(event),
            'headers': {'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers':'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Methods': 'DELETE,GET,HEAD,OPTIONS,PATCH,POST,PUT'}}


def get_all_items_in_db(event, context):

    response = table.scan()

    data = {
        'output': response['Items']
    }

    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers':'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Methods': 'DELETE,GET,HEAD,OPTIONS,PATCH,POST,PUT'}}
