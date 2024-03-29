import boto3 
import os 

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
REGION_NAME = ''

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION_NAME
)

s3 = session.resource('s3')

bucket_name = ''
s3_folder = ''
local_dir = ''

def download_s3_folder(bucket_name, s3_folder, local_dir):
    bucket = s3.Bucket(bucket_name)
    for obj in bucket.objects.filter(Prefix=s3_folder):
        target = obj.key if local_dir is None \
            else os.path.join(local_dir, os.path.relpath(obj.key, s3_folder))
        if not os.path.exists(os.path.dirname(target)):
            os.makedirs(os.path.dirname(target))
        if obj.key[-1] == '/':
            continue
        print(f"Downloading {obj.key} to {target}")
        bucket.download_file(obj.key, target)

if __name__ == '__main__':
    download_s3_folder(bucket_name, s3_folder, local_dir)