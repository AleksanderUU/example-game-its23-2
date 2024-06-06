class Settings:
    """Class for game settings"""
    
    
    def __init__(self) :
        """Inttialize game settings"""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 139)
        self.caption = 'Bubble Bluster'

        self.bubble_min_r = 16
        self.bubble_max_r = 50
        self.bubble_speed = 1
        self.speed_increment = 1

        self.bonus_score = 1000