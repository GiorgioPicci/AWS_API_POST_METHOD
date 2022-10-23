import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table("CARS")# IN MY CASE I CREATED A TABLE NAMED Cars but feel free to use other names ! 

def lambda_handler(event, context):
    table.put_item(Item=event)
    return  {"statusCode": 200,"Message":"A item was added to the table"}