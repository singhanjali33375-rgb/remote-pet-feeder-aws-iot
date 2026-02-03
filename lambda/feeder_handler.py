import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('PetFeedingLog')

def lambda_handler(event, context):
    timestamp = datetime.utcnow().isoformat()

    table.put_item(
        Item={
            'PetId': 'Dog01',
            'Timestamp': timestamp,
            'FoodAmount': '50g',
            'Action': 'Food Dispensed'
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Food dispensed successfully')
    }
