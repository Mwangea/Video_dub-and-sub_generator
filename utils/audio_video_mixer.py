import moviepy.config as mpc
mpc.IMAGEMAGICK_BINARY = r'C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe'

from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip, TextClip
import os
from config import Config
import pysrt
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def mix(video_path, audio_path, subtitle_path):
    logging.info("Starting video mixing process")
    logging.info(f"Video path: {video_path}")
    logging.info(f"Audio path: {audio_path}")
    logging.info(f"Subtitle path: {subtitle_path}")

    try:
        # Load video and audio files
        video = VideoFileClip(video_path)
        logging.info("Video loaded successfully")
        
        audio = AudioFileClip(audio_path)
        logging.info("Audio loaded successfully")
        
        # Log durations
        audio_duration = audio.duration
        video_duration = video.duration
        logging.info(f"Audio duration: {audio_duration} seconds")
        logging.info(f"Video duration: {video_duration} seconds")
        
        # Process audio and video
        if audio_duration < video_duration:
            logging.warning("Audio duration is shorter than video duration. Audio will be processed as is.")
            # Set audio duration to its length; remaining video will be silent
            video = video.set_audio(audio.subclip(0, audio_duration))
        else:
            video = video.set_audio(audio.subclip(0, video_duration))
        
        logging.info("Audio added to video")
        
        # Load and process subtitles
        subtitles = pysrt.open(subtitle_path)
        subtitle_clips = []

        for sub in subtitles:
            start_time = sub.start.seconds
            end_time = sub.end.seconds
            duration = end_time - start_time
            
            subtitle_clip = (TextClip(sub.text, fontsize=24, color='white', bg_color='black',
                                      font='Arial', size=(video.w, None), method='caption')
                             .set_position(('center', 'bottom'))
                             .set_duration(duration)
                             .set_start(start_time))
            
            subtitle_clips.append(subtitle_clip)
        
        logging.info("Subtitles processed")
        
        # Create composite video
        final_video = CompositeVideoClip([video] + subtitle_clips)
        logging.info("Composite video created")
        
        # Output path
        output_path = os.path.join(Config.OUTPUT_FOLDER, "output_video.mp4")
        final_video.write_videofile(output_path, codec='libx264', audio_codec='aac')
        logging.info(f"Video saved to {output_path}")
        
        return output_path

    except Exception as e:
        logging.error(f"Error in mix function: {str(e)}")
        raise
