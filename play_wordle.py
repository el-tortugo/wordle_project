from wordle import Wordle
def main():
    print('Hello World')
    wordle = Wordle("Apple") # init constructor for Wordle class

    while wordle.can_attempt:
        x = input("Type your guess:")
        wordle.attempt(x)
    if wordle.is_solved:
        print("Congratulations, Solved")
    else:
        print("Fail")


if __name__ == "__main__":
    main()
