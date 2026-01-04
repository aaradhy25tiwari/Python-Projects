"""A simple YouTube video downloader using pytubefix and tkinter for file dialog."""
import tkinter as tk
from tkinter import filedialog
from downloader import download_video

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # This line hides the main tkinter window
    root.attributes('-topmost', True)

    video_url = input("Enter the YouTube video URL: ")

    print("Please select a directory to save the video.")
    save_directory = filedialog.askdirectory()

    if save_directory:
        res = download_video(video_url, save_directory)
        if res["success"]:
            print(f"Downloaded: {res['path']}")
        else:
            print(f"Error: {res['error']}")
    else:
        print("Please select a valid directory to save the video.")
