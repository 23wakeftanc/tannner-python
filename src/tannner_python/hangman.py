"""
This file demo's the following principles
functions:
-def: defines a function
-return: defines the function "call" should turn into (into what the function should "return")
-"function call": whenever you run a function i.e. functio()
-arguments/parameters: the variables that the function can take in, i.e. 'def function(a, b, c,)
a, b c are the parameters
-scope: local variables: variables that are defined in an indented block of code.
They get deleted when the indented block finishes
-global variables: variables that are defined outside of all the indented blocks. so they are in teh "global scope"
any code block can see variables
-docstrings: the first line of a function is called the dockstring. It should be a short summary of what the function does. 
-'len' counts in a string

Variable types
-variables: a value tht you can change. 'a=1' and then 'a=2' overwrites the 'a' variable.
That's why it's called a variable, because we change its value over time.
-constants: a variable that NEVER gets changed To show the reader that a variable is " constant",
you make the constant name ALL_UPPERCASE_LIKE_THIS. if you do 'PI=3.1415' and then 'PI=3.14",
 you are LYING to the people reading your code, becuase you changed a constant
GLobal variables: if you need a variable in the global scope, PLEASE make it a constant so that users know to change it.
 Otherwise it is a "global variables", those are DEATH. 90% of bugs in code come from global variables.

 Typing:
 there is a builtin library in python called "typing" that helps you label what type of data you store in variables.
 you declare a type like this: 'x: int = 5'. This shows that x should ALWAYS should always be an interger.
 This is REALLY helpful for people for people reading your code, including you 2 weeks from now, when you have forgotten your
 own code.

 You can import 'List' and 'Union' from typing.

 fruits: List[str] = ['apple', 'banana', 'orange']
 that is how you d the "type annotation for a list of strings

 numbers: List[Union[int,float,bool]] = [1,2,3,4.2,true]
  is how you would do a type annotation for a list that can have intergers floats and booleans

Good ways to get help
-Google error messages and basic questions like "how do i check if a string contains a smaller string"
-python commmand: 
    -run 'python' in the terminal to get a "python shell" ( a terminal for python commands.)
    You should see ">>>"
    From there you can use the 'help' function and the type function
        -help(something): you use it like this.
            Say you want help with 'input' run help(input) to see the docstring of the function. super useful
        -type(something): tells you what the type of something is. like 'type(5) will return int and type(True) will return bool
        -exit(): this is how you quit the python shell
- udemy course
- stackoverfow
- eric the cool man
- ww3schools
"""
from random import randint
import sys
from typing import List, Union

# this is all caps becuase WORDS is a constant and the variable WORDS should never be changed
# if we did modify this it would be a 'global variable, global variables are bad
WORDS: List[str] = ["apple", "banana", "orange", "coconut"]


def get_rand_word() -> str:
    n = randint(0, len(WORDS) - 1)
    return WORDS[n]


# we documeneted this a None becuase of a variable doesn't have a return, it returns none by default
def show_help() -> None:
    """tells to run python hangman.py play"""
    print("run python hangman.py play")


def play_hangman():
    """Play a game of Hangman"""
    print("Welcome to Hangman!")
    game_over: bool = False
    print("We're playing")
    guesses: List[str] = []
    word: str = get_rand_word()
    num_wrong_guesses: int = 0
    
    while not game_over:
        if num_wrong_guesses >= 5:
            print("Game Over")
            break

        word_length: int = len(word)
        print("_ " * word_length)
        guess: str = input("Guess a letter:")
        guess_is_correct: bool = guess in word
        if guess in guesses:
            print("Already made that guess. Guess Again: ")
        else:
            guesses.append(guess)
            if guess_is_correct:
                print("Correct!")

            else:
                print("Wrong :(")
                num_wrong_guesses=num_wrong_guesses+1
                

# track the guess
# print out an updated word ouput "_ a _ a _ a"
# create a limit on wrong guesses
# print our the hanging guy

if __name__ == "__main__":
    # only play hangman if user ran "python hangman.py play"
    args = sys.argv
    print(sys.argv)
    if args[1] == "play":
        play_hangman()
    # print some help message if user ran "python hangman.py help"
    elif args[1] == "help":
        show_help()
