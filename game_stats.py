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