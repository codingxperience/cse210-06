from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.

    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
    ---
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.

        Args:
        ---
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
        ---
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        ship_weapon = cast.get_actors("ship_weapon")
        score = cast.get_first_actor("score")
        ship = cast.get_first_actor("ship")
        aliens = cast.get_first_actor("aliens")
        messages = cast.get_actors("messages")
        alien_segments = aliens.get_segments()

        self._video_service.clear_buffer()
        self._video_service.draw_actors(ship_weapon)
        self._video_service.draw_actor(score)
        self._video_service.draw_actors(alien_segments)
        self._video_service.draw_actors(messages, True)
        self._video_service.draw_actor(ship)
        self._video_service.flush_buffer()
