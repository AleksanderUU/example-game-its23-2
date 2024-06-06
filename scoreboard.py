import pygame.font


class Scoreboard():
    def __init__(self, game_settings, screen, stats):
        """Init scoreboard attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_settings = game_settings
        self.stats = stats
        # score attributes - size, color, font
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 46)
        # prepare grafical score
        self.prepare_score()

        self.high_score = self.load_high_score()

        # prepare grafical level
        self.prepare_level()
    
    def load_high_score(self):
        try:
            with open("highscore.txt", "r") as file:
                high_score = int(file.read())
        except FileNotFoundError:
            high_score = 0
        return high_score

    def save_high_score(self):
        with open("highscore.txt", "w") as file:
            file.write(str(self.high_score))

    def draw(self, stats):
        if stats.score > self.high_score:
            self.high_score = stats.score
            self.save_high_score()

        high_score_text = "Highest Score: " + str(self.high_score)
        high_score_surface = self.font.render(high_score_text, True, (255, 255, 255))

        high_score_rect = high_score_surface.get_rect(center=(self.screen.get_width() / 2, self.screen.get_height() / 2 - 150 ))

        self.screen.blit(high_score_surface, high_score_rect)

    def prepare_score(self):
        """Convert score to grafics component"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.game_settings.bg_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right - 20
        self.score_image_rect.top = 20

    def prepare_level(self):
        """Convert level to grafics component"."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.game_settings.bg_color)
        # Level is appear under score value.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_image_rect.right
        self.level_rect.top = self.score_image_rect.bottom + 10

    def draw_score(self):
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.level_image, self.level_rect)
    
