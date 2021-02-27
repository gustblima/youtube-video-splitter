from __future__ import unicode_literals
import youtube_dl
import ffmpeg
from moviepy.editor import *
import csv

def download(url, output_name, timestamp, convert_to_gif=False):
    output_path = f"output\/{output_name}\/{output_name}"
    ydl_opts = {
        "outtmpl": f"{output_path}.%(ext)s",
        "format": "mp4"
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        downloaded = ydl.download([url])
        timestamps = timestamp.split(",")
        for i in range(len(timestamps)):
            t1, t2 = timestamps[i].split("-")
            clip = (VideoFileClip(f"{output_path}.mp4").subclip(t1, t2))
            """
            ffmpeg_extract_subclip(
                filename= f"{output_full}.mp4", 
                t1=t1,
                t2=t2,
                targetname=f"{output_name}/{output_name}_{i}.mp4")
                """
            get_output_filename_with_ext = lambda ext: f"{output_path}_{t1}_{t2}.{ext}".replace(':', '')

            if convert_to_gif == 'y':
                clip.write_gif(get_output_filename_with_ext('gif'))
            else:
                try:
                    clip.write_videofile(get_output_filename_with_ext('mp4'))
                except:
                    print()

input_file = 'input.csv'
tmp_file = f"{input_file}.tmp"
with open(input_file, 'r', newline='') as csvfile, open(tmp_file, 'w+', newline='') as csvtempfile:
    writer = csv.writer(csvtempfile, delimiter='|')
    reader = csv.reader(csvfile, delimiter='|')
    for row in reader:
        output_name, url, timestamps, convert_to_gif, status = row
        if status == 'status':
            writer.writerow(row)
        elif status != 'ok':
            download(url, output_name, timestamps, convert_to_gif)
            writer.writerow([output_name, url, timestamps, convert_to_gif, 'ok'])
        else:
            writer.writerow(row)
os.remove(input_file)
os.rename(tmp_file, input_file)
                
