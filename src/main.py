#!/usr/bin/env python3

"""
Reads a new-line separated file of Youtube URLs to download as `.m4a` files (read_file)
Downloads URLs using yt-dlp (https://github.com/yt-dlp/yt-dlp) into the Swim Pro directory (write_dir).

Example usage (arguments are defaulted):
$ python main.py --read /path/to/urls.txt --write /path/to/SwimPro
"""

import os
import sys
import argparse

from yt_dlp import YoutubeDL

# ==================== Constants ====================

# User's home directory
HOME = os.path.expanduser("~")

# Default file to read media URLs from
DEFAULT_READ_FILE = f"{HOME}/Downloads/youtube-urls.txt"

# Default directory to download the media files into
DEFAULT_WRITE_DIR = "/Volumes/SWIM PRO"

# ==================== Arguments ====================

def parse_arguments():
    file_name = os.path.basename(sys.argv[0])
    parser = argparse.ArgumentParser(file_name)
    parser.add_argument("--read", help="New-line separated file of Youtube URLs to download", type=str, required=False)
    parser.add_argument("--write", help="Directory to downloaded the media files into", type=str, required=False)
    return parser.parse_args()

def init_arguments():
    args = parse_arguments()

    read_file = args.read or DEFAULT_READ_FILE
    if not os.path.exists(read_file):
        raise SystemExit(f"{read_file} file does not exist")
    
    write_dir = args.write or DEFAULT_WRITE_DIR
    if not os.path.isdir(write_dir):
        raise SystemExit(f"{write_dir} directory does not exist")
    
    return (read_file, write_dir)

# ==================== Read ====================

def read_urls(read_file):
    with open(read_file, "r") as file:
        lines = [line.strip() for line in file if line != ""]
        return list(filter(lambda x: x != "", lines))
    
# ==================== Main ====================

def main():
    # Initialize the command-line arguments
    (read_file, write_dir) = init_arguments()
    
    # Extract the URLs from the file to read
    urls = read_urls(read_file)
    
    # Exit if there are no urls to download
    if len(urls) == 0:
        print(f"No URLs to download in {read_file}")
        return
    
    # Specify the configuration for the download
    youtube_dl_options = {
        "format": "mp4/bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "m4a",
        }],
        "outtmpl": f"{write_dir}/%(title)s.%(ext)s"
    }

    # Download each URL
    with YoutubeDL(youtube_dl_options) as youtube_dl:
        youtube_dl.download(urls)

if __name__ == "__main__":
    main()
