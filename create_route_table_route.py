import boto3

route_table_ide = "rtb-0a25eb84df58b6897"
internet_gateway_id = "igw-0cd2b3c08e105fb35"

ec2 = boto3.client('ec2')

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internet_gateway_id,
    RouteTableId=route_table_ide,
)
