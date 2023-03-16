import openai


def speech2text(api_key: str, audio_file):
    openai.api_key=api_key
    
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript["text"]