import os

class Config:
    UPLOAD_FOLDER = 'uploads'
    OUTPUT_FOLDER = 'output'
    SUBTITLE_FOLDER = 'subtitles'
    ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv'}
    MAX_CONTENT_LENGTH = 500 * 1024 * 1024  # 500 MB limit

    # Ensure necessary directories exist
    for folder in [UPLOAD_FOLDER, OUTPUT_FOLDER, SUBTITLE_FOLDER]:
        os.makedirs(folder, exist_ok=True)