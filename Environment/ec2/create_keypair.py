import boto3
import os

key_name = "Key-from-boto3"  # Name of the key pair to create
file_name = 'key-from-boto3.pem'  # Name of the file to save the key material

# Initialize the EC2 client
ec2 = boto3.client('ec2')

# Create a new key pair
response = ec2.create_key_pair(
    KeyName=key_name,  # Use the value of the key_name variable
)

# Write the private key to a file
with open(file_name, 'w') as f:
    f.write(response["KeyMaterial"])

# Set the file permissions to read-only for the owner
os.chmod(file_name, 0o400)
