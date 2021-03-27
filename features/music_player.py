"""
Music player
@author: Sanjith Venkatesh
@created: March 24, 2021
"""
from playsound import playsound
import multiprocessing, os

music_folder = "/Users/sanjithvenkatesh/Music/google"

def play_song(song):
    p = multiprocessing.Process(target=playsound, args=(music_folder + song,))
    p.start()
    input("press enter to terminate")
    p.terminate()

def add_song(song):
    print("Add song: " + str(song))

def encode_songs():
    for filename in os.listdir(music_folder):
        os.rename(filename, str(hash(filename)))

