import boto3
import os

# DigitalOcean Space details
SPACE_NAME = 'techmier'
ACCESS_KEY = 'DO00UC993LWATBC7GWUC'
SECRET_KEY = 'Q5gzB0PKieU9Q93ubg/tb3U2rqGubWS43yP5//st090'
ENDPOINT_URL = 'https://blr1.digitaloceanspaces.com'

# Local directory to save files
LOCAL_DIRECTORY = './downloaded'

# Initialize boto3 client
s3 = boto3.client('s3', endpoint_url=ENDPOINT_URL,
                  aws_access_key_id=ACCESS_KEY,
                  aws_secret_access_key=SECRET_KEY)

def download_files_from_space(space_folder=''):
    # List all objects in the space folder
    response = s3.list_objects_v2(Bucket=SPACE_NAME, Prefix=space_folder)

    # Check if there are any objects
    if 'Contents' in response:
        objects = response['Contents']

        # Download each object
        for obj in objects:
            key = obj['Key']
            if key.endswith('/'):
                # It's a folder, create local folder and recursively download its content
                folder_name = key.rstrip('/')
                next_space_folder = os.path.join(space_folder, folder_name)
                download_files_from_space(next_space_folder)
            else:
                # It's a file, download it
                local_file_path = os.path.join(LOCAL_DIRECTORY, key)
                os.makedirs(os.path.dirname(local_file_path), exist_ok=True)  # Create parent directory if not exists
                print(f"Downloading {key}...")
                s3.download_file(SPACE_NAME, key, local_file_path)
                print(f"Downloaded {key} to {local_file_path}")
    else:
        print(f"No objects found in folder: {space_folder}")

if __name__ == "__main__":
    download_files_from_space()