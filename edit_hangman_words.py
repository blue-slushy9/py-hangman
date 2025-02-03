# Open file in read and write mode
with open("2hangman_words.txt", "r+") as file:
    # Read all lines in the file
    lines = file.readlines()

    # Move the file pointer to the beginning of the file
    file.seek(0)

    # Loop over each line and modify it as needed
    for word in lines:
        new_word = word.replace(' • ','')
        file.write(new_word)

    # Truncate any remaining content after the last line
    file.truncate()
