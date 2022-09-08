"""One Shot Wordle - Practice with formatted strings"""

__author__ = "730382085"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

output: str = ""
secret_word: str = "python"
secret_length: int = len(secret_word)
index_number: int = 0
other_indices_counter: int = 0

user_guessed_word: str = input(f"What is your {secret_length} letter guess? ")

if len(user_guessed_word) != len(secret_word):
    input(f"That was not {secret_length} letters! Try again:")

if user_guessed_word == secret_word:
    while secret_length != index_number:
        if user_guessed_word[index_number] == secret_word[index_number]:
            output += GREEN_BOX
        index_number = index_number + 1
    print(output)
    print("Woo! You got it!")

if user_guessed_word != secret_word:
    while secret_length != index_number:
        if user_guessed_word[index_number] == secret_word[index_number]:
            output += GREEN_BOX
        else:
            yellow_or_white_box_tracker: bool = False
            other_indices_counter = 0 

            while other_indices_counter != secret_length:
                if user_guessed_word[index_number] == secret_word[other_indices_counter]:
                    yellow_or_white_box_tracker = True
                other_indices_counter = other_indices_counter + 1
            if yellow_or_white_box_tracker is True:
                output += YELLOW_BOX
            if yellow_or_white_box_tracker is False:
                output += WHITE_BOX    
        index_number = index_number + 1

    print(output)    
    print("Not quite. Play again soon!")