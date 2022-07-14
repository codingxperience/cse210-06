from constants import *
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.game_over_message import GameOver
from game.casting.sound import Sound


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.

    The responsibility of HandleCollisionsAction is to handle the situation when
    a ship weapon collides with an Alien or an Alien touches the 570th pixel on
    the y axis of the screen.

    Attributes:
    ---
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self, audio_service):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._game_over_message = {"color": None, "message": ""}
        self._audio_service = audio_service

    def get_is_game_over(self):
        """Gets the game over boolean.

        Returns:
        ---
            _is_game_over (boolean): True or False
        """
        return self._is_game_over

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
        ---
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_collision(cast)
        else:
            self._handle_game_over(cast)

    def _handle_collision(self, cast):
        """Sets the game over flag if a ship weapon collides with an Alien
        or if the Alien touches the 570th pixel on the y axis.

        Args:
        ---
            cast (Cast): The cast of Actors in the game.
        """
        bullets = cast.get_actors("ship_weapon")
        score = cast.get_first_actor("score")
        ship = cast.get_first_actor("ship")
        alienslist = cast.get_first_actor("aliens")
        explosion = Sound(EXPLOSION_SOUND)
        game_over_sound = Sound(GAME_OVER)
        stage_clear = Sound(STAGE_CLEAR)

        if len(alienslist.get_segments()) == 0:
            self._is_game_over = True
            self._game_over_message["message"] = "You win!"
            self._game_over_message["color"] = GREEN
            ship.set_font_size(50)
            ship.set_position(Point(int((MAX_X/2)-50), int(MAX_Y/4)))
            self._audio_service.play_sound(stage_clear)

        for alien in alienslist.get_segments():
            if alien.get_position().get_y() >= MAX_Y-30:
                self._is_game_over = True
                self._audio_service.play_sound(game_over_sound)
                self._game_over_message["message"] = "Game Over!"
                self._game_over_message["color"] = RED

            for bullet in bullets:
                if alien.get_position().bounding_equals(bullet.get_position()):
                    alienslist._remove_alien(alien)

                    if bullet.get_text() == "{0}":
                        pass
                    else:
                        cast.remove_actor("ship_weapon", bullet)
                    score.add_points(alien.get_points())
                    self._audio_service.play_sound(explosion)

        for alien in alienslist.get_segments():
            if ship.get_position().bounding_equals(alien.get_position()):
                self._is_game_over = True
                self._game_over_message["message"] = "Game Over!"
                self._game_over_message["color"] = RED
                self._audio_service.play_sound(game_over_sound)

    def _handle_game_over(self, cast):
        """Shows the 'game over' message if the game is over.

        Args:
        ---
            cast (Cast): The cast of Actors in the game.
        """
        x = int(MAX_X / 2)
        y = int(MAX_Y / 2)
        position = Point(x-50, y)

        if self._is_game_over:
            game_over = GameOver()
            game_over.set_position(position)
            game_over.set_text(self._game_over_message["message"])
            game_over.set_color(self._game_over_message["color"])
            game_over.set_font_size(50)
            cast.add_actor("messages", game_over)
