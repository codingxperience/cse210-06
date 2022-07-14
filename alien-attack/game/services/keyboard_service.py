import pyray

from constants import *
from game.shared.point import Point


class KeyboardService:
    """Detects player input.

    The responsibility of a KeyboardService is to indicate whether or not a key is up or down.

    Attributes:
    ---
        _keys (Dict[string, int]): The letter to key mapping.
    """

    def __init__(self):
        """Constructs a new KeyboardService."""
        self._keys = {}

    def is_key_up(self, key):
        """Checks if the given key is currently up.

        Args:
        ---
            key (string): The given key (left arrow or right arrow)
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_up(pyray_key)

    def is_key_down(self, key):
        """Checks if the given key is currently down.

        Args:
        ---
            key (string): The given key (left arrow or right arrow)
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_down(pyray_key)

    def get_direction(self):
        """Gets direction based on user's keyboard input.
        """
        dx = 0
        dy = 0

        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -1

        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 1

        direction = Point(dx, dy)
        direction = direction.scale(15)

        return direction

    def fire_weapon(self):
        """Binds space button to fire ship's weapon.
        """
        if pyray.is_key_pressed(pyray.KEY_SPACE):
            return True
        else:
            return False

    def super_weapon(self):
        """Binds b button to super weapon.
        """
        if pyray.is_key_pressed(pyray.KEY_B):
            return True
        else:
            return False
