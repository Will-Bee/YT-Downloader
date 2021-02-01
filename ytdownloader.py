from pytube import YouTube
from moviepy.editor import *
from colorama import Fore
import os
import shutil
import urllib
from urllib.request import urlopen

###_-CONNECTION TEST-_###

def is_internet():
    try:
        urlopen('https://www.google.com', timeout=1)
        return True
    except urllib.error.URLError as Error:
        print(Error)
        return False

def internet():
    if is_internet():
        print(Fore.GREEN + "CONNECTION OK")
    else:
        print(Fore.RED + "NO CONNECTION")
        print(Fore.RESET + "PRESS ENTER TO TRY AGAIN")
        input()
        internet()

def intro():
    print(Fore.RESET + "MADE BY")
    print("WILL BEE")
    print(Fore.MAGENTA + "E" + Fore.GREEN + "N" + Fore.YELLOW + "J" + Fore.BLUE + "O" + Fore.MAGENTA + "Y")
    print(Fore.GREEN + " ") ###_- JUST A COLORFULL TEXT :D -_###

def get_mp3():
    url = input("YT link: ")
    print(Fore.YELLOW + "Waiting for download, wait a sec.")
    mp4 = YouTube(url).streams.get_highest_resolution().download()
    mp3 = mp4.split(".mp4", 1)[0] + f".mp3"

    print("!!!DOWNLOADED SUCCESSFULLY!!!")
    print(Fore.MAGENTA + "Waiting for MoviePy...")

    video_clip = VideoFileClip(mp4)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(mp3)

    audio_clip.close()
    video_clip.close()

    os.remove(mp4)                                    ###_- !!! PATH WHERE YOUR FILES WILL BE DOWNLOADED, TAKE A SEC TO EDIT           !!! -_###
    try:
        shutil.move(mp3, r"C:\Users\Admin\Music")     ###_- !!! YOU NEED TO EDIT THIS LIKE: C:\Users\NAME\Music, or your custom path   !!! -_###
                                                      ###_- !!! ANY OTHER DISC MUST BE WRITEN AS "E:\path or F:\path" DONT MAKE MISTAKE!!! -_###
    except:
        print(Fore.RED + "!!your mp3 file is in folder with my project!!!")
        print("(you must set the path in line 56 in .py file, or it is already downloaded)")

    finally:
        print(Fore.MAGENTA + "!!!CONVERTED SUCCESFULLY!!!")
        print(Fore.GREEN + "")
    
    get_mp3()

internet()

intro()

get_mp3()
