import random
    # Imports the Random module
    
class PlayGame:
    # Initializes each new game
    def __init__(self):
        word_list = ["jazzy", "lucky", "books", "class", "lower", "apple", "dream", "plane", "grape", "great"]
        self.word = random.choice(word_list)
        self.word_completion = "_" * len(self.word)
        self.guessed_letters = []
        self.failed_tries = 0
        self.board = displayBoard()

    def get_guess(self):
    # Gets a letter guess from the player, calls verify_guess
        self.guess = input("Guess a letter [a-z]: ").lower()
        self._verify_guess()

    def _verify_guess(self):
    # Checks to make sure the guess is valid, then adds the guessed letter to the list of guessed letters if it isn't already
    # Calls replace_letter if the guess is correct
        if len(self.guess) != 1:
            print("Please guess a single letter.")
        elif self.guess in self.guessed_letters:
            print("You already guessed that letter. Try again.")
        elif self.guess not in self.word:
            self.failed_tries += 1
            print(f"{self.guess} is not in the word.")
            self.guessed_letters.append(self.guess)
        else:
            print(f"{self.guess} is in the word!")
            self.guessed_letters.append(self.guess)
            self._replace_letter()

    def _replace_letter(self):
    # Iterates through each letter in the word to find its position. Replaces the guessed letter with the blank spot in the correct position
        word_as_list = list(self.word_completion)
        letters = [i for i, letter in enumerate(self.word) if letter == self.guess]
        for letter in letters:
            word_as_list[letter] = self.guess
        self.word_completion = "".join(word_as_list)

    def run_game(self):
    # Prints the board and the word completion. Calls get_guess. Calls IsGameDone, and if it returns True, stops the loop
        while True:
            print()
            self.board.stages(self.failed_tries)
            print(self.word_completion)
            self.get_guess()
            if self._is_game_done():
                return

    def _is_game_done(self):
    # Checks if the number of incorrect guesses has reached the cap, and returns True if so.
    # Checks if the word has been completed and returns True if so
    # Otherwise, returns False
        if self.failed_tries == self.board.incorrects_per_game():
            self.board.stages(self.failed_tries)
            print(f"Sorry, you lost! The word was {self.word}.")
            return True
        elif self.word_completion == self.word:
            self.board.stages(self.failed_tries)
            print(self.word_completion)
            print(f"Good job! The word was {self.word}!")
            return True
        return False

class SessionStats:
    # Stores the amount of times played
    def __init__(self):
        self.times_played = 0

class GameMaster:
    # Initializes the amount of times played every time the program starts
    def __init__(self):
        self.session_stats = SessionStats()

    def start_game_session(self):
    # Makes the program aware that it is the first time running the program. Prints the welcome dialogue
    # Builds a game and increments the amount of times played
    # Sets first to False so the game knows to ask to play again
    # Continues to ask if the player wants to play again after each game. If no, stops the loop and shows the amount of times player
        first = True
        print("Welcome to Jumper!")
        print("You will have to guess a randomly-chosen word. You must guess the word. Each wrong guess removes another layer of the stick figure jumper. Once his head becomes an 'x', the game is over.")

        while True:
            if first != True:
                cont_game = input("Do you want to play again? [y/n] ").lower()
                if cont_game == "n":
                    print("Thanks for playing!")
                    print(f"Times Played: {self.session_stats.times_played}")
                    return
            
            self.session_stats.times_played += 1
            PlayGame().run_game()

            first = False

class displayBoard:
    # Initializes the "jumper" ASCII art
    def __init__(self):
        self._jumper = [
            """
     ___ 
    /___\\
    \\   /
     \\ /
      0
     /|\\
     / \\

    ^^^^^^^
    """,
    """
    \\   /
     \\ /
      0
     /|\\
     / \\

    ^^^^^^^
    """,
    """
    \\ /
     0
    /|\\
    / \\

    ^^^^^^^
    """,
    """
     0
    /|\\
    / \\

    ^^^^^^^
    """,
    """
     x
    /|\\
    / \\

    ^^^^^^^
    """
    ]

    def stages(self, failed_tries):
        # Prints a different stick figure based on how many incorrect guesses have been made
        print(self._jumper[failed_tries])

    def incorrects_per_game(self):
        # Returns the amount of incorrect guesses allowed
        return len(self._jumper) - 1

if __name__ == "__main__":
    # Builds a game and starts the session
    GameMaster().start_game_session()