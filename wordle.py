from letter_state import LetterState


class Wordle:
    MAX_ATTEMPTS = 6
    WORD_LENGTH = 5 # global Variables, constants of class
    
    def __init__(self, secret):
        self.secret: str = secret # secret word 
        self.attempts = [] # The attempts from the user
      
    def attempt(self, word: str):
        word = word.upper() # overrides casing, handles case sensitivity
        self.attempts.append(word) # adds attempt to attempt list
      
    def guess(self, word: str):
        word = word.upper # overrides casing, handles case sensitivity
        result = []
        
        for i in range(self.WORD_LENGTH):
            character = word[i] # each character is a character, i, in word
            letter = LetterState(character) # runs each character in the word into the LetterState class
            letter.is_in_word = character in self.secret # checks to see if the character is in the word
            letter.is_in_position = character == self.secret[i] # checks to see if letter is in position
            result.append(letter)
        return result
    @property 
    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret # checks to see if wordle has been solved
    
    @property
    def remaining_attempts(self) -> int:
        return self.MAX_ATTEMPTS - len(self.attempts) # calculates and returns remaining attempts
    
    @property
    def can_attempt(self):
        return self.remaining_attempts > 0  and not self.is_solved # checks to see if the user can attempt
    