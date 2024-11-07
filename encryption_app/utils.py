import boto3
from cryptography.fernet import Fernet
from django.conf import settings

def generate_encryption_key():
    return Fernet.generate_key()
    
def encrypt_file(content, key):
    fernet = Fernet(key)
    return fernet.encrypt(content)
    
def upload_to_s3(file_name, content):
    s3 = boto3.client(
    	's3',
    	aws_access_key_id = settings.AWS_ACCESS_KEY_ID,
    	aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY,
    	region_name = settings.AWS_REGION_NAME
    )
    s3.put_object(Bucket = settings.AWS_STORAGE_BUCKET_NAME, Key=file_name, Body=content)
    return f"https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.{settings.AWS_REGION_NAME}.amazonaws.com/{file_name}"
