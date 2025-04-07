from image import *
def play(word):
    # initializes our variables and lists
    incorrect_guesses = 0
    secret_word = list(word)
    # this is to keep track of every letter guesses
    guessed_letters = set()
    # this is to keep track of each unique letter in the random word generated
    unique_letters = set(secret_word)
    print(hangman_image[0])
    # lets the user know the length of the word
    print(len(word)*" _ ")
    # loop that continues until 6 incorrect guesses occur
    while incorrect_guesses < 6:
      user_input = input("\nGuess a letter in the word: ").lower()
      # makes it so the user input can only be a letter
      if user_input.isalpha() is False:
          print("Only letters can be guessed.")
      # checks if the user input has already been guessed in the guessed-letters set
      elif user_input in guessed_letters:
          print("Letter has already been guessed!")
          print(f"Letters guessed: {sorted(guessed_letters)}")
      # checks if the user input is in the secret word
      elif user_input not in secret_word:
        incorrect_guesses += 1
        guessed_letters.add(user_input)
        print(f"Letters guessed: {sorted(guessed_letters)}")
      # checks if the user input is in the secret word
      elif user_input in secret_word:
        print("Your guess is correct")
        guessed_letters.add(user_input)
        print(f"Letters guessed: {sorted(guessed_letters)}")
      # displays the word guessing porgress and  updates it if any guesses are correct by looping though the letters in teh secret word and seeing if they are in guessed_letters set
      display = []
      for x in secret_word:
        if x in guessed_letters:
            display.append(x)
        else:
            display.append("_")
      print(' '.join(display))
      # displays the hangman status by pulling from the list on the image.py file
      if incorrect_guesses == 0:
        print(hangman_image[0])
      elif incorrect_guesses == 1:
        print(hangman_image[1])
      elif incorrect_guesses == 2:
        print(hangman_image[2])
      elif incorrect_guesses == 3:
        print(hangman_image[3])
      elif incorrect_guesses == 4:
        print(hangman_image[4])
      elif incorrect_guesses == 5:
        print(hangman_image[5])
      elif incorrect_guesses == 6:
        print(hangman_image[6])
       # win condition, checks if the unique_letters set is a subset within guessed_letters if so you win.
      if unique_letters.issubset(guessed_letters):
        print(f"Congratulations you win! The word is {word}!")
        break
