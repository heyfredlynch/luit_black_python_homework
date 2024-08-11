import boto3

def list_object_keys(client, bucket, prefix="", extension=None):
    keys = []
    response = client.list_objects_v2(Bucket=bucket, Prefix=prefix)
    
    if "Contents" in response:
        for content in response["Contents"]:
            key = content["Key"]
            # Filter by extension if provided
            if extension is None or key.endswith(extension):
                keys.append(key)

    return keys

if __name__ == '__main__':
    s3 = boto3.client('s3')

    # Example usage without extension filter
    response = list_object_keys(s3, "flynch-boto3-08-10-2024", "folder/")
    print(response)

    # Example usage with extension filter
    response_with_filter = list_object_keys(s3, "flynch-boto3-08-10-2024", "folder/", ".txt")
    print(response_with_filter)
