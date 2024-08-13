import boto3

route_tableid = "rtb-0a25eb84df58b6897"
subnet_id = "subnet-01b97e6d1fe3dd625"

ec2 = boto3.client('ec2')

association = ec2.associate_route_table(
    RouteTableId=route_tableid,
    SubnetId=subnet_id,
)

print(association["AssociationId"])