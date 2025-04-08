# 🎥 VideoDownloader
VideoDownloader is a Python-based tool that lets you download videos from platforms like YouTube, Instagram, and more — all in the most convenient way possible! 🚀

# ⚙️ Setup Instructions
🔹 Create and Activate Virtual Environment

# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Install Required Dependencies

pip install -r requirements.txt

# ▶️ How to Use
🔸 Run the Video Downloader using below command.

python video_downloader.py

🔸 Run with Progress Bar using below command.

python video_downloader2.py

# ❗Troubleshooting: Video Format / Media Not Supported?
If you encounter issues like unsupported media formats or conversion errors, make sure FFmpeg is installed properly.

✅ Install FFmpeg (Windows)
1. Download FFmpeg

Go to 👉 https://ffmpeg.org/download.html
Click on Windows → Get packages → Windows builds by gyan.dev
Download the "Essentials" ZIP

2. Extract it

Extract to a location like: C:\ffmpeg

3. Add FFmpeg to PATH

Open Start Menu → Environment Variables
Under System Variables, find and edit the Path variable
Add: C:\ffmpeg\bin
Click OK and restart your terminal/PC

# 📬 Feedback & Contributions
Feel free to open issues or pull requests if you'd like to contribute or run into any problems. Let's make video downloading even easier, together! 🙌
