import boto3

ec2 = boto3.client('ec2')

response = ec2.create_image(
    InstanceId="i-010dc4774fddeeca9", 
    Name="Go to Ami", 
)

print(response["ImageId"])