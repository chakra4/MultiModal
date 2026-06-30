#!/usr/bin/env python3
"""
YouTube Video Downloader Script
Downloads a video from YouTube using yt-dlp library.
"""

import sys
import subprocess

def check_and_install_ytdlp():
    """Check if yt-dlp is installed, if not provide installation instructions."""
    try:
        import yt_dlp
        return True
    except ImportError:
        print("yt-dlp is not installed.")
        print("\nTo install yt-dlp, run:")
        print("  pip install yt-dlp")
        print("\nOr with pip3:")
        print("  pip3 install yt-dlp")
        return False

def download_video(url, output_path='./downloads'):
    """
    Download a YouTube video.
    
    Args:
        url (str): YouTube video URL
        output_path (str): Directory to save the downloaded video
    """
    import yt_dlp
    
    # Configure download options
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'quiet': False,
        'no_warnings': False,
    }
    
    try:
        print(f"Downloading video from: {url}")
        print(f"Output directory: {output_path}\n")
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Get video info
            info = ydl.extract_info(url, download=False)
            print(f"Title: {info.get('title', 'Unknown')}")
            print(f"Duration: {info.get('duration', 0)} seconds")
            print(f"Uploader: {info.get('uploader', 'Unknown')}\n")
            
            # Download the video
            print("Starting download...")
            ydl.download([url])
            
        print("\n✓ Download completed successfully!")
        
    except Exception as e:
        print(f"\n✗ Error downloading video: {str(e)}")
        sys.exit(1)

def main():
    """Main function to run the video downloader."""
    # Check if yt-dlp is installed
    if not check_and_install_ytdlp():
        sys.exit(1)
    
    # YouTube video URL
    #video_url = "https://www.youtube.com/watch?v=84id2dzpwU0"
    video_url = "https://www.youtube.com/watch?v=5GeAORj0Nw0"

    # Download the video
    download_video(video_url)

if __name__ == "__main__":
    main()

# Made with Bob
