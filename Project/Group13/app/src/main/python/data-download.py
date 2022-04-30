# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 23:20:54 2022

@author: deanb
"""

from  helpers import *
import spotipy
from spotipy import SpotifyClientCredentials, util
from IPython.core.display import clear_output

import pandas as pd
import pandasql as ps
import time
import sqlite3
tracks,columns = download_playlist('74mjFAqRNCDixjF6cMqImW',10)
#If the id if for artist, you must to put specify True to the artist parameter
#tracks,columns = download_albums('id_of_the_artist_or_the_album',artist=True)
df1 = pd.DataFrame(tracks,columns=columns)
df1.head()
df1.to_csv('C:/Users/deanb/Downloads/Spotify-Machine-Learning-master/Spotify-Machine-Learning-master/df1.csv')