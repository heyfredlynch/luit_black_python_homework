import boto3
from list_objects import list_object_keys

def delete_object(client, bucket, key):
    response = client.delete_object(
        Bucket=bucket,
        Key=key
    )
    return response

def delete_objects(client, bucket, keys):
    objects = [{'Key': key} for key in keys]

    response = client.delete_objects(
        Bucket=bucket,
        Delete={
            'Objects': objects
        }
    )

    return response

if __name__ == '__main__':
    bucket = 'flynch-boto3-08-10-2024'
    s3 = boto3.client('s3')
    
    prefix = "folder/foldera/"

    # Get the list of object keys in the specified prefix
    keys = list_object_keys(s3, bucket, prefix=prefix)

    # Filter out directories by ensuring keys don't end with a '/'
    keys = [key for key in keys if not key.endswith('/')]
    print(f"Keys to delete: {keys}")
    
    if keys:
        delete_response = delete_objects(s3, bucket, keys)
        print(f"Delete response: {delete_response}")
    else:
        print("No files found to delete.")
