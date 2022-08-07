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
 100% ( 32.5/ 32.5MB) ├████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████┤[1/1]  612 kB/s

Downloading 【鎌倉殿の13人 (OP) 】 窥探历史的陈迹   钢琴曲【高音質】.cmt.xml ...
'''
res = p.stdout.splitlines()
song_name = final_music_name
// default format
video_format = 'flv'
for x in range(len(res)):
    print(repr(res[x]))
    fileds = x.split(":")
    if fileds[0] == 'title':
        song_name = fileds[1]
    if fileds[0] == 'container':
        video_format = fileds[1]


files = os.listdir(os.getcwd())
title = ''
fileName= ''
for file in files:
    if(file.endswith('.cmt.xml')):
        title = file.split('.')[0]
    if(file.endswith(format)):
        fileName = file
// 在 workflow 里没有指定最终音乐名称
if(len(final_music_name) == 0):
    final_music_name = song_names

my_clip = mp.VideoFileClip(filename=fileName)
my_clip.audio.write_audiofile(final_music_name + ".mp3")
my_clip.close()


f = open('song_name.txt','w+')
f.write(final_music_name + '.mp3' )
f.close()
