import json
import boto3
import uuid

s3 = boto3.client("s3")
BUCKET = "YOUR_BUCKET_NAME"

def lambda_handler(event, context):
    try:
        image_id = str(uuid.uuid4())
        key = f"uploads/{image_id}.jpg"

        url = s3.generate_presigned_url(
            "put_object",
            Params={"Bucket": BUCKET, "Key": key, "ContentType": "image/jpeg"},
            ExpiresIn=300
        )

        image_url = f"https://{BUCKET}.s3.amazonaws.com/{key}"

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "uploadUrl": url,
                "imageUrl": image_url
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": str(e)})
        }
