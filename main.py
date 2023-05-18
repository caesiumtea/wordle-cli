from random import choice
import requests, termcolor

# GLOBAL VARIABLES #
####################

maxTries = 6
wordLength = 5


# SET UP DICTIONARIES #
#######################

def makeDicts():
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
        line = line.strip("\n$^&+!")
        if len(line) == wordLength:
          allWords.append(line)
    finally:
      longDict.close()
    return commonWords,allWords


# DEFINE FUNCTIONS #
####################

# generate starting board dynamically based on wordLength
def startingBoard():
  text = "Word:   " # 3 spaces for the divider pipe
  # add extra padding if word is longer than the string "word:"
  if wordLength > 5:
    text += " " * (wordLength - 5)
  text += " - " * wordLength
  return [text]


# draw game board
def printBoard(board):
  for line in board:
    print(line)

# for valid guesses, loop through word to generate feedback
# solution guaranteed to be lowercase
def feedback(guess, solution):
  colors = []
  listResponse = []
  response = " | "
  greenSet = set()
  yellowSet = set()
  for i in range(wordLength):
    if guess[i] == solution[i]: 
      # green
      colors.append("green")
      listResponse.append(f"[{guess[i].upper()}]")
      greenSet.add(guess[i].upper())
    elif guess[i] in solution:
      #yellow
      colors.append("yellow")
      listResponse.append(f"({guess[i].lower()})")
      yellowSet.add(guess[i].upper())
    else:
      colors.append("")
      listResponse.append(" - ")
  
  # convert list of colors to final feedback, checking for duplicate letters
  for i in range(wordLength):
    # how many times this letter appears in green in response
    greens = listResponse.count(f"[{guess[i].upper()}]")
    # number of times letter is in solution is the max amount of times it can
    # appear in green + yellow in response
    inWord = solution.count(guess[i].lower()) 
    # how many yellows of this letter in response so far?
    # if it's there in lowercase then it's yellow
    yellowsSoFar = response.count(guess[i].lower())

    if colors[i] == "green":
      response += termcolor.colored(listResponse[i], None, "on_green")
    elif colors[i] == "yellow":
      # compare this letter's appearances so far in the response with the 
      # number of times it's needed
      # number of yellows needed = appearances in solution minus greens
      if yellowsSoFar < inWord - greens:
        response += termcolor.colored(listResponse[i], "black", "on_light_yellow")
      else:
        response += " - "     
    else:
      response += " - "
  return guess + response, greenSet, yellowSet

# COMMANDS #
############

# change maxTries according to player input
def changeTries(triesUsed):
  global maxTries 
  choice = input("How many guesses do you want to be allowed per game? ")
  if choice.isdigit():
    choice = int(choice)
  else:
    print("Tries must be a whole number.")
    return
  # maxTries must be greater than the current game's tries used, or else the
  # game would already be over!
  # we know triesUsed >= 0, so this line also checks that input > 0
  if choice <= triesUsed:
    print("You've already made that many guesses! Please choose a higher " \
          "number. Or start a new game and use the !tries command before " \
          "entering any guesses.")
  else:
    maxTries = choice
    print(f"The maximum number of tries is now {choice}!")


# change wordLength according to player input and start a new game
# includes remaking dictionaries based on new word length
def changeLength():
  global wordLength, commonWords, allWords
  choice = input("How many letters long should the target word be? " \
                     "(must be between 3 and 9) ")
  if choice.isdigit():
    choice = int(choice)
  else:
    print("Length must be a whole number from 3 to 9.")
    return
  if choice < 3:
    print("Length must be at least 3.")
  elif choice > 9:
    print("Length must be 9 or less.")
  else: # 3 <= choice <= 9
    wordLength = choice
  print(f"New word will be {choice} letters long!")
  commonWords, allWords = makeDicts()
  play()


# MESSAGES #
############

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
  print("\nThis game is based on Wordle from the New York Times. " \
        "The goal is to guess the randomly-chosen secret word, which is " \
        f"{wordLength} letters long, in {maxTries} tries or less.")
  print("Just type in your word and press enter to guess!\n")
  print("For each guess, the game will show you how much your letters overlap" \
        " with the secret word.")
  print("Your guess will be shown on the left, and the feedback on the right." \
        "\n")
  print("* A capital letter in square brackets like [A] means that you got " \
        "that letter in exactly the right spot! This equals a green square in" \
        " the original Wordle.")
  print("* A lowercase letter in parentheses like (a) means that this letter " \
        "does appear in the secret word, but not at this position. This " \
        "equals a yellow square in the original Wordle.")
  print("* A dash - in the feedback means that the letter at this position of" \
        " your guess does not appear in the secret word at all.")
  print("Use the feedback to guide your next guesses!\n")
  print("If you use up all your guesses without finding the word, then the " \
        "answer will be shown at the end.\n")
  print("Also, there are some special commands you can enter " \
        "while you're prompted to type a word.")
  print("* Type !quit to stop playing.")
  print("* Type !help to see these instructions again.")
  print("* Type !letters to see which letters you have or have not used in " \
        "any guesses yet.")
  print("* Type !tries to change the max amount of guesses you can make.")
  print("* Type !length to change how long of a word you want to guess. " \
        "WARNING: This will QUIT your current game and start a new game.")
  print("Good luck and have fun!")
  print("=======================\n")


# MAIN LOOP #
#############

# main gameplay loop
def play():
  board = startingBoard()
  solution = choice(commonWords).lower() #choose a random word from short list
  tries = 0
  lettersGuessed = set()
  greens = set()
  yellows = set()

  printBoard(board)

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
      printBoard(board)
    
    elif guess == "!tries":
      # tries isn't what we're setting it to, just passing it in to check that
      # they don't ask for fewer tries than already taken
      changeTries(tries)
    
    elif guess == "!length":
      changeLength()
      break

    elif guess == "!letters":
      notGuessed = ""
      guessed = ""
      for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if letter not in lettersGuessed:
          notGuessed += letter + " "
        elif letter in greens:
          guessed += termcolor.colored(letter, "green") + " "
        elif letter in yellows:
          guessed += termcolor.colored(letter, "yellow") + " "
        elif letter in lettersGuessed:
          guessed += letter + " "
      print("Letters guessed: " + guessed)
      print("Letters not guessed yet: " + notGuessed)
      

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
      response, newGreens, newYellows = feedback(guess, solution)
      board.append(response)
      greens.update(newGreens)
      yellows.update(newYellows)
      printBoard(board)

    else:
      print(f"Guess must be a real {wordLength}-letter word. Or, enter " \
            "one of these commands: !help, !letters, !quit")

  if tries >= maxTries and guess != solution:
    print("Sorry, you're out of guesses! :(")
    print(f"The word was {solution.upper()}.")
  return


# RUN THE GAME #
################

commonWords, allWords = makeDicts()

intro()
play()
again = "y"
while again != "n":
  again = input("Play again? (Y/N): ").lower()
  if again == "y":
    play()