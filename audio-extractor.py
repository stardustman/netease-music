#/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import os
import moviepy.editor as mp

# VIDEO_LINK from github actions
# FINAL_MUSIC_NAME from github actions

video_link = os.environ["VIDEO_LINK"]
final_music_name = os.environ["FINAL_MUSIC_NAME"]


print(video_link)
print(final_music_name)



# p = subprocess.run(["you-get", "--debug","--output-filename", final_music_name, "--no-caption", video_link],
#                    timeout=10000,
#                    capture_output=True, 
#                    encoding="utf-8")

# process = subprocess.Popen(
#        ["you-get", "--debug","--output-filename", final_music_name, "--no-caption", video_link],
#         stdout=subprocess.PIPE,
#         stderr=subprocess.PIPE
#     )
# process.wait()
# output, error = process.communicate()

# if process.returncode != 0:
#     raise Exception("File handling failed %d %s %s" % (process.returncode, output, error))

'''
you-get -O 镰仓殿的13人  --no-caption   https://www.bilibili.com/video/BV1KY411g7iA
site:                Bilibili
title:               【鎌倉殿の13人 (OP) 】 窥探历史的陈迹   钢琴曲【高音質】
stream:
    - format:        flv
      container:     flv
      quality:       高清 1080P
      size:          32.5 MiB (34072623 bytes)
    # download-with: you-get --format=flv [URL]

Downloading 镰仓殿的13人.flv ...
 100% ( 32.5/ 32.5MB) ├███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████┤[1/1]  770 kB/s

Skipping captions or danmaku.
'''

files = os.listdir(os.getcwd())
fileName = ''
for file in files:
    print(file)
    if(file.startswith(final_music_name)):
        fileName = file
        break

my_clip = mp.VideoFileClip(filename=fileName)
my_clip.audio.write_audiofile(final_music_name + ".mp3")
my_clip.close()


f = open('song_name.txt','w+')
f.write(final_music_name + '.mp3' )
f.close()
