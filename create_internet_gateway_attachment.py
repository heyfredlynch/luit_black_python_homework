import boto3

internet_gateway_id = "igw-0cd2b3c08e105fb35"
vpc_id = "vpc-0ae634672d6ea93de"

ec2 = boto3.client('ec2')

ec2.attach_internet_gateway(
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_id,
)