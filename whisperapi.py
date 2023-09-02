import openai
import os

def saveLyrics(mp3_path,output_dir):
    openai.api_key = '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'
    audio_file= open(mp3_path, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)['text']
    text_file = open(os.path.join(output_dir,'vocals.txt'), "w")
    text_file.write("%s" % transcript)
    text_file.close()