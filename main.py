from random import choice
import requests

commonWords = ["wordy"]
allWords = ["wordy", "truth", "ghast", "volts", "swing", "swish", "splat", "smash"]
# commonWords = read small wordlist from github
# allWords = read large wordlist from local file

maxTries = 6
wordLength = 5
# pare down word lists to wordlength words only?
#TODO: helper function to generate starting board dynamically based on wordLength

# helper function to draw game board
def print_board(board):
  for line in board:
    print(line)

# main gameplay loop
def play():
  board = ["         _  _  _  _  _ "]
  solution = choice(commonWords) #choose a random word from short list
  tries = 0

  # print intro
  # ask if they want instructions

  while tries < maxTries:
    response = ""

    triesLeft = maxTries - tries
    print(f"You have {triesLeft} more tries to guess the secret word.")
    guess = input("Guess a word: ").lower()

    if guess == "!help":
      print("help")
      # print instructions 
      # print board
    elif guess == "!letters":
      print("letters")
      # show letters guessed so far
      # print board
    elif guess == "!quit":
      break
    elif guess == solution:
      print("You win!")
      break
    #TODO: make this a helper function to process valid guesses
    elif len(guess) == wordLength and guess in allWords:
      tries += 1
      response += guess + " | "
      for i in range(wordLength):
        if guess[i] == solution[i]: 
          # green
          response += f"[{guess[i].upper()}]"
        elif guess[i] in solution:
          #yellow
          response += f"({guess[i].lower()})"
        else:
          response += " - "
      board.append(response)
      print_board(board)
    else:
      print(f"Guess must be a real {wordLength}-letter word.")
  if tries >= maxTries:
    print("No guesses left.")
  return

play()
# input("Play again? Y/N") -> if y: play