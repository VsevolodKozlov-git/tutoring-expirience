from python_alien_invasion.settings import  Settings
class GameStats:
    def __init__(self, ai_settings):
        self.settings: Settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit

