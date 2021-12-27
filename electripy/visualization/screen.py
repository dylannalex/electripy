from numpy import array, ndarray
from numpy.linalg import norm
from math import acos, cos, sin, pi, sqrt
import pygame
from typing import Callable, Union
from electripy.physics.charges import Proton, Electron
from electripy.physics.charge_network import ChargeNetwork
from electripy.visualization import colors, settings, numbers
import pkg_resources


SOUND_PATH = pkg_resources.resource_filename(
    "electripy.visualization", "sounds/add_charge.wav"
)


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
        # Electric Field
        self.ef_vector = Vector(self._window, settings.DEFAULT_EF_VECTOR_SCALE_FACTOR)
        self.electric_field = Field(
            self._window,
            settings.DEFAULT_EF_BRIGHTNESS,
            self.charge_network.get_electric_field,
            settings.DEFAULT_SPACE_BETWEEN_EF_VECTORS,
        )

        # State attributes
        self.showing_vectors_components = False
        self.showing_electric_forces_vectors = False
        self.showing_electric_field_at_mouse_position = False
        self.showing_electric_field = True

        # Sounds setup
        self.add_charge_sound = pygame.mixer.Sound(SOUND_PATH)

        # Text setup
        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 13)
        self.text_color = colors.WHITE

    def clean(self) -> None:
        """Fills the screen with it's background color."""
        self._window.fill(self.background_color)

    def clear(self) -> None:
        """Restarts charge network."""
        self.charge_network = ChargeNetwork()
        self.clean()

    def add_charge(self, charge: Union[Proton, Electron]) -> None:
        """Adds a charge to the screen and to the charge network."""
        self.add_charge_sound.play()
        self.charge_network.add_charge(charge)
        self.electric_field.field_function = self.charge_network.get_electric_field
        self.refresh_screen()

    def show_electric_field_vector(self, x: int, y: int) -> None:
        """Shows the electric field vector at the given position."""
        position = array([x, y])
        ef = self.charge_network.get_electric_field(position)
        self._draw_vector(
            self.ef_vector,
            position,
            ef,
            AnimatedPoint.RADIUS,
            colors.GREEN,
            self.showing_vectors_components,
        )

    def increment_scale_factor(self) -> None:
        """
        Increments the ef_vector or force_vector factor depending
        on the current mode.
        """
        self.force_vector.scale_factor *= Vector.DELTA_SCALE_FACTOR
        self.ef_vector.scale_factor *= Vector.DELTA_SCALE_FACTOR
        self.refresh_screen()

    def decrement_scale_factor(self) -> None:
        """
        Decrements the ef_vector or force_vector factor depending
        on the current mode.
        """
        self.force_vector.scale_factor /= Vector.DELTA_SCALE_FACTOR
        self.ef_vector.scale_factor /= Vector.DELTA_SCALE_FACTOR
        self.refresh_screen()

    def increment_electric_field_brightness(self) -> None:
        if self.electric_field.brightness < Field.MAX_BRIGHTNESS:
            self.electric_field.brightness += Field.BRIGHTNESS_VARIATION

    def decrement_electric_field_brightness(self) -> None:
        if self.electric_field.brightness > Field.MIN_BRIGHTNESS:
            self.electric_field.brightness -= Field.BRIGHTNESS_VARIATION

    def _draw_vector(
        self,
        vector,
        position: ndarray,
        array: ndarray,
        radius: int,
        color: tuple,
        show_components: bool,
    ) -> None:
        vector.draw(position, array, radius, color)
        if show_components:
            self._display_arrays_components(vector.last_end_point, array)

    def _display_arrays_components(self, position: ndarray, array: ndarray):
        """Displays the arrays components next to the vector drawn."""
        x, y = numbers.array_to_string(array)
        x_text = self.font.render(x, True, self.text_color)
        y_text = self.font.render(y, True, self.text_color)
        self._window.blit(x_text, position)
        position[1] += 15
        self._window.blit(y_text, position)

    def refresh_screen(self, mx: int = None, my: int = None) -> None:
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

        if self.showing_electric_field:
            self.show_electric_field()

        if self.showing_electric_field_at_mouse_position:
            self.show_electric_field_vector(mx, my)

    def _draw_charge(self, charge: Union[Proton, Electron], force: ndarray) -> None:
        """Draws a charge and its force vector."""
        if isinstance(charge, Proton):
            color = AnimatedProton.COLOR
            radius = AnimatedProton.RADIUS

        if isinstance(charge, Electron):
            color = AnimatedElectron.COLOR
            radius = AnimatedElectron.RADIUS

        pygame.draw.circle(self._window, color, charge.position, radius)

        if len(self.charge_network) > 1 and self.showing_electric_forces_vectors:
            self._draw_vector(
                self.force_vector,
                charge.position,
                force,
                radius,
                colors.YELLOW,
                self.showing_vectors_components,
            )

    def show_electric_field(self) -> None:
        restricted_points = [
            charge.position for charge in self.charge_network.charges_set.charges
        ]
        self.electric_field.draw(restricted_points)


class Field:
    BRIGHTNESS_VARIATION = 25
    MAX_BRIGHTNESS = 205
    MIN_BRIGHTNESS = 50

    def __init__(
        self,
        window: pygame.Surface,
        brightness: int,
        field_function: Callable,
        space_between_vectors: int,
    ) -> None:
        """
        field_function must be a function that given a 2-dimensional vector
        returns another 2-dimensional vector.
        space_between_vectors is the amount of pixels between each vector. The
        shorter space_between_vectors is the more accurate the field will be.
        """
        self._window = window
        self.brightness = brightness
        self.vector_painter = ColoredVector(window)
        self.field_function = field_function
        self.space_between_vectors = space_between_vectors

    def _is_in_restricted_point(
        self, position: ndarray, restricted_points: list[ndarray]
    ) -> bool:
        for point in restricted_points:
            if norm(position - point) <= AnimatedProton.RADIUS * 2:
                return True
        return False

    def _get_field(self, restricted_points: list[ndarray]) -> list[dict]:
        field = []
        w, h = self._window.get_size()
        for x in range(0, w, self.space_between_vectors):
            for y in range(0, h, self.space_between_vectors):
                if self._is_in_restricted_point(array((x, y)), restricted_points):
                    continue
                field.append(
                    {"position": (x, y), "vector": (self.field_function((x, y)))}
                )
        return field

    @staticmethod
    def get_sorted_field_vectors(field: list[dict]) -> list[dict]:
        field_vectors = [d["vector"] for d in field]
        return sorted(field_vectors, reverse=True, key=norm)

    @staticmethod
    def get_greatest_norm(field: list[dict]) -> float:
        return norm(Field.get_sorted_field_vectors(field)[0])

    def draw(self, restricted_points: list[ndarray]) -> None:
        field = self._get_field(restricted_points)
        greatest_norm = Field.get_greatest_norm(field)
        red_blue_color_generator = colors.RedBlueColorGenerator(greatest_norm)
        for d in field:
            self.vector_painter.draw(
                d["position"],
                d["vector"],
                red_blue_color_generator.get_color(norm(d["vector"]), self.brightness),
            )


class Vector:
    DELTA_SCALE_FACTOR = 2
    DEFAULT_VECTOR_HEAD_LENGTH = 8
    DEFAULT_VECTOR_WIDTH = 2

    def __init__(self, window: pygame.Surface, scale_factor: int) -> None:
        self._window = window
        self.scale_factor = scale_factor
        self.last_end_point = [0, 0]

    def draw(self, position: tuple, vector: tuple, radius: int, color: tuple) -> None:
        """Draws a vector at the given position."""
        vector_norm = (vector[0] ** 2 + vector[1] ** 2) ** (1 / 2)
        unit_vector = [vector[0] / vector_norm, vector[1] / vector_norm]
        start_point = (
            position[0] + unit_vector[0] * radius,
            position[1] + unit_vector[1] * radius,
        )
        end_point = (
            start_point[0] + vector[0] * self.scale_factor,
            start_point[1] + vector[1] * self.scale_factor,
        )

        pygame.draw.line(
            self._window, color, start_point, end_point, Vector.DEFAULT_VECTOR_WIDTH
        )
        self._draw_vector_head(
            vector,
            end_point,
            color,
            Vector.DEFAULT_VECTOR_HEAD_LENGTH,
            Vector.DEFAULT_VECTOR_WIDTH,
        )
        self.last_end_point = end_point

    def _draw_vector_head(
        self, vector, vector_end_point, color, head_length, head_width
    ):
        vector_angle = Vector.get_angle(vector)
        if vector[1] < 0:
            vector_angle *= -1

        left_head_vector = (
            head_length * cos(vector_angle + pi * 5 / 4),
            head_length * sin(vector_angle + pi * 5 / 4),
        )
        left_head_endpoint = (
            vector_end_point[0] + left_head_vector[0],
            vector_end_point[1] + left_head_vector[1],
        )

        pygame.draw.line(
            self._window,
            color,
            vector_end_point,
            left_head_endpoint,
            head_width,
        )

        right_head_vector = (
            head_length * cos(vector_angle - pi * 5 / 4),
            head_length * sin(vector_angle - pi * 5 / 4),
        )
        right_head_endpoint = (
            vector_end_point[0] + right_head_vector[0],
            vector_end_point[1] + right_head_vector[1],
        )

        pygame.draw.line(
            self._window,
            color,
            vector_end_point,
            right_head_endpoint,
            head_width,
        )

    @staticmethod
    def get_norm(vector):
        return sqrt(vector[0] ** 2 + vector[1] ** 2)

    @staticmethod
    def get_angle(vector):
        return acos(vector[0] / Vector.get_norm(vector))


class ColoredVector(Vector):
    """
    Vector which length is determined by its color. The more red it
    is the grater its norm is.
    """

    DEFAULT_VECTOR_WIDTH = 2
    DEFAULT_HEAD_LENGTH = 4

    def __init__(
        self,
        window: pygame.Surface,
        scale_factor: int = 10,
    ) -> None:
        self._window = window
        self.scale_factor = scale_factor

    def draw(self, position: tuple, vector: tuple, color: tuple) -> None:
        """Draws a unit vector scaled by scale_factor at the given position."""
        vector_norm = (vector[0] ** 2 + vector[1] ** 2) ** (1 / 2)
        unit_vector = [vector[0] / vector_norm, vector[1] / vector_norm]

        end_point = [
            position[0] + unit_vector[0] * self.scale_factor,
            position[1] + unit_vector[1] * self.scale_factor,
        ]
        pygame.draw.line(
            self._window, color, position, end_point, ColoredVector.DEFAULT_VECTOR_WIDTH
        )
        self._draw_vector_head(
            vector,
            end_point,
            color,
            ColoredVector.DEFAULT_HEAD_LENGTH,
            ColoredVector.DEFAULT_VECTOR_WIDTH,
        )


class AnimatedProton:
    COLOR = colors.RED
    RADIUS = 20


class AnimatedElectron:
    COLOR = colors.BLUE
    RADIUS = 20


class AnimatedPoint:
    COLOR = colors.ORANGE
    RADIUS = 10
