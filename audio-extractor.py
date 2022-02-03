# -*- coding: utf-8 -*-
import subprocess
import os
import moviepy.editor as mp

# video_link = input('please input a video link: ')
# VIDEO_LINK from github actions
video_link = os.environ["VIDEO_LINK"]
print(video_link)

p = subprocess.run(["you-get", video_link],
                   capture_output=True, encoding="utf-8")

'''
site:                Bilibili
title:               【720P】Kate Bush - Cloudbusting
stream:
    - format:        flv720
      container:     flv
      quality:       高清 720P
      size:          102.9 MiB (107884110 bytes)
    # download-with: you-get --format=flv720 [URL]

Downloading 【720P】Kate Bush - Cloudbusting.flv ...
'''
res = p.stdout.splitlines()
for x in range(len(res)):
    print(res[x])

# print(res[1])

# 1. get video format
print(res[4])
format = (res[4].split(":")[1]).strip()
# format = ''.join([i for i in fmt if not i.isdigit()])
print(format)

# Get the current working directory
cwd = os.getcwd()
# Get all file
# 2. get video name by xxx.cmt.xml file
files = os.listdir(os.getcwd())
title = ''
for file in files:
    if(file.endswith('.cmt.xml')):
        title = file.split('.')[0]
        break

# print(format)
fileName = cwd + '/' + title + '.' + format

print("title is " + title)
print("file path is ：" + repr(fileName))
my_clip = mp.VideoFileClip(filename=fileName)
my_clip.audio.write_audiofile(title + ".mp3")
my_clip.close()

os.remove(fileName)
os.remove(title + ".cmt.xml")

f = open('song_name.txt','w+')
f.write(title + '.mp3' )
f.close()
