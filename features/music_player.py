"""
Music player
@author: Sanjith Venkatesh
@created: March 24, 2021
"""
from playsound import playsound
import multiprocessing

music_folder = "/Users/sanjithvenkatesh/Music/"

def play_song(song):
    p = multiprocessing.Process(target=playsound, args=(music_folder + song,))
    p.start()
    input("press enter to terminate")
    p.terminate()


