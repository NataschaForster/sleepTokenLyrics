# read lyrics from file and parse them into objects

import os
import re
from typing import List
from data_model.Song import Song, Block 


def textReader() -> List[Song]:
    song_title_pattern = re.compile(r"^\d+\s+[A-Za-z\s]+$")
    block_type_pattern = re.compile(r"^\[[A-Za-z\s\d\-]+\]$")
    block_text_pattern = re.compile(r"^[a-zA-Z].*$")

    songs: List[Song] = []
    song: Song = Song()
    block: Block = Block()
    
    #Read file line by line
    with open("./lyrics.txt", 'r') as f:
        for line in f: 
            if song_title_pattern.match(line):
                # append created object
                if song.title is not None:
                    songs.append(song)
                    song = Song(title=line)

                # create new object
                song.title = line
            # ignore empty lines
            elif line == "\n":
                continue
            
            elif block_type_pattern.match(line):
                # reset old block object
                if block is not {}:
                    song.blocks.append(block)
                    block = Block(type=line, text="")
                    
                block.type = line
            elif block_text_pattern.match(line):
                line = re.sub(r'[^a-zA-Z\s]', '', line)
                block.text += line + "\n" 

        # append last block 
        if block is not None:
            song.blocks.append(block)

        # Füge den letzten Song hinzu, falls vorhanden
        if song is not None:
            songs.append(song)  

        # print(song.title)
        # print(song.blocks[0].type)
        # print(song.blocks[0].text)

    return songs
                