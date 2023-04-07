from random import choice
import requests

# commonWords = read small wordlist from github
# allWords = read large wordlist from local file

wordLength = 5
# pare down word lists to wordlength words only?

# helper function to draw game board?

def play():
  #TODO: generate starting board dynamically based on wordLength
  board = ["         _  _  _  _  _ "]
  solution = choice(commonWords) #choose a random word from short list

  # print intro
  # ask if they want instructions

  while True:
    response = ""
    guess = input("Guess a word: ")
    if guess == "!help":
      # print instructions 
      # print board
    elif guess == "!letters":
      # show letters guessed so far
      # print board
    elif guess == solution:
      print("You win!")
      break
    #TODO: make this a helper function to process valid guesses
    elif len(guess) == wordLength and guess in allWords:
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
    else:
      print(f"Guess must be a real {wordLength}-letter word.")
  return

play()
# input("Play again? Y/N") -> if y: play