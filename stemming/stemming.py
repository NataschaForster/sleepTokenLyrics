from typing import List
from stemming.text_reader import textReader
from nltk.stem import PorterStemmer # type: ignore
 

def stemming() -> List[str]:
    ps = PorterStemmer()

    songs = textReader()

    result = []

    for song in songs:
        for block in song.blocks:
            words = block.text
            if(block.text is None):
                continue
            words = block.text.split()
            for word in words:
                stemming:str = str(ps.stem(word, True))
                result.append(stemming)
            # print(result)

    return result



