from wordle import Wordle
from colorama import Fore
from letter_state import LetterState
from typing import List
from wonderwords import RandomWord

r = RandomWord()

secret = r.word(word_min_length=5, word_max_length=5)

# ================ START OF MAIN GAME ==================
def main():
    print('WELCOME TO WORDLE!!1')
    wordle = Wordle(secret) # init constructor for Wordle class

    while wordle.can_attempt:
        x = input("\nType your guess: ")

        if len(x) != wordle.WORD_LENGTH:
            print(Fore.RED + f"Word must be {Wordle.WORD_LENGTH} characters long" + Fore.RESET)
            continue
        wordle.attempt(x)
        display_results(wordle)
    if wordle.is_solved:
        print(f"Congrats, you solved the challenge! It took: {wordle.attempts} times")
    if wordle.can_attempt == False:
        print(f"Sorry, you failed the challenge, try again!\n")
        print(f"The word was: {wordle.secret}")
# ================ END OF MAIN GAME ==================

# ================ START OF FUNCTIONS ==================
def display_results(wordle: Wordle):
    print("\nYour results so far...\n")
    print(f"You have {wordle.remaining_attempts} attempts remaining.")

    lines = []

    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convert_results_to_color(result)
        lines.append(colored_result_str)

    for _ in range(wordle.remaining_attempts):
        lines.append(" ".join(["_"] * wordle.WORD_LENGTH))
    
    
    draw_border_around(lines)

# ================ End of display_results() ==================

def convert_results_to_color(result: List[LetterState]):
    result_with_color  = []
    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.WHITE
        colored_letter = color + letter.character + Fore.RESET
        result_with_color.append(colored_letter)

    return " ".join(result_with_color)
# ================ End of convert_results_to_color(), start of draw_border_around() ==================

def draw_border_around(lines: List[str], size: int = 9, pad: int = 1): 
    content_length = size + pad * 2
    top_border = "┌" + "─" * content_length + "┐"
    bottom_border = "└" + "─" * content_length + "┘" 
    space = " " * pad 
    print(top_border)
    for line in lines:
        print("│" + space + line + space + "│")
    print(bottom_border)

# ================ End of draw_border_around() ==================

# ================ Execution Guard ==================
if __name__ == "__main__":
    main()
