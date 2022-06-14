class Player:
    # This Class allow us to manage the current score a user has while he/she plays a game.

    def __init__(self):
        # In this Constructor we initialize the score of the user with the value 0
        self._score = 0

    def get_current_score(self):
        # It allow us to obtain the current score value of the Player
        return self._score

    def set_current_score(self, new_score):
        # It allow us to assign a new value to the score of he Player
        self._score = new_score
