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
            pprint(f"Stream {stream} is being a bitch")
            continue

        video_file.audio.write_audiofile(
            f"{youtube_video.title}.mp3"
        )


if __name__ == "__main__":
    urls = [
        ################# BUSTED URLS ################
        # Broken Pipe - Dude Where's My Car
        # 'https://www.youtube.com/watch?v=G2Mbj06Ns2Y',

        # Broken Pipe - Old School (Will Ferrell)
        # 'https://www.youtube.com/watch?v=f-Ni6u5XCuQ',

        # TEST CASE - Age Restricted
        # 'https://www.youtube.com/watch?v=INNC8111kgI',

        ################# WORKING URLS ################
        # 'https://www.youtube.com/watch?v=AyiGEc6HE-w',
        # 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
        # 'https://www.youtube.com/watch?v=o3WdLtpWM_c',
        # 'https://www.youtube.com/watch?v=UePtoxDhJSw',

        # Meg tha Stallion - Yadda Yadda
        # 'https://www.youtube.com/watch?v=7PBYGu4Az8s',

        # Sia - Elastic Heart
        # 'https://www.youtube.com/watch?v=noHygl5CGEY',

        # Medasin - Wild Thoughts (Rhianna)
        # 'https://www.youtube.com/watch?v=6muAULmNpgo',

        # Flume - Highest Building
        'https://www.youtube.com/watch?v=zU8JDmnrq2o',
    ]

    for url in urls:
        download_track(url)
