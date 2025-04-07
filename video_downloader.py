import yt_dlp

import tkinter as tk
from tkinter import ttk, messagebox

def download_video():
    url = url_entry.get()
    output_path='./'
    ydl_opts = {
        'outtmpl': f'{output_path}%(title)s.%(ext)s',  # Output template
        'quiet': True,                                    # Suppress verbose output
        # 'no_warnings': True,                              # Hide warnings
        'format': 'bestvideo+bestaudio/best',             # Best quality
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            print(f"Downloaded: {info.get('title', 'Untitled')}")
            return True
    except Exception as e:
        print(f"Error downloading video: {e}")
        return False

# Example usage
if __name__ == "__main__":
    # video_url = input("Enter video URL: ")

    # Create the main window
    root = tk.Tk()
    root.title("YouTube Video Downloader")
    root.geometry("400x150")

    # URL Entry
    url_label = tk.Label(root, text="Enter Video URL:")
    url_label.pack(pady=5)
    url_entry = tk.Entry(root, width=50)
    url_entry.pack(pady=5)

    # Download Button
    download_button = tk.Button(root, text="Download", command=download_video)
    download_button.pack(pady=10)

    root.mainloop()
    # download_video(video_url)