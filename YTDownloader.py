import pytube
import os

# Ask for URL
url = input("Enter the YouTube URL: ")

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
