import hashlib
import random

correct = "527aa9f431539da8e151d5434d1d5e611d973f601d8e970790882624554146b0"

def guesser(guesses, length):
    alphaNumeral = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    numeral = "0123456789"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"

    guess = ""

    for _ in range(guesses):
        for _ in range (length):
            guess += lower[random.randint(0,  25)]
        if (hashlib.sha256(guess.encode("utf-8")).hexdigest()) == correct:
            print("The correct string is: " + guess)
            break
        guess = ""

guesser(62**3, 3)