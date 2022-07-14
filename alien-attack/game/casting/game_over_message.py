import random
from constants import *
from game.casting.actor import Actor
from game.shared.color import Color


class GameOver(Actor):
    """
    Displays a Game Over Message

    Attributes:
    ---
        _color (constant): The color value the game over message is displayed in.
    """

    def __init__(self):
        "Constructs a game over message."
        super().__init__()
        self._color = GREEN

    def get_color(self):
        """Gets the actor's color as a tuple of three ints (r, g, b).

        Returns:
        ---
            Color: random rainbow color
        """
        return Color(random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))

    def set_color(self, color):
        """Updates the color to the given one.

        Args:
        ---
            color (Color): The given color.
        """
        return super().set_color(color)
