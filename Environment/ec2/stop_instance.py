import boto3

# Create Ec2
ec2 = boto3.client('ec2')

# Specify the instance you want to shut down
instance_id = "i-0e81c6a831b5e8bce" 

# Command the Ec2 instance to stop
response = ec2.stop_instances(
    InstanceIds=[
        instance_id,
        ],
)

print(response)