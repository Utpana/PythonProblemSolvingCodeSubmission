
# Problem Set 2(Hangman)
# Name: Utpana
# Time Spent: 12:00hrs

import random

print("loading word list......")
WORDLIST_FILENAME = "words.txt"
inFile = open(WORDLIST_FILENAME, 'r')
line = inFile.readline()
wordlist = line.split()
print("  ", len(wordlist),"loaded words." )
word = random.choice(wordlist)      #Function will choose one random word from this list of words.  
 
name = input("Enter Your  name : ")
 
print("Welcome to the game, Hangman!")

print("Guess the characters")
guesses = ''
print("I'm thinking of a word that",len(word),"character is long")
turns = len(word) * 2
print('You have '+ str(turns) +' guesses left.')
 
while turns > 0:
     
                    # counts the number of times a user fails.
    failed = 0         
     
                     # all characters from the input word taking one at a time.
    for char in word:
         
                     # comparing that character with the character in guesses
        if char in guesses:
            print(char)
             
        else:
            print("-")
             
                    # for every failure 1 will be incremented in failure
            failed += 1
             
 
    if failed == 0:
                    # user will win the game if failure is 0 and 'You Win' will be given as output
        print("You won")
         
                    # this print the correct word
        print("The word is: ", word)
        break
     
                 # if user has input the wrong alphabet then it will ask user to enter another alphabet
    guess = input("Guess the character:")
     
                 # every input character will be stored in guesses
    guesses += guess
                 # check input with the character in word
    if guess not in word:
         
        turns -= 1
         
                  # if the character doesn’t match the word then “Wrong” will be given as output
        print("Wrong")
         
                  # this will print the number of turns left for the user
        print("You have", + turns, 'more guesses')
         
         
        if turns == 0:
            print("You Lose")
