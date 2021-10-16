from numpy import ndarray
import pygame
from typing import Union
from electripy.physics.charges import Proton, Electron
from electripy.physics.charge_network import ChargeNetwork
from electripy.visualization import colors, settings, string


class Screen:
    def __init__(
        self,
        title: str,
        height: int,
        width: int,
        resizable: bool,
        background_color: str,
    ):
        # Window setup
        pygame.display.set_caption(title)
        if resizable:
            self._window = pygame.display.set_mode((height, width), pygame.RESIZABLE)
        else:
            self._window = pygame.display.set_mode((height, width))
        self.background_color = background_color
        self.clean()

        # Charge network and Vector setup
        self.charge_network = ChargeNetwork()
        self.vector = Vector(
            self._window, settings.DEFAULT_VECTOR_SCALE_FACTOR, colors.YELLOW
        )

        # Sounds setup
        self.add_charge_sound = pygame.mixer.Sound(
            "electripy/visualization/sounds/add_charge.wav"
        )

        # Text setup
        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 13)
        self.text_color = colors.WHITE
        self._show_force_array = False

    def clean(self) -> None:
        """Fills the screen with it's background color"""
        self._window.fill(self.background_color)

    def clear(self) -> None:
        """Restarts charge network"""
        self.charge_network = ChargeNetwork()
        self.clean()

    def add_charge(self, charge) -> None:
        """Adds a charge to the screen and to the charge network"""
        self.add_charge_sound.play()
        self.charge_network.add_charge(charge)
        self._refresh_screen()

    def increment_scale_factor(self) -> None:
        self.vector.scale_factor *= Vector.DELTA_SCALE_FACTOR
        self._refresh_screen()

    def decrement_scale_factor(self) -> None:
        self.vector.scale_factor /= Vector.DELTA_SCALE_FACTOR
        self._refresh_screen()

    def show_force_array(self):
        if self._show_force_array:
            self._show_force_array = False
        else:
            self._show_force_array = True
        self._refresh_screen()

    def _display_force_array(self, possition, force):
        """Displays the force array next to the force vector drawn"""
        x, y = string.array_to_string(force)
        x_text = self.font.render(x, True, self.text_color)
        y_text = self.font.render(y, True, self.text_color)
        self._window.blit(x_text, possition)
        possition[1] += 15
        self._window.blit(y_text, possition)

    def _refresh_screen(self) -> None:
        """
        Cleans the screen, get electric forces and calls _draw_charge
        for each charge on screen.
        """
        self.clean()
        electric_forces = self.charge_network.get_electric_forces()
        for ef in electric_forces:
            charge = ef[0]
            force = ef[1]
            self._draw_charge(charge, force)

    def _draw_charge(self, charge: Union[Proton, Electron], force: ndarray) -> None:
        """Draws a charge and its force vector"""
        if isinstance(charge, Proton):
            color = AnimatedProton.COLOR
            radius = AnimatedProton.RADIUS

        if isinstance(charge, Electron):
            color = AnimatedElectron.COLOR
            radius = AnimatedElectron.RADIUS

        pygame.draw.circle(self._window, color, charge.possition, radius)

        if len(self.charge_network) > 1:
            self.vector.draw(charge.possition, force, radius)
            if self._show_force_array:
                self._display_force_array(self.vector.last_end_point, force)


class Vector:
    DELTA_SCALE_FACTOR = 2

    def __init__(self, window, scale_factor, color):
        self._window = window
        self.scale_factor = scale_factor
        self.color = color
        self.last_end_point = [0, 0]

    def draw(self, possition: tuple, vector: tuple, radius: int):
        vector_norm = (vector[0] ** 2 + vector[1] ** 2) ** (1 / 2)
        unit_vector = [vector[0] / vector_norm, vector[1] / vector_norm]
        start_point = [
            possition[0] + unit_vector[0] * radius,
            possition[1] + unit_vector[1] * radius,
        ]
        end_point = [
            start_point[0] + vector[0] * self.scale_factor,
            start_point[1] + vector[1] * self.scale_factor,
        ]
        pygame.draw.line(self._window, self.color, start_point, end_point, 2)
        self.last_end_point = end_point


class AnimatedProton:
    COLOR = colors.RED
    RADIUS = 20


class AnimatedElectron:
    COLOR = colors.BLUE
    RADIUS = 20
