from flask import Flask, render_template, request, jsonify, send_file
from werkzeug.utils import secure_filename
import os
from utils import video_processor, speech_recognition, translation, text_to_speech, subtitle_generator, audio_video_mixer
import config

app = Flask(__name__)
app.config.from_object(config.Config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_video():
    if 'video' not in request.files:
        return jsonify({'error': 'No video file provided'}), 400
    
    video = request.files['video']
    target_language = request.form.get('target_language', 'en')
    
    if video.filename == '':
        return jsonify({'error': 'No video file selected'}), 400
    
    if video and video_processor.allowed_file(video.filename):
        filename = secure_filename(video.filename)
        video_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        video.save(video_path)
        
        try:
            # Extract audio from video
            audio_path = video_processor.extract_audio(video_path)
            
            # Transcribe audio
            transcription = speech_recognition.transcribe(audio_path)
            
            # Translate text
            translated_text = translation.translate(transcription, target_language)
            if translated_text == transcription:
                raise Exception("Translation failed or returned original text")
            
            # Generate dubbed audio
            dubbed_audio_path = text_to_speech.generate(translated_text, target_language)
            
            # Generate subtitles
            subtitle_path = subtitle_generator.generate(translated_text, video_path)
            
            # Mix dubbed audio with original video
            output_video_path = audio_video_mixer.mix(video_path, dubbed_audio_path, subtitle_path)
            
            result = {
                'output_video': output_video_path,
                'subtitles': subtitle_path
            }
            
            return jsonify(result)
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/download/<path:filename>')
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)