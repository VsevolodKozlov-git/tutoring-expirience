import pygame
from pygame.sprite import Group
import sys
from time import sleep
from python_alien_invasion.settings import Settings
from python_alien_invasion.ship import Ship
from python_alien_invasion.bullet import Bullet
from python_alien_invasion.alien import Alien
from python_alien_invasion.game_stats import GameStats
from python_alien_invasion.buffs.speed_bullet_controller import SpeedBulletBuff


class AlienInvasion:
    def __init__(self):
        # Initialize pygame, settings, and screen object.
        self.ai_settings = Settings()
        self.screen = pygame.display.set_mode((self.ai_settings.screen_width,
                                               self.ai_settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        self.stats = GameStats(self.ai_settings)
        self.game_active = True
        self.speed_bullet_buff = SpeedBulletBuff(self)

        self.ship = Ship(self.ai_settings, self.screen)
        self.bullets = Group()

        self.aliens = Group()
        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_aliens()
                self._update_bullets()
                self.speed_bullet_buff.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen, each pass through the loop.
        self.screen.fill(self.ai_settings.bg_color)

        # Redraw all bullets, behind ship and aliens.
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _update_bullets(self):
        """Update position of bullets, and get rid of old bullets."""
        # Update bullet positions.
        self._move_bullets()
        self._remove_out_of_edge_bullets()
        self._check_bullet_alien_collide()

    def _move_bullets(self):
        self.bullets.update()

    def _remove_out_of_edge_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_bullet_alien_collide(self):
        pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

    def _fire_bullet(self):
        """Fire a bullet, if limit not reached yet."""
        # Create a new bullet, add to bullets group.
        if len(self.bullets) < self.ai_settings.bullets_allowed:
            bullet_angle = self.ai_settings.bullet_angle
            for angle in [-bullet_angle, 0, bullet_angle]:
                new_bullet = Bullet(self.ai_settings, self.screen, self.ship, angle)
                self.bullets.add(new_bullet)

    def _update_aliens(self):
        if self._check_fleet_edges():
            self.change_fleet_direction()

        if self._check_alien_ship_collide() or self._check_fleet_bottom():
            self._ship_hit()
        else:
            self.aliens.update()

    def _check_fleet_edges(self):
        for alien in self.aliens:
            if alien.check_edges():
                return True
        return False

    def _check_fleet_bottom(self):
        for alien in self.aliens:
            if alien.check_bottom():
                return True
        return False

    def _check_alien_ship_collide(self):
        return pygame.sprite.spritecollideany(self.ship, self.aliens)

    def _ship_hit(self):
        self.stats.ships_left -= 1
        if self.stats.ships_left > 0:
            self.aliens.empty()
            self.bullets.empty()
            # todo bullet buff update
            self.speed_bullet_buff.init_buff()

            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.game_active = False

    def change_fleet_direction(self):
        for alien in self.aliens:
            alien.rect.y += self.ai_settings.fleet_drop_distance
        self.ai_settings.fleet_direction *= -1

    def _create_fleet(self):
        alien_rows = self._compute_alien_rows()
        alien_cols = self._compute_alien_cols()
        for alien_row in range(alien_rows):
            for alien_col in range(alien_cols):
                self._create_alien(alien_row, alien_col)

    def _compute_alien_cols(self):
        sample_alien = Alien(self)
        alien_width = sample_alien.rect.width
        screen_width = self.ai_settings.screen_width

        available_space_x = screen_width - 2 * alien_width
        alien_cols = available_space_x // (2 * alien_width)

        return alien_cols

    def _compute_alien_rows(self):
        sample_alien = Alien(self)
        alien_height = sample_alien.rect.height
        ship_height = self.ship.rect.height
        screen_height = self.ai_settings.screen_height

        available_space_y = screen_height - (3 * alien_height) - ship_height
        alien_rows = available_space_y // (2 * alien_height)

        return alien_rows

    def _create_alien(self, row, col):
        alien = Alien(self)
        alien.x = float(alien.rect.width * (1 + 2 * col))
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height * (1 + 2 * row)
        self.aliens.add(alien)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
