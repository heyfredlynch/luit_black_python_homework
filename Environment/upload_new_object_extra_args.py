import boto3

s3 = boto3.client('s3')

s3.put_object(Bucket="flynch-boto3-08-10-2024", Key="test_text_string.txt", Body="Hey this is a string", ContentType="text/plain") 
