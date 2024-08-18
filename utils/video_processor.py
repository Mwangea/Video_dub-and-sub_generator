from moviepy.editor import VideoFileClip
import os
from config import Config

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

def extract_audio(video_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio_path = os.path.join(Config.OUTPUT_FOLDER, "extracted_audio.wav")
    audio.write_audiofile(audio_path)
    return audio_path