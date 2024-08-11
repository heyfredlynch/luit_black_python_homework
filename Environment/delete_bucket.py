import boto3

def empty_bucket(client, bucket):
    response = client.list_objects_v2(Bucket=bucket)

    while response.get("Contents"):
        # Collect objects to delete
        objects = [{'Key': content["Key"]} for content in response["Contents"]]

        # Delete objects
        delete_response = client.delete_objects(
            Bucket=bucket,
            Delete={
                'Objects': objects
            }
        )
        print(f"Deleted objects: {delete_response}")

        # Check if there is more data to paginate through
        if response.get("NextContinuationToken"):
            response = client.list_objects_v2(
                Bucket=bucket, 
                ContinuationToken=response["NextContinuationToken"]
            )
        else:
            break

s3 = boto3.client('s3')
bucket = "flynch-boto3-08-10-2024"

empty_bucket(s3, bucket)

response = s3.delete_bucket(
    Bucket=bucket
)