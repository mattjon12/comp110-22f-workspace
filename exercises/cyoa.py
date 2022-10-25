"""Ex06 Wizard 101: Assignment of schools."""

__author__ = "730382085"
global player 
global points
points: int = 0
player: str = ""
 

def greet() -> None:
    """The purpose of this function is to greet the player and give some context to the game."""
print("Welcome to the universe of Wizard 101! This game is fun for all ages and playable on a personal computer. Once inside, you can experience a Wizard's journey from learning how to control and use magic to exploring far off places and using your magic to save other from harm. The purpose of this little game is to assign you to your wizard school so you can begin your adventures!!")
player = input("Hello young wizard, what is your name? ")
print(f"Have fun playing the game, {player}!! ")

def main() -> None:
    """This function is the main function that will ask the player a series of questions."""
personality_option_1: str = "smart"
personality_option_2: str = "funny"
personality_option_3: str = "vying"
personality_trait: str = input(f"Let's begin. How would you best describe yourself, {player}: smart, funny, or vying?")
greet()
while len(personality_trait) != 5:
        input("Error: word must be one of the three word choices, please try again!")
else:
    if personality_trait == personality_option_1:
        print("yay.")




    