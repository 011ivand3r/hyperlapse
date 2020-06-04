import os
from moviepy.editor import *
from PIL import Image

ABS_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(ABS_PATH)

clip = VideoFileClip("input video filename .mp4") # input video filename
source_audio_path = os.path.join(BASE_DIR, '.mp3 filename')  # mp3 filename
opening_text = "Treble" # opening text

timeLapse_dir = os.path.join(BASE_DIR, "timeLapse_dir")
final_audio_video_path = os.path.join(BASE_DIR, 'output filename .mp4') # output filename

os.makedirs(timeLapse_dir, exist_ok=True)


fps = clip.reader.fps

for i, frame in enumerate(clip.iter_frames()):
    fphs = int(fps/1) # change the denominator for the frequency of photos you want to take
    if i % fphs == 0 :
        current_ms = int((i / fps) * 1000)
        newimg_filepath = os.path.join(timeLapse_dir, f"{current_ms}.jpg")
        newimg = Image.fromarray(frame)
        newimg.save(newimg_filepath)

directory = {}

for root, dirs, files in os.walk(timeLapse_dir):
    for _file in files:
        filepath = os.path.join(root, _file)
        try:
            key = float(_file.replace(".jpg", ""))
        except:
             key = None
        if key != None:
            directory[key] = filepath

new_paths = []
for k in sorted(directory.keys()):
    filepath = directory[k]
    new_paths.append(filepath)
    
clip = ImageSequenceClip(new_paths, fps=30) 


intro_duration = 4
intro_text = TextClip(
    opening_text,
    size=clip.size,
    fontsize=150,
    color = "#fff",
    bg_color= "transparent",
    font= "Segoe-UI-Light",
    kerning=25
)
intro_text = intro_text.set_duration(intro_duration)
intro_text = intro_text.set_fps(fps)
intro_text = intro_text.set_pos("center")

final_clip = concatenate_videoclips([intro_text, clip]) #final video clip

duration = final_clip.duration
bg_audio = AudioFileClip(source_audio_path)
bg_music = bg_audio.subclip(0, duration)
bg_music = bg_music.volumex(1.5)

final_av_clip = final_clip.set_audio(bg_music)
final_av_clip.write_videofile(final_audio_video_path) # final audio added clip
