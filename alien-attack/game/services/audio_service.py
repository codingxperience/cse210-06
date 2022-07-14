import pyray
import pathlib


class AudioService:
    """Creates audio for Spaceship

    The responsibility of AudioService is to make sounds for when the spaceship
    fires a rocket or destroys an alien
    """

    def __init__(self):
        """Constructs a new Audio Service."""
        self._sounds = {}

    def initialize(self):
        """Initializes audio"""
        pyray.init_audio_device()

    def play_sound(self, sound):
        """finds audio location and begins playing sound

        Args:
        ---
            sound (.wav): Gets sound location and plays it
        """
        filepath = sound.get_filename()
        filepath = str(pathlib.Path(filepath))
        soundl = pyray.load_sound(filepath)
        self._sounds[filepath] = soundl
        pyray.set_sound_volume(self._sounds[filepath], sound.get_volume())
        pyray.play_sound(self._sounds[filepath])

    def release(self):
        """Stops audio"""
        pyray.close_audio_device()

    def is_sound_playing(self, sound):
        """Keeps the audio playing

        Args:
        ---
            sound (.wav): Gets sound location and plays it

        Returns:
        ---
            isPlaying (method): A method with a dictionary passed in which contains a file path.
        """
        filepath = sound.get_filename()
        filepath = str(pathlib.Path(filepath))
        sound = self._sounds[filepath]
        isPlaying = pyray.is_sound_playing(self._sounds[filepath])
        return isPlaying
