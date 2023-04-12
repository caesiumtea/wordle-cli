from random import choice
import requests

# VARIABLES #
#############

maxTries = 6
wordLength = 5


# SET UP DICTIONARIES #
#######################

commonWords = []
common = requests.get('https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-no-swears.txt')
commonDict = common.text.splitlines()
for word in commonDict:
  if len(word) == wordLength:
    commonWords.append(word)  

allWords = []
longDict = open("data/3of6game.txt", "r")
try:
  for line in longDict:
    line = line.strip("\n$")
    if len(line) == wordLength:
      allWords.append(line)
finally:
  longDict.close()
print(allWords[0:30])


# DEFINE FUNCTIONS #
####################

#TODO: helper function to generate starting board dynamically based on wordLength

# helper function to draw game board
def print_board(board):
  for line in board:
    print(line)

# helper function to evaluate valid guesses
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

# print opening text at start of game
def intro():
  print("WORDLE: Terminal Edition")
  print(f"You have {maxTries} tries to guess the secret {wordLength}-letter " \
        "word!")

  #ask if they want instructions
  readHelp = input("Would you like to read the instructions? (Y/N) ").lower()
  if readHelp == "y":
    instruct()
  else:
    print("You can read instructions later by typing \"!help\" .")

# print instructions
def instruct():
  print(f"The goal is to guess the randomly-chosen secret word, which is " \
        "{wordLength} letters long.")

# main gameplay loop
def play():
  board = ["Word:    _  _  _  _  _ "]
  solution = choice(commonWords) #choose a random word from short list
  tries = 0
  print_board()

  while tries < maxTries:
    triesLeft = maxTries - tries
    if triesLeft == 1:
      print(f"You have {triesLeft} more try to guess the secret word.")
    else: 
      print(f"You have {triesLeft} more tries to guess the secret word.")
    guess = input("Guess a word: ").lower()

    if guess == "!help":
      print("help")
      instruct()
      print_board(board)
    elif guess == "!letters":
      print("letters")
      #TODO show letters guessed so far
      print_board(board)
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


# RUN THE GAME #
################

intro()
play()
# again = "y"
# while again != "n":
#   again = input("Play again? (Y/N): ").lower()
#   if again == "y":
#     play()