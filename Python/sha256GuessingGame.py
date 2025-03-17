import hashlib
import random
import sys
import time

correct = "527aa9f431539da8e151d5434d1d5e611d973f601d8e970790882624554146b0" # runner
cat = "77af778b51abd4a3c51c5ddd97204a9c3ae614ebccb75a606c3b6865aed6744e"

def guesser(guesses, length):
    alphaNumeral = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    numeral = "0123456789"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    guess = ""

    start = time.time();
    for _ in range(guesses):
        for _ in range (length):
            guess += lower[random.randint(0,  25)] # change lower to alphaNumeral, alpha, etc.
        if (hashlib.sha256(guess.encode("utf-8")).hexdigest()) == correct:
            print("The correct string is: " + guess + "\n")
            print("Took " + str(time.time() - start) + " seconds.")
            break
        guess = ""

def guessing_game():
    count = 0
    print("Guess the alphanumeric string (6 characters)!\n")

    while (True):
        count += 1
        guess = input("Guess " + str(count) + ": ")
        if (hashlib.sha256(guess.encode("utf-8")).hexdigest()) == correct:
            print("\nCONGRATS! You are correct (in " + str(count) + " guesses)!");
            sys.exit(0);

guesser(52**6, 6)
guessing_game()