# This is hangman, although without the actual picture of the man hanging. 
# As with the pictorial version, in this game you will also lose after 6 wrong
# guesses.

# The computer will select a word at random from a list, and then present to 
# you the number of letters contained in that word. If you guess a letter 
# correctly, the computer will fill out the slots where that letter goes and 
# then present it to you for your benefit.

#######################

# The choice method from the random module allows you to pick an element at
# random from, in this case, a text document with many different words in it;
from random import choice

# Using 'with open' instead of 'open' ensures the file is properly opened and
# closed at the end; we are opening our 2hangman text file in read mode, this
# file was edited by me with another short Python script in the directory 
# which I used to get it into the correct format to use in this program;
# we are opening the file as 'words_file';
with open('2hangman_words.txt','r') as words_file:
    
    # Then we create a wordlist which consists of the entire contents of the
    # original text file, only we used the split() method which by default
    # breaks up the text at every whitespace character; since the words in 
    # the text file are each on their own line, this method creates a new
    # list where each word is an element thereof;
    wordlist = words_file.read().split()

# random_word will be our word the player has to guess, it is selected from
# our wordlist, which is a text file in the same directory;
random_word = choice(wordlist)

# The underscores will be the visual representation of the word, one for each
# letter, we create it as an empty list so that we can use list manipulation
# techniques on it;
underscores = []

# For every letter in our word, we add an underscore to the empty list we 
# created;
for letter in random_word:
    underscores.append('_')

# The built-in join() method allows us concatenate the elements of a list into
# a single string; we put a space between the ' ' , which also puts a space 
# between the underscores, which helps with visualization; otherwise the 
# underscores would look like one long underscore;
joined_underscores = (' '.join(underscores))

# Throughout this program, I use many print() statements to enhance legibility;
print()

print("Here is the representation of your word...")
print()

print(joined_underscores)
print()

# i is our strikes counter, keeps track of how many guesses the player has
# gotten wrong; 
i=0

# Create a list that will store all of the letters that the player has guessed
# in this round, in order to inform them in the case that they try to guess
# the same letter twice; the letter will be added at the end of the loop so
# it doesn't cause interference with normal functioning (i.e. a correct guess
# that hasn't been guessed before);
guesses = []

# We stay in this loop until either the player has reached 6 wrong guesses or
# they have won the game;
while True:
    
    # Since the user only gets 6 incorrect guesses, if the counter reaches
    # that amount, then they lose;
    if i==6:
        print()
        print(f"Sorry, that's all 6 of your strikes! You have lost the game,\n" 
                f"your word was {random_word}. Please try again.\n")
        break
    
    # If all of the '_'s in the underscores list have been replaced, that
    # means there are no more letters to guess, ergo the player has won;
    elif '_' not in underscores:
        print(f"Congratulations, you have won the game! Your word is\n" 
                f"{random_word}!\n")
        break
    
    print()
    print("Please enter your guess now, it should be a single letter...")
    print()
    guess = input()
    print()

    # First check whether the letter has already been guessed in this round;
    if guess in guesses:
        print("You have already guessed this letter! Please enter a\n"
                "different letter!")
        print()

    elif guess in random_word:
        # Create an empty list to hold the indexes of the positions where the 
        # letter the player guessed, if it is correct, appear in the random
        # word, so that we can replace the underscore(s) with the letter;
        indexes = []
        
        # Loop through random_word...
        for n in range(len(random_word)):
            # if the letter in the word matches the letter that was guessed...
            if random_word[n] == guess:
                # append the value, n, of the index to the indexes list;
                indexes.append(n)
        
        # Loop through every index we have added to indexes list...
        for index in indexes:
            # based on these values, replace the same index in underscores 
            # with the letter that was guessed;
            underscores[index] = guess            
   
        # Create new variable to hold the joined string version of our
        # underscores list, after we have possibly replaced some of the 
        # underscores with letters based on player guesses;
        string_underscores = (' '.join(underscores))
        
        # "Updated representation" means the correct underscores have been
        # replaced with the letter(s) that were guessed correctly;
        print(f"Good guess! Here is the updated representation of your word:\n"
                f"\n{string_underscores}\n")
        
        # Add the letter to guesses list to keep track of letters already
        # guessed and prevent user from entering same letter twice;
        guesses.append(guess)
        
    elif guess not in random_word:
        # Incorrect guess means counter goes up by one;
        i+=1
        
        # Use join() method to convert updated underscores list into a string, 
        # so we can print it out below; we put a space between the two quotes
        # (' ') so that the list elements will also be joined with a space
        # between them, this helps with visualization;
        string_underscores = (' '.join(underscores))
        
        print(f"Sorry, that is incorrect! That is strike {i} of 6.\n")
        print()
        
        # Prints updated underscores list, which may or may not have some
        # letters in it, based on the player's guesses up to this point;
        print(f"Here is what you have so far:\n\n{string_underscores}\n")
        
        # Add the letter to guesses list to keep track of letters already
        # guessed and prevent user from entering same letter twice;
        guesses.append(guess)

