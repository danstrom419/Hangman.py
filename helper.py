from image import *
def play(word):
    # prompt user
    incorrect_guesses = 0
    secret_word = list(word)
    guessed_letters = set()
    unique_letters = set(secret_word)
    print(hangman_image[0])
    print(len(word)*" _ ")
    # loop - counter controlled - GLOBAL
    while incorrect_guesses < 6:
      user_input = input("\nGuess a letter in the word: ").lower()
      if user_input.isalpha() is False:
          print("Only letters can be guessed.")
      
      elif user_input in guessed_letters:
          print("Letter has already been guessed!")
          print(f"Letters guessed: {sorted(guessed_letters)}")
      
      elif user_input not in secret_word:
        incorrect_guesses += 1
        guessed_letters.add(user_input)
        print(f"Letters guessed: {sorted(guessed_letters)}")
      
      elif user_input in secret_word:
        print("Your guess is correct")
        guessed_letters.add(user_input)
        print(f"Letters guessed: {sorted(guessed_letters)}")
      
      display = []
      for x in secret_word:
        if x in guessed_letters:
            display.append(x)
        else:
            display.append("_")
      print(' '.join(display))

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

      if unique_letters.issubset(guessed_letters):
        print(f"Congratulations you win! The word is {word}!")
        break
