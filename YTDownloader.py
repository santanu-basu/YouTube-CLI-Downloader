import pytube
import os
import sys
import re

# Check for command line argument
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    # Prompt the user to input the YouTube URL
    url = input("Enter the YouTube URL: ")

# Extract the URL until the video ID
match = re.search(r"(https://www.youtube.com/watch\?v=[^&]+)", url)
if match:
    url = match.group(1)
else:
    print("Error: Invalid YouTube URL format.")
    sys.exit(1)

# Show downloading message
print("Downloading...")

# Create YouTube object
yt = pytube.YouTube(url)

# Get the first stream with a resolution of 720p that contains both audio and video
video = yt.streams.filter(res="720p", progressive=True).first()

# Set the output directory to the current working directory
output_dir = os.getcwd()

# Download the video
video.download(output_dir)

# Get the full path of the downloaded file
downloaded_file = os.path.join(output_dir, video.default_filename)

# Print the full path of the downloaded file
print(f"Downloaded: {downloaded_file}")
