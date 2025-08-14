import boto3
import os

session = boto3.session.Session()
client = session.client(
    's3',
    region_name='blr1',
    endpoint_url='https://blr1.digitaloceanspaces.com',
    aws_access_key_id='DO00UC993LWATBC7GWUC',
    aws_secret_access_key='Q5gzB0PKieU9Q93ubg/tb3U2rqGubWS43yP5//st090'
)

bucket_name = 'techmier'
prefix = ''  # if you want a subdirectory
local_dir = './downloaded'

# --- Test Listing First ---
response = client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

if 'Contents' not in response:
    print("❌ No files found. Check your 'prefix' or bucket name.")
    exit()


# --- Paginator for All Files ---
paginator = client.get_paginator('list_objects_v2')

print(f"🔍 Scanning and downloading all files from '{bucket_name}'...")

total = 0
for page in paginator.paginate(Bucket=bucket_name, Prefix=prefix):
    contents = page.get('Contents', [])
    for obj in contents:
        key = obj['Key']
        dest_path = os.path.join(local_dir, key)
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        client.download_file(bucket_name, key, dest_path)
        print(f"✅ Downloaded: {key}")
        total += 1

print(f"\n🎉 Done! {total} files downloaded to '{local_dir}'.")
