import re
from typing import List
from data_model.Song import Song
from rake_nltk import Rake # type: ignore
from stemming.text_reader import textReader

def readText() -> List[Song]:
    song_title_pattern = re.compile(r"^\d+\s+[A-Za-z\s]+$")

    with open("../lyrics.txt") as f:
        for line in f: 
            if song_title_pattern.match(line):
                

# Uses stopwords for english from NLTK, and all puntuation characters by
# default
r = Rake()

# Extraction given the text.
r.extract_keywords_from_text()

# Extraction given the list of strings where each string is a sentence.
r.extract_keywords_from_sentences()

# To get keyword phrases ranked highest to lowest.
r.get_ranked_phrases()

# To get keyword phrases ranked highest to lowest with scores.
r.get_ranked_phrases_with_scores()