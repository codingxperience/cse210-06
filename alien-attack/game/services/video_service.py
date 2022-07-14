import pyray
from constants import *


class VideoService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state
    on the screen.
    """

    def __init__(self, debug=False):
        """Constructs a new VideoService using the specified debug mode.

        Args:
        ---
            debug (bool): whether or not to draw in debug mode.
        """
        self._debug = debug
        self._alien_font = None
        self._space_invaders_font = None
        self._font_options = None

    def close_window(self):
        """Closes the window and releases all computing resources."""
        pyray.close_window()

    def clear_buffer(self):
        """Clears the buffer in preparation for the next rendering. This method should be called at
        the beginning of the game's output phase.
        """
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        if self._debug == True:
            self._draw_grid()

    def draw_actor(self, actor, centered=False):
        """Draws the given actor's text on the screen.

        Args:
        ---
            actor (Actor): The actor to draw.
        """
        text = actor.get_text()
        x = actor.get_position().get_x()
        y = actor.get_position().get_y()
        font_size = actor.get_font_size()
        font = self._font_options[actor.get_font()]
        color = actor.get_color().to_tuple()
        position = pyray.Vector2(x, y)

        if centered:
            width = pyray.measure_text(text, font_size)
            offset = int(width / 2)
            x -= offset

        pyray.draw_text_ex(font, text, position, font_size, 0, color)

    def draw_actors(self, actors, centered=False):
        """Draws the text for the given list of actors on the screen.

        Args:
        ---
            actors (list): A list of actors to draw.
        """

        for actor in actors:
            self.draw_actor(actor, centered)

    def flush_buffer(self):
        """Copies the buffer contents to the screen. This method should be called at the end of
        the game's output phase.
        """
        pyray.end_drawing()

    def is_window_open(self):
        """Whether or not the window was closed by the user.

        Returns:
        ---
            bool: True if the window is closing; false if otherwise.
        """
        return not pyray.window_should_close()

    def open_window(self):
        """Opens a new window with the provided title.

        Args:
        ---
            title (string): The title of the window.
        """
        pyray.init_window(MAX_X, MAX_Y, CAPTION)
        pyray.set_target_fps(FRAME_RATE)
        self._alien_font = pyray.load_font(ALIENS_FONT)
        self._space_invaders_font = pyray.load_font(LETTER_FONT)
        self._font_options = {
            ALIENS_FONT: self._alien_font,
            LETTER_FONT: self._space_invaders_font
        }

    def _draw_grid(self):
        """Draws a grid on the screen."""
        for y in range(0, MAX_Y, CELL_SIZE):
            pyray.draw_line(0, y, MAX_X, y, pyray.GRAY)

        for x in range(0, MAX_X, CELL_SIZE):
            pyray.draw_line(x, 0, x, MAX_Y, pyray.GRAY)

    def _get_x_offset(self, text, font_size):
        """Gets the offset measurement for the text.

        Args:
        ---
            text (string): The actor's textual representation.
            font_size (constant): The size of an actor.
        """
        width = pyray.measure_text(text, font_size)
        return int(width / 2)
