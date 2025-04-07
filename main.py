import random as r
from helper import *
from image import *
def main():
        # starts the initial loop to begin the game
        while True:
            word = r.choice(open("word_list.txt").read().split())
            print(" Welcome to hangman, try and guess the word to save a stick man!\n")
            play(word)
            # starts the second loop after the game ends to see if the player wants to play again
            while True:
                play_again = input("Play again? [Y/N]: ").upper()
                if play_again == "N":
                    print("Thank you for playing!")
                    return
                elif play_again == "Y":
                    break
                elif play_again not in ["Y", "N"]:
                    print("Please input the correct value!")




if __name__ == "__main__":
        main()
