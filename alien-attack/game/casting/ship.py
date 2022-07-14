"""
Aurthor: Fred Okorio
Task: Code the the ship class with methods
""" 

from constants import *
from game.casting.actor import Actor
from game.shared.point import Point


class Ship(Actor):
    """An elite fighter space ship that is part of The Interstellar Armed Forces.

    The responsibility of Ship is to move itself.
    """

    def __init__(self):
        """Constructs a new Ship."""
        super().__init__()

    def move_next(self):
        """Moves the actor to its next position according to its velocity. Will wrap the position
        from one side of the screen to the other when it reaches the given maximum x and y values.
        """
        if self._position.get_x() >= 0 and self._position.get_x() <= 870:
            x = (self._position.get_x() + self._velocity.get_x())
            y = (self._position.get_y() + self._velocity.get_y())
            if x < 0:
                x = 0
            if x > 870:
                x = 870
            self._position = Point(x, y)

    def set_ship_color(self, color):
        """Sets the color for each segment of a cycle.

            Args:
            ---
                color (Color): The given color.
            """
        self._color = color
        self._segments[0].set_color(self._color)

    def set_name(self, name):
        """Sets the name for each player.

            Args:
            ---
                String: The players given name as text.
            """
        self._name = name
