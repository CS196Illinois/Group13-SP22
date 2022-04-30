# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 00:37:58 2022

@author: deanb
"""

from KerasClassification import *
from helpers import *

Playlist = input("Enter Playlist ID:")
Mood = input("Enter Mood:")
playlist = get_songs_ids_playlist(Playlist)

songlist = [0] * 0

for song in playlist:
    array = predict_mood(song)
    if (array[2] == Mood):
        songlist.append(array[0] + " by " + array[1])
        print("{0} by {1} is a {2} song".format(array[0],array[1],array[2]))

print("\n")
print("\n")
print("\n")

for song in songlist:
    print(song)