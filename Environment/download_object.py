import boto3
import os 
from list_objects import list_object_keys

def download_single_object(client, bucket, key, Filename):
    client.download_file(bucket, key, filename) 

if __name__ == '__main__':

    bucket = 'flynch-boto3-08-10-2024'
    key = 'test_text_string.txt'
    filename = 'test_text_string.txt' 

    s3 = boto3.client('s3')

    keys = list_object_keys(s3, bucket, prefix= "folder/")  

    for key in keys:
        if '/' == key[-1]:
            try:
                os.mkdir(key)
            except:
                pass 
        else:
            download_single_object(s3, bucket, key, key) 