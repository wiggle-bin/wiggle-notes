import requests
import time
import os

def fetch_zip_file_list(url):
    """
    Fetch the list of zip files from the given URL.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return []

def download_file(url, filename):
    """
    Download a file from a given URL and save it to the local filesystem.
    """
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)

# URL to fetch the list of zip files
data_url = "http://wigglebin.local:5000/zips/hourly"

# Fetch the list of zip files
zip_files = fetch_zip_file_list(data_url)

# Ensure the download directory exists
download_dir = "downloads"
os.makedirs(download_dir, exist_ok=True)

# Download each file with a delay
for item in zip_files:
    file_name = item['name']
    file_path = item['path']
    local_file_path = os.path.join(download_dir, f"{file_name}.zip")
    
    # Check if the file already exists
    if not os.path.exists(local_file_path):
        print(f"Downloading {file_name}...")
        download_file(file_path, local_file_path)
        print(f"Downloaded {file_name} successfully.")
        time.sleep(2)  # Delay for 2 seconds
    else:
        print(f"File {file_name} already exists. Skipping download.")