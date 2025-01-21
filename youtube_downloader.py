import yt_dlp
import tkinter as tk
from tkinter import messagebox, filedialog


def download_video():
    url = url_entry.get()  # Get the URL from the input box
    download_path = filedialog.askdirectory()  # Ask user to select a folder

    if not url or not download_path:
        messagebox.showerror("Error", "Please provide a valid URL and select a folder.")
        return

    # yt-dlp options
    options = {
        'format': 'best',  # Download the best quality
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',  # Output template for filenames
    }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])  # Download the video
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


# GUI setup
root = tk.Tk()
root.title("YouTube Downloader")

# Input field for URL
tk.Label(root, text="Enter YouTube Video URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Download button
download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack(pady=10)

root.mainloop()
