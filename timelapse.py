from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image

source_path = os.path.join(SAMPLE_INPUTS, "###.mp4") # change the input file name
timeLapse_dir = os.path.join(SAMPLE_OUTPUTS, "timeLapse")
output_video = os.path.join(SAMPLE_OUTPUTS, "timelapse.mp4")

os.makedirs(timeLapse_dir, exist_ok=True)

clip = VideoFileClip(source_path)

print(clip.reader.fps)
print(clip.duration)
print(nframes)

# iterating through all the frames

fps = clip.reader.fps

for i, frame in enumerate(clip.iter_frames()):
    
    # change the denominator for the amount of photos you want to take
    fphs = int(fps/0.1) 
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

# change fps as per your choice
clip = ImageSequenceClip(new_paths, fps=10) 
clip.write_videofile(output_video)