# Welcome to Jumper!
This was made by Anna Rector for CSE 210.

This game uses the Random module to pick a random word from a list of words. Then it allows the player to guess the letters of the word until either the word is completed, or the player reaches a set number of incorrect guesses. After the game is over, it asks if you want to play again.

This program is structured as follows:
- import random
- PlayGame class
    - init
    - get_guess
    - verify_guess
    - replace_letter
    - run_game
    - is_game_done
- SessionStats class
    - init
- GameMaster class
    - init
    - start_game_session
- DisplayBoard class
    - init
    - stages
    - incorrects_per_game
- Call to GameMaster

The required software to run this program is anything that can run Python in a terminal. The creator's reccomendation is Visual Studio Code.

Creator's emails: lighteternal.lunae@gmail.com | arector2002@gmail.com