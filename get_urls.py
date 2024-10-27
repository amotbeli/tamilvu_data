
import json

import json

# Load the JSON data
with open('tamilvu_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract all download links
download_links = [entry.get("download link") for entry in data if "download link" in entry]

# Write download links to a new text file
with open('download_links.txt', 'w', encoding='utf-8') as file:
    for link in download_links:
        if len(link) > 5:
            file.write(link + '\n')

print("Download links have been written to download_links.txt")
