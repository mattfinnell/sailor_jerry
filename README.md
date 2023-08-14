# Sailor Jerry

Download Tracks from Streaming Platforms. AKA _"Bootlegging"_ hence the name "Sailor Jerry". Currently only works with Youtube if the video doesn't have any age restrictions.

## Example Usages

NOTE : Requires [pipenv](https://pipenv.pypa.io/en/latest/). Get this, and all python versioning and package management will be handled.


```sh
git clone git@github.com:mattfinnell/sailor_jerry.git
cd sailor_jerry
pipenv install

# One Liner
pipenv run python3 youtube_downloader.py youtube https://www.youtube.com/watch?v=dQw4w9WgXcQ

# (alternative) Enter within the pipenv shell
pipenv shell
python3 youtube_downloader.py youtube https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

## Todo / Considerations

- Specify an output directory
- Cleanup video files
- Cache Results
- Get all videos and audio streams + codecs > sort > take best candidate
- Get past the AgeRestrictedError
- Parallel Batch Download
- Turn into an Ableton Max4Live Utility
- Other downloaders
  - Spotify
  - Soundcloud
  - Vimeo
  - Bandcamp
