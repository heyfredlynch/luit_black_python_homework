import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket='flynch-boto3-08-10-2024'
)

print(response)