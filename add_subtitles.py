from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
import pysubs2
import os

def add_subtitles_to_video(input_video, subtitle_path, output_path):
    # Load the video file
    video = VideoFileClip(input_video)
    
    # Load the subtitles using pysubs2
    subs = pysubs2.load(subtitle_path)

    # Prepare a list to hold video and subtitle clips
    clips = [video]

    # Path to the Lobster font
    font_path = os.path.join("fonts", "Lobster-Regular.ttf")

    # Process each subtitle
    for sub in subs:
        # Create the text clip for each subtitle with the Lobster font
        txt_clip = TextClip(
            sub.text,
            fontsize=40,
            color='white',
            bg_color='black',
            font=font_path  # Use the custom Lobster font
        ).set_position("center").set_start(sub.start / 1000).set_duration((sub.end - sub.start) / 1000)  # Duration in seconds

        clips.append(txt_clip)

    # Combine the video and subtitle clips
    final = CompositeVideoClip(clips)

    # Write the final video to the specified output path
    final.write_videofile(output_path, codec='libx264', audio_codec='aac')

