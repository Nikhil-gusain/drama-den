# merge_audio_video.py
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
import os

def merge_audio_video(input_video, input_audio, output_path):
    video = VideoFileClip(input_video)
    audio = AudioFileClip(input_audio)
    final = video.set_audio(audio)
    final.write_videofile(output_path, codec='libx264', audio_codec='aac')
