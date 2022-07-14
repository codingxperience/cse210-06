from constants import *
from game.casting.actor import Actor
from game.shared.point import Point


class Alien(Actor):
    """Aliens that are invading your ship

    The responsibility of Alien is to move down and reach the bottom of the screen

    Attributes:
    ---
        _segments(list): segments of alien invaders
        _prepare_alien (method): A method that will create the ship for each instance of Ship.

    """

    def __init__(self):
        """Constructs a new Alien."""
        super().__init__()
        self._segments = []
        self._prepare_alien(Point(100, 100))

    def get_segments(self):
        """Gets the segments for each cycle.

        Returns:
        ---
            List: The list of actors for each cycle"""
        return self._segments

    def move_next(self):
        """Moves the actor to its next position according to its velocity. Will wrap the position
            from one side of the screen to the other when it reaches the given maximum x and y values.
        """
        for segment in self._segments:
            segment.move_next()

    def set_ship_color(self, color):
        """Sets the color for each segment of a cycle.

            Args:
            ---
                color (Color): The given color.
            """

        self._color = color
        self._segments[0].set_color(self._color)

    def _prepare_alien(self, position):
        """Sets the Alien's design, speed, and color.

            Args:
            ---
                position (Point): The position and direction that each cycle will travel in at game start.
            """
        x = position.get_x()
        y = position.get_y()
        points = [15,10,5,20]
        font = ["a", "c", "e", "h"]
        for x in range(30, 870, 30):
            for y in range(4):
                position = Point(x + 0 * 15, 30 + y * 15)
                velocity = Point(0, 1)
                text = font[y]

                segment = Actor()
                segment.set_font(ALIENS_FONT)
                segment.set_position(position)
                segment.set_velocity(velocity)
                segment.set_text(text)
                segment.set_color(ALIEN_COLORS[y-1])
                segment.set_points(points[y-1])
                self._segments.append(segment)

    def _remove_alien(self, alien):
        """Removes an Alien from the screen.

        Args:
        ---
            alien (type <class>): An Alien object.
        """
        self._segments.remove(alien)
