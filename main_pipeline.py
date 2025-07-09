# main_pipeline.py

import os
from merge_audio_video import merge_audio_video
from add_subtitles import add_subtitles_to_video
from split_into_shorts import split_video_into_shorts

RAW_DIR = "raw_input"
MERGED_DIR = "merged_output"
FINAL_DIR = "final_videos"
SHORTS_DIR = "shorts"
SUBS_DIR = "subtitles"

os.makedirs(MERGED_DIR, exist_ok=True)
os.makedirs(FINAL_DIR, exist_ok=True)
os.makedirs(SHORTS_DIR, exist_ok=True)

video_path = os.path.join(RAW_DIR, "video2.mp4")
audio_path = os.path.join(RAW_DIR, "combined_output.mp3")
# subtitle_path = os.path.join(SUBS_DIR, "subs.srt")

merged_output = os.path.join(MERGED_DIR, "merged.mp4")
# final_output = os.path.join(FINAL_DIR, "final_with_subs.mp4")

print("▶️ Step 1: Merging video and voiceover...")
merge_audio_video(video_path, audio_path, merged_output)

print("▶️ Step 2: Adding subtitles...")
# add_subtitles_to_video(merged_output, subtitle_path, final_output)

print("▶️ Step 3: Splitting into shorts...")
# split_video_into_shorts(merged_output, SHORTS_DIR)

print("✅ All done.")
