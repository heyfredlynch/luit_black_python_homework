import boto3

internet_gateway_id = "igw-0cd2b3c08e105fb35"

ec2 = boto3.client('ec2')

ec2.delete_internet_gateway(
    InternetGatewayId=internet_gateway_id,
)