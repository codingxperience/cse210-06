from constants import *
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.actor import Actor
from game.casting.sound import Sound


class ActorInputs(Action):
    """Gets the inputs for the actors

    The responsibility of ActorInputs is to get the input from the user and and create
    the ship weapon and get directional input

    Attributes:
    ---
        _keyboard_service: An instance of KeyboardService
        _audio_service: An instance of AudioService
    """

    def __init__(self, keyboard_services, audio_service):
        """Constructs a new instance of ActorInputs"""
        self._keyboard_service = keyboard_services
        self._audio_service = audio_service

    def execute(self, cast, script):
        """Executes the Actor inputs.

        Args:
        ---
            cast (Cast): The cast of actors.
            script (Script): The script of actions in the game.
        """
        self._get_inputs(cast)

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.

        Args:
        ---
            cast (Cast): The cast of actors.
        """
        ship = cast.get_first_actor("ship")
        velocity = self._keyboard_service.get_direction()
        ship.set_velocity(velocity)
        fire_sound = Sound(SHOT_SOUND)

        if self._keyboard_service.fire_weapon():
            ship_weapon = Actor()
            ship_weapon.set_position(ship.get_position())
            ship_weapon.set_velocity(Point(0, -7))
            ship_weapon.set_text("!")
            ship_weapon.set_font_size(FONT_SIZE)
            ship_weapon.set_color(YELLOW)
            cast.add_actor("ship_weapon", ship_weapon)
            self._audio_service.play_sound(fire_sound)

        if self._keyboard_service.super_weapon():
            bullets = cast.get_actors("ship_weapon")
            for bullet in bullets:
                if bullet.get_text() == "{0}":
                    return

            ship_weapon = Actor()
            ship_weapon.set_position(ship.get_position())
            ship_weapon.set_velocity(Point(0, -5))
            ship_weapon.set_text("{0}")
            ship_weapon.set_font_size(FONT_SIZE)
            ship_weapon.set_color(RED)
            cast.add_actor("ship_weapon", ship_weapon)
            self._audio_service.play_sound(fire_sound)
