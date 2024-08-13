import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_internet_gateways()

for ig in response["InternetGateways"]:
    print(ig["InternetGatewayId"]) 
    for attachement  in ig["Attachments"]:
        print(attachement["VpcId"], attachement["State"]) 
