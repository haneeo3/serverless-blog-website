import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("BlogPosts")

def lambda_handler(event, context):
    try:
        response = table.scan()
        posts = response.get("Items", [])

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps(posts)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": str(e)})
        }
