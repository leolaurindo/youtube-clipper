import os
import yt_dlp as youtube_dl
from moviepy.editor import VideoFileClip

def download_video(url, output_filename):
    def hook(d):
        if d['status'] == 'finished':
            print("\nDone downloading, now converting ...")

    ydl_opts = {
        'format': 'best[ext=mp4]',
        'progress_hooks': [hook],
        'outtmpl': output_filename,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def trim(input_path, start_time, end_time, output_path, mode="video"):
    with VideoFileClip(input_path) as clip:
        start_seconds = sum(int(x) * 60 ** i for i, x in enumerate(reversed(start_time.split(":"))))
        end_seconds = sum(int(x) * 60 ** i for i, x in enumerate(reversed(end_time.split(":"))))
        trimmed = clip.subclip(start_seconds, end_seconds)

        if mode == "video":
            trimmed.write_videofile(output_path, codec='libx264')
        if mode == "audio":
            trimmed.audio.write_audiofile(output_path)
            trimmed.audio.close()

def extract_audio_from_video(video_path, output_path):
    with VideoFileClip(video_path) as video:
        video.audio.write_audiofile(output_path)
        video.audio.close()

def cleanup(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        pass

def main():
    url = input("Enter the YouTube URL: ")
    
    while True:
        choice = input("\n1. download video; \n2. download audio; \n3. download and trim video;\n4. download and trim audio;\n\nChoose an action by the number: ")
        if choice in ["1", "2", "3", "4"]:
            break
        print("Invalid choice. Please enter a number between 1 and 4.")

    output_name = input("\n Enter the output filename: ")

    if choice in ["3", "4"]:
        while True:
            start_time = input("Enter start time (HH:MM:SS): ")
            end_time = input("Enter end time (HH:MM:SS): ")
            if len(start_time.split(':')) == 3 and len(end_time.split(':')) == 3:
                try:
                    # Validate actual numbers, assuming HH, MM, SS are integers and within normal ranges
                    hours, minutes, seconds = map(int, start_time.split(':'))
                    eh, em, es = map(int, end_time.split(':'))
                    if 0 <= minutes < 60 and 0 <= seconds < 60 and 0 <= em < 60 and 0 <= es < 60:
                        break
                except ValueError:
                    # Catch conversion error if not all parts are integers
                    pass
            print("Invalid time format. Please enter the time in HH:MM:SS format.")

    if choice == "1":
        download_video(url, output_name + ".mp4")
    elif choice == "2":
        download_video(url, "temp_video.mp4")
        extract_audio_from_video("temp_video.mp4", output_name + ".mp3")
    elif choice == "3":
        download_video(url, "temp_video.mp4")
        trim("temp_video.mp4", start_time, end_time, output_name + ".mp4", mode="video")
    elif choice == "4":
        download_video(url, "temp_video.mp4")
        trim("temp_video.mp4", start_time, end_time, output_name + ".mp3", mode="audio")


if __name__ == "__main__":
    main()
    cleanup("temp_video.mp4")
