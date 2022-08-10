from python_alien_invasion.settings import Settings
from time import perf_counter
from pygame.time import Clock


class SpeedBulletBuff:
    def __init__(self, ai_game):
        self.time_remaining = 0
        self.ai_game = ai_game
        self.game_settings = ai_game.ai_settings
        self.default_settings = Settings()
        self.buff_active = False
        self.was_activated = False
        self.timer = Clock()
        self.timer.tick()

    def init_buff(self):
        self.deactivate()
        self.was_activated = False

    def activate(self):
        if not self.is_active():
            self.time_remaining = self.game_settings.speed_bullet_duration
            self.game_settings.bullet_speed_factor *= 2
            self.game_settings.bullet_width = 20

    def deactivate(self):
        self.time_remaining = 0
        self.game_settings.bullet_speed_factor = self.default_settings.bullet_speed_factor
        self.game_settings.bullet_width = self.default_settings.bullet_width

    def update(self):
        if len(self.ai_game.aliens) < 30 and not self.was_activated:
            self.activate()
            self.was_activated = True
        self.reduce_time()

    def is_active(self):
        return self.time_remaining != 0

    def reduce_time(self):
        elapsed_seconds = self.timer.tick() / 1000
        if self.time_remaining != 0:
            self.time_remaining -= elapsed_seconds
            if self.time_remaining < 0:
                self.deactivate()
