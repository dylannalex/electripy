from numpy import array, ndarray
import pygame
from typing import Union
from electripy.physics.charges import PointCharge, Proton, Electron
from electripy.physics.charge_network import ChargeNetwork
from electripy.visualization import colors, settings, numbers


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
        self.force_vector = Vector(
            self._window, settings.DEFAULT_FORCE_VECTOR_SCALE_FACTOR
        )
        self.ef_vector = Vector(self._window, settings.DEFAULT_EF_VECTOR_SCALE_FACTOR)

        # State attributes
        self.mode = "electric_force"
        self._show_force_components = False
        self._show_ef_components = True

        # Sounds setup
        self.add_charge_sound = pygame.mixer.Sound(
            "electripy/visualization/sounds/add_charge.wav"
        )

        # Text setup
        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 13)
        self.text_color = colors.WHITE

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

    def show_electric_field(self, x, y):
        self._refresh_screen()
        position = array([x, y])
        ef = self.charge_network.get_electric_field(position)
        self._draw_vector(
            self.ef_vector,
            position,
            ef,
            AnimatedPoint.RADIUS,
            colors.GREEN,
            self._show_ef_components,
        )

    def increment_scale_factor(self) -> None:
        if self.mode == "electric_force":
            self.force_vector.scale_factor *= Vector.DELTA_SCALE_FACTOR

        if self.mode == "electric_field":
            self.ef_vector.scale_factor *= Vector.DELTA_SCALE_FACTOR

        self._refresh_screen()

    def decrement_scale_factor(self) -> None:
        if self.mode == "electric_force":
            self.force_vector.scale_factor /= Vector.DELTA_SCALE_FACTOR

        if self.mode == "electric_field":
            self.ef_vector.scale_factor /= Vector.DELTA_SCALE_FACTOR

        self._refresh_screen()

    def show_components(self):
        if self.mode == "electric_field":
            self._show_ef_components = not self._show_ef_components
        if self.mode == "electric_force":
            self._show_force_components = not self._show_force_components
        self._refresh_screen()

    def change_mode(self):
        if self.mode == "electric_force":
            self.mode = "electric_field"
        else:
            self.mode = "electric_force"
        self._refresh_screen()

    def _draw_vector(
        self,
        vector,
        position: ndarray,
        array: ndarray,
        radius: int,
        color: tuple,
        show_components: bool,
    ):
        vector.draw(position, array, radius, color)
        if show_components:
            self._display_arrays_components(vector.last_end_point, array)

    def _display_arrays_components(self, position, array):
        """Displays the arrays components next to the vector drawn"""
        x, y = numbers.array_to_string(array)
        x_text = self.font.render(x, True, self.text_color)
        y_text = self.font.render(y, True, self.text_color)
        self._window.blit(x_text, position)
        position[1] += 15
        self._window.blit(y_text, position)

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

        pygame.draw.circle(self._window, color, charge.position, radius)

        if len(self.charge_network) > 1:
            self._draw_vector(
                self.force_vector,
                charge.position,
                force,
                radius,
                colors.YELLOW,
                self._show_force_components,
            )


class Vector:
    DELTA_SCALE_FACTOR = 2

    def __init__(self, window, scale_factor):
        self._window = window
        self.scale_factor = scale_factor
        self.last_end_point = [0, 0]

    def draw(self, position: tuple, vector: tuple, radius: int, color: tuple):
        vector_norm = (vector[0] ** 2 + vector[1] ** 2) ** (1 / 2)
        unit_vector = [vector[0] / vector_norm, vector[1] / vector_norm]
        start_point = [
            position[0] + unit_vector[0] * radius,
            position[1] + unit_vector[1] * radius,
        ]
        end_point = [
            start_point[0] + vector[0] * self.scale_factor,
            start_point[1] + vector[1] * self.scale_factor,
        ]

        pygame.draw.line(self._window, color, start_point, end_point, 2)
        self.last_end_point = end_point


class AnimatedProton:
    COLOR = colors.RED
    RADIUS = 20


class AnimatedElectron:
    COLOR = colors.BLUE
    RADIUS = 20


class AnimatedPoint:
    COLOR = colors.ORANGE
    RADIUS = 10
