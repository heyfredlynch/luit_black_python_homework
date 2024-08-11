import boto3

s3 = boto3.client('s3')

bucket = "flynch-boto3-08-10-2024"
key = "test_text.txt"

# Update Public Access Block configuration
response = s3.put_public_access_block(
    Bucket=bucket,
    PublicAccessBlockConfiguration={
        'BlockPublicAcls': False,
        'IgnorePublicAcls': False,
        'BlockPublicPolicy': False,
        'RestrictPublicBuckets': False
    },
    # Uncomment or set the ExpectedBucketOwner value if needed
    # ExpectedBucketOwner='string'  
)
print("Public Access Block response:", response)

# Update Bucket Ownership Controls
response = s3.put_bucket_ownership_controls(
    Bucket=bucket,
    OwnershipControls={
        'Rules': [
            {
                'ObjectOwnership': 'BucketOwnerPreferred'
            },
        ]
    }
)
print("Bucket Ownership Controls response:", response)

# Set Bucket ACL
response = s3.put_bucket_acl(
    ACL='private',
    Bucket=bucket  # Fixed missing comma
)
print("Bucket ACL response:", response)

# Set Object ACL
response = s3.put_object_acl(
    ACL='public-read',
    Bucket=bucket,
    Key=key
)
print("Object ACL response:", response)
