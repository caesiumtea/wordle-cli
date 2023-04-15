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

# draw game board
def print_board(board):
  for line in board:
    print(line)

# for valid guesses, loop through word to generate feedback
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
  print("WORDLE: Terminal Edition (unofficial!)")
  print(f"You have {maxTries} tries to guess the secret {wordLength}-letter " \
        "word!")

  #ask if they want instructions
  readHelp = input("Would you like to read the instructions? (Y/N) ").lower()
  if readHelp == "y":
    instruct()
  else:
    print("You can enter the command \"!help\" to read instructions later.")

# print instructions
def instruct():
  print("This game is based on Wordle from the New York Times.")
  print("The goal is to guess the randomly-chosen secret word, which is " \
        f"{wordLength} letters long, in {maxTries} tries or less.")
  print("Just type in your word and press enter to guess!")
  print("For each guess, the game will show you how much your letters overlap" \
        " with the secret word.")
  print("Your guess will be shown on the left, and the feedback on the right.")
  print("A capital letter in square brackets like [A] means that you got that" \
        " letter in exactly the right spot! This equals a green square in the" \
        " original Wordle.")
  print("A lowercase letter in parentheses like (a) means that this letter " \
        "does appear in the secret word, but not at this position. This " \
        "equals a yellow square in the original Wordle.")
  print("A dash - in the feedback means that the letter at this position of " \
        "your guess does not appear in the secret word at all.")
  print("Use the feedback to guide your next guesses!")
  print("Also, this game has some special commands you can enter in place of " \
        "guesses.")
  print("Type !quit to stop playing.")
  print("Type !help to see these instructions again.")
  print("Type !letters to see a list of letters you have not used in any " \
        "guesses yet.")
  print("Good luck and have fun!")


# main gameplay loop
def play():
  board = ["Word:    _  _  _  _  _ "]
  solution = choice(commonWords) #choose a random word from short list
  tries = 0
  lettersGuessed = set()

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
      notGuessed = ""
      for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if letter not in lettersGuessed:
          notGuessed += letter + " "
      print("Letters not guessed yet: " + notGuessed)
      print_board(board)

    elif guess == "!quit":
      break

    elif guess == solution:
      tries += 1
      print("Correct! Great job!")
      if tries == 1:
        print("You guessed the word on your first try! Wow!")
      else:
        print(f"You found the word in {tries} tries!")
      break

    elif len(guess) == wordLength and guess in allWords:
      tries += 1
      for letter in guess:
        lettersGuessed.add(letter.upper())
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
again = "y"
while again != "n":
  again = input("Play again? (Y/N): ").lower()
  if again == "y":
    play()