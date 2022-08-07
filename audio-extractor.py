# -*- coding: utf-8 -*-
import subprocess
import os
import moviepy.editor as mp

# video_link = input('please input a video link: ')
# VIDEO_LINK from github actions
# FINAL_MUSIC_NAME from github actions
video_link = os.environ["VIDEO_LINK"]
final_music_name = os.environ["FINAL_MUSIC_NAME"]
print(video_link)

p = subprocess.run(["you-get", video_link],
                   capture_output=True, encoding="utf-8")

'''
site:                Bilibili
title:               【鎌倉殿の13人 (OP) 】 窥探历史的陈迹   钢琴曲【高音質】
stream:
    - format:        flv
      container:     flv
      quality:       高清 1080P
      size:          32.5 MiB (34072623 bytes)
    # download-with: you-get --format=flv [URL]

Downloading 【鎌倉殿の13人 (OP) 】 窥探历史的陈迹   钢琴曲【高音質】.flv ...
'''
res = p.stdout.splitlines()
# for x in range(len(res)):
    # print(res[x])

# print(len(s))
# print(res[1])

# 1. get video format
# print(res[4])
# format = (res[4].split(":")[1]).strip()
# format = ''.join([i for i in fmt if not i.isdigit()])
# print(format)

# Get the current working directory
cwd = os.getcwd()
# Get all file
# 2. get video name by xxx.cmt.xml file
files = os.listdir(os.getcwd())
title = ''
fileName= ''
for file in files:
    if(file.endswith('.cmt.xml')):
        title = file.split('.')[0]
    else:
        fileName = file


# print(format)
# fileName = cwd + '/' + title + '.' + format
if(len(final_music_name) == 0):
    final_music_name = fileName

# print("title is " + title)
# print("file path is ：" + repr(fileName))
my_clip = mp.VideoFileClip(filename=final_music_name)
my_clip.audio.write_audiofile(title + ".mp3")
my_clip.close()

os.remove(fileName)
os.remove(title + ".cmt.xml")

f = open('song_name.txt','w+')
f.write(title + '.mp3' )
f.close()
