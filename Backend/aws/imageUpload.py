import boto3
from fastapi import UploadFile
from dotenv import load_dotenv
import os
from mimetypes import guess_extension

load_dotenv()
S3_KEY = os.getenv('AWS_ACCESS')
S3_BUCKET = os.getenv('S3_BUCKET')
S3_HOST = os.getenv('S3_HOST')

AWS_ACCESS = os.getenv('AWS_ACCESS')
AWS_SECRET = os.getenv('AWS_SECRET')

async def upload_image(file: UploadFile, recipeId:str, fileType: str,) -> str:
    """
    Uploads an image to the S3 bucket and returns the URL of the image.
    input:
    file: the image file
    filename: the name of the file
    output:
    str: the URL of the image
    """
    prefix = 'Photos/'
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS, aws_secret_access_key=AWS_SECRET)
    #list files in Photos folder
    response = s3.list_objects_v2(Bucket=S3_BUCKET, Prefix=prefix)
    response = response.get('Contents')
    response = [file.get('Key') for file in response]
    count = 0
    filename = recipeId + guess_extension(fileType)
    while prefix + filename in response:
        count += 1
        filename = filename.split('.')
        filename = filename[0] + str(count) + '.' + filename[1]
    s3.upload_fileobj(file, S3_BUCKET, prefix +filename)
    return f"{S3_HOST}/{prefix}{filename}"

if __name__ == "__main__":
    print(upload_image( "test1.txt"))