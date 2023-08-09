class Wordle:
    MAX_ATTEMPTS = 6
    WORD_LENGTH = 5 # global Variables, constants of class
    
    def __init__(self, secret):
        self.secret: str = secret # secret word 
        self.attempts = [] # The attempts from the user.
      
    def attempt(self, word: str):
        self.attempts.append(word)

    @property 
    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret
    
    @property
    def remaining_attempts(self) -> int:
        return self.MAX_ATTEMPTS - len(self.attempts)
    
    @property
    def can_attempt(self):
        return self.remaining_attempts > 0  and not self.is_solved
    