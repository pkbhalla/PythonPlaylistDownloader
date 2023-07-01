import os
import yt_dlp

link = input("Enter the playlist/video link you wish to download:")
frmt = input("Enter the format to download videos (best/worst):")
tpe = input("Choose the link type, whether playlist(p) link or video(v) link[Enter p/v]:")
pth = input("Enter path where you wish to download the video/s:")

# Define the options for the downloader
options_p = {
    'format': frmt,
    'outtmpl': os.path.join(pth, '%(playlist_index)s_%(title)s.%(ext)s' ),
    'ignoreerrors': True,
    'quiet': True, 
}

options_v = {
    'noplaylist' : True,
    'format': frmt,
    'outtmpl': os.path.join(pth, '%(title)s.%(ext)s' ),
    'ignoreerrors': True,
    'quiet': True,
}

if tpe == "p":
    with yt_dlp.YoutubeDL(options_p) as ydl:
        ydl.download([link])

if tpe == "v":
    with yt_dlp.YoutubeDL(options_v) as ydl:
        ydl.download([link])