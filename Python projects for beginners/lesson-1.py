# guessing game
from random import randint
from IPython.display import clear_output
guesses = False
number = randint(0, 100)
guesses = 0
while not guesses:
    ans = input("Try the guess number I am thinking of!")
    guesses += 1
    clear_output()
    if int (ans) == number:
        print("Congrats! You guessed it correctly.")
        print( "It took you { } guesses!".format(guesses) )
        break
else if int (ans) > number:
    print("The number is lower than what you guessed.")
elif int(ans) < number:
        print("The number is greater than what you guessed.")