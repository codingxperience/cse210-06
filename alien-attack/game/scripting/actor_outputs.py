from game.scripting.action import Action


class ActorOutputs(Action):
    """displays output for the actors

    The responsibility of ActorOutputs is to display the actors on the screen
    """

    def _do_outputs(self, cast):
        """Draws the actors on the screen.

        Args:
        ---
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
