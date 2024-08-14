import boto3

vpc_id = "vpc-0ae634672d6ea93de"

ec2 = boto3.client('ec2')

ec2.delete_vpc(
    VpcId=vpc_id,
)