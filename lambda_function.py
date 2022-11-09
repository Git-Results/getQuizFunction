import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
  client = boto3.resource('dynamodb', region_name='us-east-1')
  table = client.Table('gitCCP_quiz')   
  response =table.scan()
  items=response['Items']
  print(items)
  
  return {
    'isBase64Encoded': False,
    'headers': { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': 'http://my-static-bucket-jenkins.s3-website-us-east-1.amazonaws.com' },
    'statusCode': 200,
    'body': json.dumps(items)
  }
