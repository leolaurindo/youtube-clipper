# YTClipper

YTClipper is a simple console-based Python utility that allows you to download videos and audios from YouTube and, in the process, clip it to the desired length. This tool is perfect for creating video clips or extracting audio from YouTube videos directly via URL.

I use it to extract audio from live performances that I love and then upload to my Youtube Music or Spotify account. But you may find other uses, such as creating memes, clip a Youtube video to your social media, or whatever you'd like.

## Features

- **Download Videos:** Download YouTube videos in MP4 format.
- **Convert to Audio:** Extract audio from videos and save as MP3.
- **Trim Videos:** Cut videos or audios to your specified start and end times.

## Requirements

- Python 3.6+
- yt-dlp
- moviepy

## Installation

To use `YTClipper`, you need to install the required Python libraries. You can install these dependencies via pip:

```bash
pip install yt-dlp moviepy
```

## Usage

To start using `YTClipper`, run the script from the command line:

```
python ytclipper.py
```

Follow the on-screen prompts to choose your actions:

1. Enter the YouTube URL.
2. Choose the action by the number, as it will be prompted (1. video, 2. audio, 3. trim video, 4. trim audio).
3. Specify start and end times for trimming (format: HH:MM:SS).
4. Enter the desired output filename.