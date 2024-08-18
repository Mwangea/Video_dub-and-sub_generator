# Video Audio Mixing and Subtitling Project

## Overview

This project allows you to mix audio with video and add subtitles using MoviePy and other related tools. It provides a simple web interface using Flask for video processing, including handling subtitles and syncing audio. This README will guide you through setting up and running the project.

## features
Mix audio with video.

Add subtitles to videos.

Supports various video formats.

## Installation
1. Set Up Your Environment
Python: Ensure Python 3.7+ is installed on your system. It's recommended to use a virtual environment.
2. Install Dependencies
Clone the repository and navigate to the project directory. Install the required Python packages:
```bash
pip install -r requirements.txt
```
3. Install FFmpeg
FFmpeg is required by MoviePy for video processin
[FFmpeg](https://ffmpeg.org/download.html)
4. Install ImageMagick
[ImageMagick](https://imagemagick.org/script/download.php) is used for text rendering in MoviePy.

Windows:
Download and install from ImageMagick. Ensure you set the path to magick.exe in your code:
```bash
import moviepy.config as mpc
mpc.IMAGEMAGICK_BINARY = r'C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe'
```
5. Download and Setup [Vosk Model](https://alphacephei.com/vosk/models/vosk-model-en-us-0.22.zip)
Download the English Vosk model from Vosk Models. Extract it to your project directory.

6. Create Necessary Directories
In your project root, create the necessary directories:
```bash
mkdir uploads output subtitles
```
7. Run the Flask Application
Start the Flask application:
```bash
python app.py
```
Open a web browser and go to http://localhost:5000. Use the web interface to:

Upload a video file (supported formats: mp4, avi, mov, mkv).

Select the target language for dubbing and subtitles.

Click "Process Video" to start the conversion.

## Important Notes
Quality: This implementation uses free tools, which may not provide the highest quality results for speech recognition, translation, and text-to-speech. For higher quality, consider paid services.

Google Translate API: The implementation uses the unofficial googletrans library. For production use, consider the official Google Cloud Translation API.

Performance: Processing long videos can be memory-intensive. For production, consider implementing chunking and background processing.

Error Handling: Basic error handling is implemented. For a robust application, add more comprehensive error handling and logging.

Authentication: This project does not include user authentication or rate limiting. These should be added for public-facing applications.

Subtitle Timing: The subtitle generation is basic. For professional results, improve subtitle timing and formatting.

Codec Handling: The project may need additional preprocessing steps to handle different video codecs or formats.

## Troubleshooting
If you encounter issues:

Check Console: Review the console for error messages.

Dependencies: Ensure all dependencies are installed.

Vosk Model: Verify the Vosk model is in the correct location.

FFmpeg: Confirm FFmpeg is installed and accessible.

Feel free to ask if you need further assistance!

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
