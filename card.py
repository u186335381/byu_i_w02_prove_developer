class Card:
    # This Class allow us to manage the current value of a Card that will be used while a user Plays a game.

    def __init__(self):
        # In this Constructor we initialize the Card number with the value 0
        self._card_number = 0

    def get_card_number(self):
        # It allow us to obtain the current value of the Card number
        return self._card_number

    def set_card_number(self, card_number):
        # It allow us to assign a new value to the Card number
        self._card_number = card_number
