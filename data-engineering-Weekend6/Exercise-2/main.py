import os
import requests
import re
import pandas as pd
from datetime import datetime

def main():
    # URL of the page to scrape
    url = 'https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/'

    # Target timestamp to search for
    target_timestamp = '2024-01-19 10:27'
    target_datetime = datetime.strptime(target_timestamp, '%Y-%m-%d %H:%M')

    # Regular expression to find file links and their timestamps
    pattern = r'<a href="([^"]+)"[^>]*>([^<]+)</a>.*?(\d{4}-\d{2}-\d{2} \d{2}:\d{2})'

    # Send GET request to fetch the page
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for any bad status

    # Find all matches for the file names and timestamps
    matches = re.findall(pattern, response.text, re.DOTALL)

    # Find the file corresponding to the target timestamp
    file_name = None
    for file_link, link_text, modification_time in matches:
        try:
            # Parse the modification time
            file_datetime = datetime.strptime(modification_time, '%Y-%m-%d %H:%M')
            
            if file_datetime == target_datetime:
                file_name = file_link
                print(f"Found file: {file_name}")
                break
        except ValueError:
            # Skip if the time is not in the correct format
            continue

    if not file_name:
        print("File with the specified timestamp not found.")
        return

    # Step 2: Download the file
    file_url = f'https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/{file_name}'
    download_response = requests.get(file_url)
    download_response.raise_for_status()  # Ensure the download was successful

    # Save the file locally
    local_file_path = file_name.split('/')[-1]  # Extract file name from URL
    with open(local_file_path, 'wb') as file:
        file.write(download_response.content)

    print(f"File downloaded as {local_file_path}")

    # Step 3: Load the file into Pandas
    # Assuming the file is in CSV format (if not, you'll need to adjust accordingly)
    df = pd.read_csv(local_file_path)

    # Step 4: Find the record(s) with the highest HourlyDryBulbTemperature
    max_temp_record = df.loc[df['HourlyDryBulbTemperature'].idxmax()]

    # Print the record(s) with the highest HourlyDryBulbTemperature
    print("Record(s) with the highest HourlyDryBulbTemperature:")
    print(max_temp_record)

if __name__ == "__main__":
    main()
