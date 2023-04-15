## brainstorm
-   testing that the input is 5 characters and made up of letters
-   needs a dictionary… two options, an api (wiktionary?) or a download like the enable dictionary... nah just grab some text files from github as your word lists and that’s good enough
-   correct letter shows as capital letter, wrong spot as lowercase letter or in parens, and nowhere as a dash instead of letter?
-   special command (start with !) to show letters guessed so far

## setup
-   read in a word list for solutions ([10k most common words, medium length, no swears](https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-usa-no-swears-medium.txt)) and convert it to a list. maybe remove everything from the list that’s not 5 letters? (can you use a list comprehension for this?)
    
-   [Quickstart — Requests 2.28.2 documentation](https://requests.readthedocs.io/en/latest/user/quickstart/)
    ```python
    import requests
    
    common = requests.get('https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-no-swears.txt')
    common_words = common.text.split('\n')
    ```
    
-   read in a word list for guesses and convert to a list
    -   use 3of6game wordlist from 12dicts [Version 6 of the 12dicts word lists (aspell.net)](http://wordlist.aspell.net/12dicts-readme/#3of6game)
    -   first download from [12Dicts Package (aspell.net)](http://wordlist.aspell.net/12dicts/)
    -   have to work with opening and closing local files [Reading and Writing Files in Python (Guide) – Real Python](https://realpython.com/read-write-files-python/)

## game steps

1.  choose secret word from wordlist, maybe using a string method to all caps it
2.  need variables for solution, current guess, current response, and all letters tried so far. maybe also all words tried so far, just in case that might be handy somehow, idk
3.  (loop) ask player for input, maybe using a string method to all caps it
4.  check if player input equals the solution (ignoring caps) and tell them they win if so
5.  check if the input is a real word and 5 letters long 
6.  for each letter, check first whether guess[letter] = solution[letter], then check whether it’s anywhere in the solution
    1.  if match, add capital letter to response
    2.  if partial match, add (letter) or lowercase letter to response
    3.  if no match, add - to response
    4.  print response

### output format
```
         _  _  _  _  _
guess | (g)[U](e) -  -
```

## TODO
[x] add BOTH dictonaries
    [x] requests
    [x] file operations
[x] write the instructions and welcome message
[] tracking letters guessed
    [x] letters not yet guessed
    [] letters not in the word
    [] list yellow letters
    [] list green letters
[] fix it so that the "yellow" letters don't exceed actual occurrences of that letter (see "oozes" example)
[] change the length of words
    [] function to generate the blank board string
    [] ask the user how long (either let them enter a number OR just ask easy/medium/hard)
    [] ask the number of tries???
[x] maybe process the dicitonaries to only have words of the right length
    [] refactor this using list comprehensions???
[] COLORS - termcolor package?
[?] use curses instead of regular UI
