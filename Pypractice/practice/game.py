import random
import os
# simple cows and bulls guessing game
def generate():
    alphabets = list(map(chr, range(97, 123)))
    random.shuffle(alphabets)
    line = alphabets[:4]
    print("Generated word is", "".join(list(map(str, line))))
    return line
def custom_create(string):
    line = [x for x in string]
    return line
os.system("cls")
print("press 1 for generated word")
print("press 2 for custom input")
mode = int(input())
if mode is 1:
    word = generate()
else:
    _ = input("Enter 4 letter word: ")
    word = custom_create(_)
    os.system("cls")
bulls = cows = count = 0
while bulls is not 4:
    guess = [x for x in input("Make a guess : ")]
    bulls = sum([1 for i, j in zip(guess, word) if i == j])
    cows = sum([1 for i in guess if i in word and guess.index(i) != word.index(i)])
    print("Bulls:", bulls, " Cows:", cows, "\n")
    count += 1
print("\n", "You won after", count, "guesses!")
