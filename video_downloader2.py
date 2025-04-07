import tkinter as tk
from tkinter import ttk, messagebox
import yt_dlp
import threading

# Function to handle video download
def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a valid URL.")
        return

    # Disable the download button during download
    download_button.config(state=tk.DISABLED)
    progress_bar.start()

    def download_thread():
        ydl_opts = {
            'outtmpl': f'./%(title)s.%(ext)s',  # Output template
            'quiet': True,                      # Suppress verbose output
            'format': 'bestvideo+bestaudio/best',  # Best quality
            'progress_hooks': [update_progress],  # Progress hook
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                messagebox.showinfo("Success", "Download completed!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to download video: {e}")
        finally:
            progress_bar.stop()
            progress_bar['value'] = 0  # Reset progress bar
            download_button.config(state=tk.NORMAL)

    # Run the download in a separate thread to avoid freezing the UI
    threading.Thread(target=download_thread, daemon=True).start()

# Function to update progress (called by yt-dlp)
def update_progress(d):
    if d['status'] == 'downloading':
        percent_str = d.get('_percent_str', '0%').strip('%').strip()  # Remove '%' and spaces
        try:
            percent = float(percent_str)  # Convert to float
            progress_bar['value'] = percent  # Update progress bar
        except ValueError:
            pass  # Ignore invalid values
        root.update_idletasks()

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("400x150")

# URL Entry
url_label = tk.Label(root, text="Enter Video URL:")
url_label.pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Progress Bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=10)

# Download Button
download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack(pady=10)

# Run the application
root.mainloop()