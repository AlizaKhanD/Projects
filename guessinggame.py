
#Guessing_game 

#open textfile and make a list of words
with open('word.txt', 'r') as file:
    words = [words.rstrip() for words in file] #met rstrip() meer controle bij het verwijderen van witruime en nieuwe lijn aan het einde van de regel 
 
 
import random

#choose a random word from the list
word = random.choice(words)
word_list = list(word)

# def function
def make_misplcaed(word_list):
    return ["_"] * len(word_list) 

def make_wrong():
    return[]

def max_guesses():
    return 5

def guesses_taken(wrong):
    return len(wrong)

#spel initiatlisatie
misplaced = make_misplcaed(word_list)
wrong = make_wrong()
won = False 

#spel uitleg
print("Welcome to the guessing game!")
print("You have to guess the word.")
print("There are " + str(len(word))+ " " +"letters in the word.")
print("You have " + str(max_guesses()) + " guesses.")

playing = input('Do you want to play?  ')
if playing.lower() != 'yes':
    quit()
print('Great! Let\'s play!')

#spel loop
while "_" in misplaced and guesses_taken(wrong) < max_guesses():
    print("\nYour word so far: " + " ".join(misplaced))
    guess = input("What is your guess? ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.")
    elif guess in misplaced or guess in wrong:
        print("You already guessed that letter.")
    elif guess in word_list:
        print("Correct!")
        for i, letter in enumerate(word_list):
            if letter == guess:
                misplaced[i] = guess
    else:
        print("Incorrect!")
        wrong.append(guess)
        print("You have " + str(max_guesses() - guesses_taken(wrong)) + " guesses left.")
        if "_" not in misplaced:
             won = True
if "won" not in misplaced:
    print("Congratulations! You guessed the word: " + word)
else:
    print("Sorry! You ran out of guesses. The word was: " + word)