"""A simple YouTube video downloader using pytubefix and tkinter for file dialog."""
import tkinter as tk
from tkinter import filedialog
from pytubefix import YouTube 

def download_video(url, save_path):
    """Download a YouTube video from the given URL to the specified save path."""
    try:
        yt = YouTube(url)
        # 'progressive=True' contains both audio and video, but usually maxes at 720p
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_quality_stream = streams.get_highest_resolution()
        
        print(f"Downloading '{yt.title}'...")
        highest_quality_stream.download(output_path=save_path)
        print(f"Video downloaded successfully to {save_path}")

    except Exception as e:
        print(f"Error: {e}")

def open_file_dialog():
    """Open a file dialog to select a directory."""
    print("Opening file dialog...")
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # This line hides the main tkinter window
    root.attributes('-topmost', True)

    video_url = input("Enter the YouTube video URL: ")
    
    print("Please select a directory to save the video.")
    save_directory = open_file_dialog()

    if save_directory:
        download_video(video_url, save_directory)
    else:
        print("Please select a valid directory to save the video.")
