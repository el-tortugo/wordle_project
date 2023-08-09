class LetterState:
# Letter Properties
    def __init__(self, character: str):
        self.character: str = character 
        self.is_in_word: bool = False
        self.is_in_position: bool = False
    
    def __repr__(self): 
# represent constructor, returns the properties of each letter, and whether or not it's in the word and/or position
        return f"[{self.character} is_in_word: {self.is_in_word} _is_in_position: {self.is_in_position}]"