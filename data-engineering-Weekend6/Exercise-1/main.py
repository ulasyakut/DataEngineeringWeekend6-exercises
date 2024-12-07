import os
import requests
import zipfile
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

# List of URLs to download
urls = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
    ""  # Empty URL for testing error handling
]

# Directory to save downloads
download_dir = Path("Exercise-1/downloads")

# Create the downloads directory if it doesn't exist
def create_directory():
    download_dir.mkdir(parents=True, exist_ok=True)

# Download a file and extract it
def download_and_extract_file(url):
    if not url:  # Skip empty URLs
        print("Skipping empty URL")
        return

    filename = url.split("/")[-1]
    file_path = download_dir / filename

    try:
        # Download the file
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        with open(file_path, "wb") as f:
            f.write(response.content)

        # Extract the zip file
        try:
            with zipfile.ZipFile(file_path, "r") as zip_ref:
                zip_ref.extractall(download_dir)
        except zipfile.BadZipFile:
            print(f"Error: {filename} is not a valid zip file.")
        finally:
            # Delete the zip file
            if file_path.exists():
                file_path.unlink()

    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")

# Multithreaded download
def download_files_threadpool():
    with ThreadPoolExecutor() as executor:
        executor.map(download_and_extract_file, urls)

# Main function
def main():
    create_directory()

    # Synchronous download
    print("Starting synchronous downloads...")
    for url in urls:
        download_and_extract_file(url)

    # Multithreaded download
    print("Starting multithreaded downloads...")
    download_files_threadpool()

if __name__ == "__main__":
    main()
