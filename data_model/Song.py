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

