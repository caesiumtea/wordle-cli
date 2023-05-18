# WORDLE: Terminal edition! 
[![Hippocratic License HL3-LAW-MIL-SV](https://img.shields.io/static/v1?label=Hippocratic%20License&message=HL3-LAW-MIL-SV&labelColor=5e2751&color=bc8c3d)](https://firstdonoharm.dev/version/3/0/law-mil-sv.html)

Play Wordle right from the terminal!

Created as a final project for [Codédex.io](https://www.codedex.io/) course The Legend of Python.

[GitHub repo](https://github.com/caesiumtea/wordle-cli) | [Interactive version on repl.it](https://replit.com/@caesiumtea/wordle-cli)

This game is merely *based on* Wordle. It is not affiliated with the official Wordle game from the New York Times. It also (presumably) uses different dictionaries than the official Wordle, so it might differ in what words it accepts or generates.

I know there's already 500 million Wordle clones out there. This was made more as a practice exercise and doesn't really serve any purpose as a game. It doesn't even offer the benefit of being an offline version of Wordle, since it uses an internet connection to pull one of its dictionaries from GitHub each time it starts up. (Which is again impractical, but I wanted to practice with the `requests` module.)

## How to play
You have 6 tries to guess the secret 5-letter word!

This game is based on Wordle from the New York Times. The goal is to guess the randomly-chosen secret word, which is 5 letters long, in 6 tries or less.
Just type in your word and press enter to guess!

For each guess, the game will show you how much your letters overlap with the secret word.
Your guess will be shown on the left, and the feedback on the right.

* A capital letter in square brackets like `[A]` means that you got that letter in exactly the right spot! This equals a green square in the original Wordle.
* A lowercase letter in parentheses like `(a)` means that this letter does appear in the secret word, but not at this position. This equals a yellow square in the original Wordle.
* A dash - in the feedback means that the letter at this position of your guess does not appear in the secret word at all.
Use the feedback to guide your next guesses!

If you use up all your guesses without finding the word, then the answer will be shown at the end.

Good luck and have fun!

### Commands
There are some special commands you can enter during the game when you're prompted to type a word.
* `!help` - See these instructions.
* `!letters` - See which letters you have or have not used in any guesses yet.
* `!tries` - Change the max amount of guesses you can make.
* `!length` - Change how long of a word you want to guess. **WARNING:** This will QUIT your current game and start a new game.
* `!quit` - Stop playing.

## Installation
If you want to play the game, I recommend just visiting the [repl.it page](https://replit.com/@caesiumtea/wordle-cli). However, if you really want to install it locally, try these steps:

- Clone/download the repo
- Make sure you have Python 3 and pip installed
- Use pip to install the packages `requests` and `termcolor`, as listed in the `requirements.txt`
- Run `main.py`

If you have a bit of Python knowledge and you want this game to work offline, download the ["10k most common words" text file](https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-no-swears.txt) from GitHub and save it into the repo's `data` directory. Then edit line 16 of main.py to remove the `requests` call, and set `common` to use the same process as `longDict` on lines 23-30, changing the filename to match what you just saved and changing `allWords` to `commonWords`. Doing this also removes the dependence on `requests`, so if you want to set it up this way, you don't actually need to install `requests`.

## Development process
You can see a rough outline of my development process by checking out [pseudocode.md](pseudocode.md). This is where I jotted down notes as I planned out the features and worked through algorithms. I included it with the repo in case it can be helpful for other learners, e.g. to see how I broke things down into steps, or even just as an example of how you might write your own pseudocode. I'm a huge proponent of writing thorough pseudocode before you start actually coding a project!

I recorded two Twitch streams while working on this project, and I'm hoping to eventually edit and upload those videos somewhere, so that folks can have a chance to see what the problem solving process looked like in real time as well.

## Contributing
Since this is a personal portfolio project, I don't intend to accept any PRs, but please still feel free to fork the repo and play around with it for your own amusement!

If you have any feedback about how my code could be improved, I encourage you to leave a comment or file an issue instead. My goal is to learn, not to have the best Wordle clone ever, so if you see something wrong with my code, I would be more grateful for explanations of why it's wrong rather than just handing me a solution.

## License
The Hippocratic License is an *almost* open license that says you can do basically anything you want with this code as long as it doesn't hurt people. Check out [LICENSE.md](LICENSE.md) as well as the [Hippocratic License website](https://firstdonoharm.dev/).

## Acknowledgements
- Based on [Wordle](https://www.nytimes.com/games/wordle/index.html) from the New York Times
- Dictionary of secret word options comes from [GitHub repo "google-10000-english"](https://github.com/first20hours/google-10000-english/blob/master/google-10000-english-no-swears.txt)
- Dictionary of legal guesses is the "3 of 6 game" dictionary from [12dicts](http://wordlist.aspell.net/12dicts/) from the SCOWL project 
- Thanks to the [Codédex](https://www.codedex.io/) community for your support about the project!
- Extra special thanks to the folks who joined me on Twitch while I streamed working on this! ✨
- To my web dev [study group](): sorry I'm still ghosting yalls while I finish this project, thank you for your patience 🙏

## Author
Hey, I'm **caesiumtea**, AKA Vance! Feel free to contact me with any feedback.
- [Website and social links](https://caesiumtea.glitch.me/)
- [@caesiumtea_dev on Twitter](https://www.twitter.com/caesiumtea_dev)
- [@entropy@mastodon.social](https://mastodon.social/@entropy)