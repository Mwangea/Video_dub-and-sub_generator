from vosk import Model, KaldiRecognizer, SetLogLevel
import wave
import json

def transcribe(audio_path):
    SetLogLevel(-1)
    
    model = Model("vosk-model-en-us-0.22")
    
    wf = wave.open(audio_path, "rb")
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)
    
    transcription = []
    
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            transcription.append(result['text'])
    
    final_result = json.loads(rec.FinalResult())
    transcription.append(final_result['text'])
    
    return ' '.join(transcription)