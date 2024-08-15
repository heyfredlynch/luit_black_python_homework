import boto3

ami_id = "ami-0dfcc9db34628d548"  # AMI ID to use for launching the instance
key_pair_name = "Key-from-boto3"  # Name of the key pair (must match exactly)
security_group_id = "sg-088e82cd657a9bd10"  # Security group ID for the instance

# Initialize the EC2 client
ec2 = boto3.client('ec2')

# Run an EC2 instance
response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType='t2.micro',  # Instance type (t2.micro is within the free tier)
    KeyName=key_pair_name,
    MaxCount=1,  # Launch exactly 1 instance
    MinCount=1,
    SecurityGroupIds=[
        security_group_id,
    ]
)

# Print the response to see the details of the launched instance
print(response["Instances"][0]["InstanceId"]) 
