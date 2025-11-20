import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("BlogPosts")

def lambda_handler(event, context):
    try:
        body = json.loads(event["body"])

        post_id = str(uuid.uuid4())
        title = body["title"]
        content = body["content"]
        image_url = body["imageUrl"]
        created_at = datetime.utcnow().isoformat()

        item = {
            "postId": post_id,
            "title": title,
            "content": content,
            "imageUrl": image_url,
            "createdAt": created_at
        }

        table.put_item(Item=item)

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps(item)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": str(e)})
        }
