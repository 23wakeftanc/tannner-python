from random import randint
import sys
from typing import List, Union
 #this is all caps becuase WORDS is a constant and the variable WORDS should never be changed
 # if we did modify this it would be a 'global variable, global variables are bad
WORDS: List[str]=[
    "apple",
    "banana",
    "orange",
    "coconut"
]
def get_rand_word() ->str :
    n = randint(0,len(WORDS)-1)
    return WORDS[n]
# we documeneted this a None becuase of a variable doesn't have a return, it returns none by default
def show_help() -> None:
    """ tells to run python hangman.py play"""
    print("run python hangman.py play")


def play_hangman():
    """Play a game of Hangman"""
    print("Welcome to Hangman!")
    game_over = False
    print("We're playing")

    while not game_over:
        WORDS=get_rand_word()
        print(WORDS)
        break


if __name__ == "__main__":
# only play hangman if user ran "python hangman.py play"
    args = sys.argv
    print(sys.argv)
    if args[1] == "play":
        play_hangman()
    # print some help message if user ran "python hangman.py help"
    elif args[1] == "help":
        show_help()
