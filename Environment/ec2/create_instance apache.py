import boto3

def create_instance(client, ami_id, security_group_id, key_pair_name, user_data=None):
    try:
        response = client.run_instances(
            ImageId=ami_id,
            InstanceType='t2.micro',
            KeyName=key_pair_name,
            MaxCount=1,
            MinCount=1,
            SecurityGroupIds=[security_group_id],
            UserData=user_data
        )
        instance_id = response["Instances"][0]["InstanceId"]
        print(f"Instance created successfully. Instance ID: {instance_id}")
        return instance_id
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

ami_id = "ami-0dfcc9db34628d548"
key_pair_name = "Key-from-boto3"
security_group_id = "sg-088e82cd657a9bd10"

user_data = '''#!/bin/bash
apt update -y
apt-get install -y apache2
systemctl start apache2
systemctl enable apache2'''

# Initialize the EC2 client (optionally specifying a region)
ec2 = boto3.client('ec2', region_name='us-east-1')  # Replace with your desired region

instance_id = create_instance(ec2, ami_id, security_group_id, key_pair_name, user_data)
if instance_id:
    print(f"You can now use this instance ID for further operations: {instance_id}")