from numpy import ndarray
import pygame
from electripy.physics.charges import Proton, Electron
from electripy.physics.charge_network import ChargeNetwork
from electripy.visualization import colors, settings
from typing import Union


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

    def clean(self) -> None:
        """Fills the screen with it's background color"""
        self._window.fill(self.background_color)

    def add_charge(self, charge) -> None:
        """Adds a charge to the screen and to the charge network"""
        self.charge_network.add_charge(charge)
        self._refresh_screen()

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


class Vector:
    def __init__(self, window, scale_factor, color):
        self._window = window
        self.scale_factor = scale_factor
        self.color = color

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


class AnimatedProton:
    COLOR = colors.RED
    RADIUS = 20


class AnimatedElectron:
    COLOR = colors.BLUE
    RADIUS = 20
