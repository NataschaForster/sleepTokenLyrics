from typing import List

class Block:
    def __init__(self, type: str = None, text: str = None):
        self.type = type
        self.text = text
        self.words : List[str] = []
        self.stemmings:List[str] = []

class Song:
    def __init__(self, title: str = None): 
        self.title = title
        self.blocks: List[Block] = []

class Result:
    def __init__(self, id, stem, amount, songs, line):
        self.id = id
        self.stem = stem
        self.amount = amount
        self.songs = songs
        self.line = line
