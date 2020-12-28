import moviepy.editor as mpe
from tkinter import *
from moviepy.editor import *


clip1 = VideoFileClip('D:\\Languages\\Python\\Video Editor\\1.mp4')
clip2 = VideoFileClip('D:\\Languages\\Python\\Video Editor\\2.mp4')
clip3 = VideoFileClip('D:\\Languages\\Python\\Video Editor\\3.mp4')

audioClip = AudioFileClip('D:\\Languages\\Python\\Video Editor\\audio.m4a')
# VideoClip = mpe.VideoClip.set_audio(audioClip)
final_clip = clip1.set_audio(audioClip)
final_clip.write_videofile("Final render6.mp4")
