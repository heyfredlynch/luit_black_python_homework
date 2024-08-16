import boto3

ec2 = boto3.client('ec2')

response = ec2.delete_security_group(
    GroupId="sg-0653bf3d03232d148"  
)

print(response)