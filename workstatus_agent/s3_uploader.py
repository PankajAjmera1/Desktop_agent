import boto3
from botocore.exceptions import NoCredentialsError

class S3Uploader:
    def __init__(self, bucket_name, aws_access_key, aws_secret_key):
        self.bucket_name = bucket_name
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key
        )

    def upload_file(self, file_path, s3_key):
        try:
            self.s3_client.upload_file(file_path, self.bucket_name, s3_key)
            print(f"File {file_path} uploaded successfully to {s3_key}.")
        except FileNotFoundError:
            print(f"The file {file_path} was not found.")
        except NoCredentialsError:
            print("Credentials not available.")