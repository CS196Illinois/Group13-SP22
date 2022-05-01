# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 00:37:58 2022

@author: deanb
"""

from KerasClassification import *
from helpers import *


def main(setPlaylist, setMood):
    if setPlaylist == None or setPlaylist == "":
        playlistId = "37i9dQZF1DX4JAvHpjipBk"
    elif "playlist/" in setPlaylist:
        linkParts = setPlaylist.split("playlist/")
        playlistBack = linkParts[1].split("?")
        playlistId = playlistBack[0]
    else:
        playlistBack = setPlaylist.split("?")
        playlistId = playlistBack[0]

    playlist = get_songs_ids_playlist(playlistId)
    mood = setMood
    songlist = [0] * 0
    for song in playlist:
        array = predict_mood(song)
        if (array[2] == mood):
            songlist.append(array[0] + " by " + array[1])
    recommended = ""
    for song in songlist:
        recommended += song + "\n"
    return recommended


"""
Plan going forward:
In FilterActivity, enter playlist ID and mood
FilterActivity calls main, which returns a multiline string containing the name and artist of each of
the songs in the given playlist which fit the given mood
In FilterActivity, it parses the multiline string, and sets its text to the list of recommended songs
Should generally follow the video

//////////////

EditText Et1, Et2;
Button Btn
TextView tv;

Et1 = (EditText)findViewById(R.id.et1)
Et2 = (EditText)findViewById(R.id.et2)
Button = (Button)findViewById(R.id.btn)
tv = (TextView)findViewById(R.id.text_view)



Upon clicking the button on the mainactivity, the playlist id and the mood will be sent to the new activity with the text views



Btn.setOnClickListener(new View.OnClickListener() {
    @Override
    public void onClick(View view) {
        obj = pyobj.callAttr("main", Et1.getText().toString(), Et2.getText().toString());
        songlist = obj.toString()
    }
});
String[] songarray = new String[];
songarray = songlist.split("\n")

Then a loop or something which sets the textview to given songs

//////////////


Using this code in Filter Activity when all the activities are set up correctly should allow it to work

"""