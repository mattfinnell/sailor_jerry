import click

from pprint import pprint
from pytube import YouTube
from moviepy.editor import VideoFileClip


def download_track(url):
    youtube_video = YouTube(url)

    streams: List[pytube.Stream] = youtube_video.streams \
        .filter(mime_type="video/mp4") \
        .filter(video_codec="avc1.64001F") \
        .filter(res="720p") # TODO: Scan through lowest tolerable resolution available (720p ... 8k)

    for stream in streams:
        video_output_path = ".artifacts"
        video_file_name = "outfile.mp4"
        video_file_path = f"{video_output_path}/{video_file_name}"

        stream.download(
            output_path=video_output_path,
            filename=video_file_name
        )

        video_file = VideoFileClip(video_file_path)

        if not video_file.audio:
            pprint(f"Stream {stream} has no associated audio...")
            continue

        video_file.audio.write_audiofile(
            f"{youtube_video.title}.mp3"
        )

@click.group()
def cli():
    pass

@cli.command()
@click.argument('url')
def youtube(url: str):
    download_track(url)

if __name__ == "__main__":
    cli()