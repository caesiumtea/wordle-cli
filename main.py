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

def feedback(guess, solution):
  response = guess + " | "
  for i in range(wordLength):
    if guess[i] == solution[i]: 
      # green
      response += f"[{guess[i].upper()}]"
    elif guess[i] in solution:
      #yellow
      response += f"({guess[i].lower()})"
    else:
      response += " - "
  return response


# main gameplay loop
def play():
  board = ["         _  _  _  _  _ "]
  solution = choice(commonWords) #choose a random word from short list
  tries = 0

  # print intro
  # ask if they want instructions

  while tries < maxTries:

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
    elif len(guess) == wordLength and guess in allWords:
      tries += 1
      board.append(feedback(guess, solution))
      print_board(board)
    else:
      print(f"Guess must be a real {wordLength}-letter word.")
  if tries >= maxTries:
    print("No guesses left.")
  return

play()
again = "y"
while again != "n":
  again = input("Play again? (Y/N): ").lower()
  if again == "y":
    play()

