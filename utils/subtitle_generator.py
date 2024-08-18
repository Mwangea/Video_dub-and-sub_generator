import pysrt
from moviepy.editor import VideoFileClip
import os
from config import Config

def generate(text, video_path):
    video = VideoFileClip(video_path)
    duration = video.duration
    
    subs = pysrt.SubRipFile()
    
    # Split text into sentences and create subtitles
    sentences = text.split('. ')
    time_per_sentence = duration / len(sentences)
    
    for i, sentence in enumerate(sentences):
        start_time = i * time_per_sentence
        end_time = (i + 1) * time_per_sentence
        
        sub = pysrt.SubRipItem(
            index=i+1,
            start=pysrt.SubRipTime(seconds=start_time),
            end=pysrt.SubRipTime(seconds=end_time),
            text=sentence
        )
        subs.append(sub)
    
    output_path = os.path.join(Config.SUBTITLE_FOLDER, "subtitles.srt")
    subs.save(output_path, encoding='utf-8')
    return output_path