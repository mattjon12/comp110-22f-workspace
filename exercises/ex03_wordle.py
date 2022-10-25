"""Structured Wordle Practice."""

__author__ = "730382085"

def contains_char(multi_char_string: str, single_char_string: str) -> bool:
    """The function determines if the single character of the second string is found at any index of the first string."""
    assert len(single_char_string) == 1
    string_length: int = len(multi_char_string)
    index_parser: int = 0
    string_check: bool = False


    while string_length != index_parser:
        if multi_char_string[index_parser] == single_char_string:
            string_check = True
        index_parser = index_parser + 1
        
    if string_check is True:
        return True
    if string_check is False:
        return False


def emojified(user_input_guess: str, code_word: str) -> str:
    """Given two strings of equal length, the first a guess (user_input_guess) and the second a secret (secret_word), it will return a string of emoji whose color is codified."""
    assert len(user_input_guess) == len(code_word)

    GREEN_BOX: str = "\U0001F7E9"
    WHITE_BOX: str = "\U00002B1C"
    YELLOW_BOX: str = "\U0001F7E8"

    output: str = ""
    index_number: int = 0

    while len(code_word) != index_number: 
        if user_input_guess[index_number] == code_word[index_number]:
            output += GREEN_BOX
        else:
            if contains_char(code_word, user_input_guess[index_number]):
                output += YELLOW_BOX
            else:
                output += WHITE_BOX
        index_number = index_number + 1
    return output


def input_guess(integer: int) -> str:
    """Given an integer, the function will prompt the user for a guess of that length."""
    user_input_guess = input(f"Enter a {integer} character word: ")
    while len(user_input_guess) != integer:
        user_input_guess = input(f"That wasn't {integer} chars. Try again: ")
    if len(user_input_guess) == integer:
        return user_input_guess
    return user_input_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    code_word: str = "codes"
    user_input_guess: str = ""
    turn_total: int = 6
    integer: int = 5
    current_turn: int = 1
    while code_word != user_input_guess and turn_total >= current_turn:
        print(f"=== Turn { current_turn}/{turn_total } ===")
        user_input_guess = input_guess(integer)
        if user_input_guess == code_word:
            print(emojified(user_input_guess, code_word))
            print(f"You won in { current_turn}/{turn_total } turns!")
        if current_turn < turn_total and user_input_guess != code_word:
            print(emojified(user_input_guess, code_word))
        if current_turn >= turn_total and user_input_guess != code_word:
            print(emojified(user_input_guess, code_word))
            print(f"X/{turn_total} - Sorry, try again tomorrow!")
        current_turn = current_turn + 1


if __name__ == "__main__":
    main()