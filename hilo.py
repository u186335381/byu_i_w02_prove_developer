import random
from pyray import text_to_lower
from player import Player
from card import Card

# The minimum and maximum card numbers are the following
MAX_CARD_NUMBER = 13
MIN_CARD_NUMBER = 1
INITIAL_SCORE = 300
CHOICES = ["h", "l"]


player = Player()

# The initial Score is the following
player.set_current_score(INITIAL_SCORE)

card = Card()

play_game = True
while play_game:
    # Chooses a random Card number between the minimum and the maximum available
    card.set_card_number(random.randrange(MIN_CARD_NUMBER, MAX_CARD_NUMBER))

    print(f"The card is: {card.get_card_number()}")

    # The new card number is randomly generated
    next_card = random.randrange(MIN_CARD_NUMBER, MAX_CARD_NUMBER)

    # We prevent the next_card number to be equals to the previous card so it can be greater or lower
    while next_card == card.get_card_number():
        next_card = random.randrange(MIN_CARD_NUMBER, MAX_CARD_NUMBER)

    # It is validated if the next card has a value greater or lower than the previous card
    if next_card > card.get_card_number():
        result = "h"
    elif next_card < card.get_card_number():
        result = "l"

    # We ask the game question
    pending_question = True
    while pending_question:

        choice = input("Higher or lower? [h/l] ")
        if text_to_lower(choice) == result:
            # The player earns 100 points
            player.set_current_score(player.get_current_score() + 100)
            pending_question = False
        elif text_to_lower(choice) in CHOICES:
            # The player loses 75 points
            player.set_current_score(player.get_current_score() - 75)
            pending_question = False
        else:
            print("Please enter a valid option")
            pending_question = True

    print(f"Next card was: {next_card}")
    print(f"Your score is: {player.get_current_score()}")

    pending_question = True
    while pending_question and player.get_current_score() > 0:
        play_game = input("Play again? [y/n] ")
        if text_to_lower(play_game) == "y":
            pending_question = False
            play_game = True
        elif text_to_lower(play_game) == "n":
            pending_question = False
            play_game = False
        else:
            print("Please enter a valid option")
            pending_question = True
            play_game = False

    if player.get_current_score() <= 0:
        play_game = False
