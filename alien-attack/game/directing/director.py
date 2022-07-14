from constants import *

from game.casting.sound import Sound


class Director:
    """A person who directs the game.
    The responsibility of a Director is to control the sequence of play.

    Attributes:
    ---
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
        _score (int): A default score set to an integer of 100.
    """

    def __init__(self, keyboard_service, video_service, audio_service):
        """Constructs a new Director using the specified keyboard and video services.

        Args:
        ---
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
            audio_service (AudioService): An instance of AudioService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._audio_service = audio_service
        self._score = 100
        self._music_loop = Sound(LOOP_SOUND, volume=0.75, repeat=True)

    def start_game(self, cast, script):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
        ---
            cast (Cast): The cast of actors.
            script (Script): The script of actions in the game.
        """
        self._video_service.open_window()
        self._audio_service.initialize()
        self._audio_service.play_sound(self._music_loop)
        while self._video_service.is_window_open():
            if not self._audio_service.is_sound_playing(self._music_loop):
                self._audio_service.play_sound(self._music_loop)
            self._execute_actions("input", cast, script)
            self._execute_actions("update", cast, script)
            self._execute_actions("output", cast, script)
        self._video_service.close_window()

    def _execute_actions(self, group, cast, script):
        """Calls execute for each action in the given group.

        Args:
        ---
            group (string): The action group name.
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        actions = script.get_actions(group)
        for action in actions:
            action.execute(cast, script)
