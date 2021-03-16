#Hangman Step by Step

import random

#TODO-1: - Import the logo and stages from hangman_art.py and print logo at the start of the game.
from hangman_art import logo,stages
print(logo)

#TODO-2: - Update the chosen word to use the list from hangman_words.py
from hangman_words import word_list
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-3: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#Create blanks
display = []

#TODO-4: - Loop through each position in the chosen_word;
for letter in chosen_word:
    display += "_" 

#TODO-5: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

while '_' in display and lives > 0:
    guess = input("Guess a letter: ").lower()
    print(guess)

    #TODO-6: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print("Letter already guessed")
    else:
        #Check guessed letter
        for position in range(0, len(chosen_word)):
            letter = chosen_word[position]

            if letter == guess:
                display[position] = letter    

        #TODO-7: - If guess is not a letter in the chosen_word,
        #print out the letter and let them know it's not in the word.Then reduce 'lives' by 1. 
        #If lives goes down to 0 then the game should stop and it should print "You lose."    
        if guess not in chosen_word:
            lives -=1
            print(guess + " is not in the word, you have lost a life") 
            print(stages[lives])      
    print(display)

if lives <= 0:
    print("Ooops, you lose.") 
else:
    print("Yaay, you won!")

#Join all the elements in the list and turn it into a String.
print(f"{' '.join(display)}")
        
