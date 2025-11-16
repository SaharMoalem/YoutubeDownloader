import os
import tkinter as tk
from tkinter import filedialog
import yt_dlp

def download_video(url, path):
    outtmpl = os.path.join(path, '%(title)s.%(ext)s')
    ydl_opts = {
        'outtmpl': outtmpl,
        'format': 'best[ext=mp4]/best',
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get('title', url)
            print(f"Download completed: {title}")
    except Exception as e:
        print(f"Download failed: {e}")

def browse_directory():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    directory = filedialog.askdirectory()
    root.destroy()

    if directory:
        print(f"Selected directory: {directory}")

    return directory

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_path = browse_directory()
    
    if download_path:
        print("Starting download...")
        download_video(video_url, download_path)
    else:
        print("No directory selected. Exiting.")