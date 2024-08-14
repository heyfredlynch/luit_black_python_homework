import boto3

subnet_id = "subnet-01b97e6d1fe3dd625"

ec2 = boto3.client('ec2')

ec2.delete_subnet(
    SubnetId=subnet_id,
)