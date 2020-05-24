# hyperlapse

This is a bot that takes a video and an audio as inputs and gives a hyperlapse/timelapse as output.

## How to use

1. Put the video & the audio file, you want to make a timelapse verion of in the same directory as timelapse.py.
2. Make another directory, "timeLapse_dir" in the same directory.
3. Input the video filename, the input audio filename and the opening_text.
4. You can change the frequency of photos on ```line 21```.
5. Run "timelapse.py" and you'll get the final video with the name "final-video.mp4".

## Dependencies

- moviepy 1.0.3
- Pillow 7.1.2
- Also install the latest version of [ImageMagick](https://imagemagick.org/script/download.php).
- If you are on Windows, then to use ImageMagick you have to manually update the "default_config.py" file in moviepy.\
Just add the following line to the file.\
```IMAGEMAGICK_BINARY = "<file\\path\\to\\magick.exe>"```

