from tkinter import *
from moviepy.editor import *


# Variable
clip1 = VideoFileClip('D:\\Languages\\Python\\Video Editor\\1.MP4')
clip2 = VideoFileClip('D:\\Languages\\Python\\Video Editor\\2.MP4')
clip3 = VideoFileClip('D:\\Languages\\Python\\Video Editor\\3.MP4')


# Main Screen
root = Tk()
root.title("Instant Editor")
root.geometry('750x200')
root.minsize(750, 200)
root.maxsize(750, 200)
root.config(bg="#232323")
root.iconbitmap('D:\\Languages\\Python\\Video Editor\\icon.ico')


# Functions
def mix():
    final_clip = concatenate_videoclips([clip1, clip2])
    final_clip.write_videofile("Final render.mp4")


def mirror():
    clip_mirror = clip1.fx(vfx.mirror_y)
    clip_mirror.write_videofile("Final render1.mp4")


def resize():
    r = float(input("Enter your Size: "))
    clip_resize = clip1.resize(height=r)
    clip_resize.write_videofile("Final render2.mp4")


def Effects_speed():
    speed = float(input("Enter your Speed: "))
    clip_speed = clip1.fx(vfx.speedx, speed)
    clip_speed.write_videofile("Final render3.mp4")


def Effects_colour():
    colour = float(input("Enter your Darkness: "))
    clip_colour = clip1.fx(vfx.colorx, colour)
    clip_colour.write_videofile("Final render4.mp4")


def trim():
    start = float(input("Enter your Starting point: "))
    end = float(input("Enter your Ending point: "))
    clip_trim = clip1.cutout(start, end)
    clip_trim.write_videofile("Final render5.mp4", codec = 'libx264')


def audio_file():
    audioClip = AudioFileClip('D:\\Languages\\Python\\Video Editor\\audio_9.mpeg')
    final_clip = clip1.set_audio(audioClip)
    final_clip.write_videofile("Final render6.mp4")


# Mix
b = Button(root, text="Mix", relief=GROOVE, background="#232323", foreground="white", command=mix, cursor="hand1")
b.pack(side="left", padx=20)
b.config(width=8, height=3)

# Mirror
b = Button(root, text="Mirror", relief=GROOVE, background="#232323", foreground="white", command=mirror, cursor="hand1")
b.pack(side="left", padx=20)
b.config(width=8, height=3)

# Resize
b = Button(root, text="Resize", relief=GROOVE, background="#232323", foreground="white", command=resize, cursor="hand1")
b.pack(side="left", padx=20)
b.config(width=8, height=3)

# Speed
b = Button(root, text="Speed", relief=GROOVE, background="#232323", foreground="white", command=Effects_speed, cursor="hand1")
b.pack(side="left", padx=20)
b.config(width=8, height=3)

# Colour
b = Button(root, text="Colour", relief=GROOVE, background="#232323", foreground="white", command=Effects_colour, cursor="hand1")
b.pack(side="left", padx=20)
b.config(width=8, height=3)

# Trim
b = Button(root, text="Trim", relief=GROOVE, background="#232323", foreground="white", command=trim, cursor="hand1")
b.pack(side="left", padx=20)
b.config(width=8, height=3)

# Audio
b = Button(root, text="Audio", relief=GROOVE, background="#232323", foreground="white", command=audio_file, cursor="hand1")
b.pack(side="left", padx=20)
b.config(width=8, height=3)


# root.mainLoop()
root.mainloop()