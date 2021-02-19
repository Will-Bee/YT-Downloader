from pytube import YouTube
from moviepy.editor import *
from colorama import Fore as f
import os
import shutil
from urllib.request import urlopen

###_- Write path of your music folder here (u must use /, not \) -_###
final_location = 'C:/Users/Admin/Desktop/DownloadedSongs'

def Internet_Check():
    try:
        urlopen('https://www.google.com', timeout=1)
        return True
    except:
        return False

def internet():
    if Internet_Check():
        print(f.GREEN + "CONNECTION OK")
        print(f.RESET + "")
    else:
        print(f.RED + "NO CONNECTION")
        print(f.RESET + "!!! PRESS ENTER TO TRY AGAIN !!!")
        internet_again = input("N to exit, or press enter: ")
        if internet_again == "N" or internet_again == "n":
            exit()
        else:
            internet()

def intro():
    print("MADE BY")
    print("WILL BEE")
    print(f.MAGENTA + "E" + f.GREEN + "N" + f.YELLOW + "J" + f.BLUE + "O" + f.MAGENTA + "Y")
    print(f.GREEN + " ") ###_- JUST A COLORFULL TEXT :D -_###

def get_mp3():
    url = input("YT link: ")
    try:
        print(f.YELLOW + "Waiting for download, wait a sec.")
        mp4 = YouTube(url).streams.get_highest_resolution().download()
        mp3 = mp4.split(".mp4", 1)[0] + f".mp3"

        print("!!!DOWNLOADED SUCCESSFULLY!!!")
        print(f.MAGENTA + "Waiting for MoviePy...")

        video_clip = VideoFileClip(mp4)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(mp3)

        audio_clip.close()
        video_clip.close()

        os.remove(mp4)
        try:
            shutil.move(mp3, final_location)
            print(f.CYAN + "Downloaded to your Music folder")
        except:
            print(f.CYAN + "!!!your mp3 file is in folder with my project!!!")
            print("!!!you must set the path in line 10 in .py file, or it is already downloaded!!!")

        finally:
            print(f.MAGENTA + "!!!CONVERTED SUCCESFULLY!!!")
            print(f.GREEN + "")
    except:
        print(f.RED + "WRONG LINK !!")
        print(f.GREEN + " ")
        get_mp3()
    
    get_mp3()

internet()

intro()

get_mp3()
