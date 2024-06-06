class GameStats():
    """Check game statistics"""

    def __init__(self):
        """Initialize statistics. """
        # game starts in nonactive condition
        self.game_active = False
        self.reset_stats()


    def reset_stats(self):
        """Initialize score, which can change during the game."""
        self.score = 0
        self.level = 1
        self.bonus = 0
    
    def highscore_get(self):
        with open ("highscore.txt", "r") as file:
            highscore = int(file.read())
        return highscore
    
    
    def highscore_update(self, score):
        current_highscore = self.highscore_get()  # Retrieve the current high score
        if score >= current_highscore:
            self.highscore = score
            with open("highscore.txt", "w") as file:
                file.write(str(score))