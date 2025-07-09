from moviepy.video.io.VideoFileClip import VideoFileClip

def split_video_into_shorts(input_video, output_dir, min_len=30, max_len=50, overlap=5):
    import os
    import random
    os.makedirs(output_dir, exist_ok=True)

    video = VideoFileClip(input_video)
    total_duration = video.duration

    start = 0
    part = 1

    while start + min_len < total_duration:
        duration = random.randint(min_len, max_len)
        end = min(start + duration, total_duration)

        # Modern slicing approach
        short = video.cutout(end, total_duration)  # removes after 'end'
        short = short.set_start(0).set_duration(end - start)

        output_file = os.path.join(output_dir, f"part_{part}.mp4")
        short.write_videofile(output_file, codec='libx264', audio_codec='aac')
        print(f"[✓] Created {output_file}")

        start = end - overlap
        part += 1
