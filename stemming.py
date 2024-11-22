from data_model import Song
from text_reader import textReader
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from typing import List
 
ps = PorterStemmer()

songs = textReader()

#print(songs[2].blocks[0].text)

for song in songs:
    for block in song.blocks:
        words = block.text
        if(block.text is None):
            continue
        words = block.text.split()
        for word in words:
            stemming:str = str(ps.stem(word, True))
            block.stemmings.append(stemming)
        print(block.stemmings)

 


# for line in songs:

