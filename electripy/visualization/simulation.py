import pygame
from electripy.visualization import settings, colors
from electripy.visualization.screen import Screen
from electripy.physics.charges import Proton, Electron
from numpy import array


LEFT = 1
RIGHT = 3


def start_simulation(screen: Screen, clock: pygame.time.Clock) -> None:
    while True:
        clock.tick(settings.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            # Mouse click events:
            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and not screen.showing_electric_field_at_mouse_position
            ):
                mx, my = event.pos
                position = array([mx, my])
                if event.button == LEFT:
                    charge = Proton(position)
                elif event.button == RIGHT:
                    charge = Electron(position)
                else:
                    continue
                screen.add_charge(charge)

            # Key down events:
            screen_state_changed = True
            if event.type == pygame.KEYDOWN:
                key_pressed = pygame.key.name(event.key)
                mods = pygame.key.get_mods()

                """Action keys"""
                # Key down combinations:
                if (
                    mods & pygame.KMOD_CTRL
                    and key_pressed == settings.KEYS["remove_last_charge_added"]
                ):  # CTRL + remove_last_charge_added key
                    screen.remove_last_charge_added()
                    continue

                # Single key down:
                if key_pressed == settings.KEYS["increment_electric_field_brightness"]:
                    screen.increment_electric_field_brightness()

                if key_pressed == settings.KEYS["decrement_electric_field_brightness"]:
                    screen.decrement_electric_field_brightness()

                if key_pressed == settings.KEYS["clear_screen"]:
                    screen.clear()
                    continue

                """ State keys: """
                # Single key down:
                if key_pressed == settings.KEYS["show_vector_components"]:
                    screen.showing_vectors_components = (
                        not screen.showing_vectors_components
                    )

                elif key_pressed == settings.KEYS["show_electric_forces_vectors"]:
                    screen.showing_electric_forces_vectors = (
                        not screen.showing_electric_forces_vectors
                    )

                elif (
                    key_pressed
                    == settings.KEYS["show_electric_field_at_mouse_position"]
                ):
                    screen.showing_electric_field_at_mouse_position = (
                        not screen.showing_electric_field_at_mouse_position
                    )

                elif key_pressed == settings.KEYS["show_electric_field"]:
                    screen.showing_electric_field = not screen.showing_electric_field

            else:
                screen_state_changed = False

            if screen_state_changed or screen.showing_electric_field_at_mouse_position:
                mx, my = pygame.mouse.get_pos()
                screen.refresh_screen(mx, my)

        pygame.display.update()


def main() -> None:
    pygame.init()
    # Screen setup
    screen = Screen(
        settings.WINDOW_TITLE,
        settings.HEIGHT,
        settings.WIDTH,
        settings.RESIZABLE,
        colors.BLACK,
    )

    # Start animation
    clock = pygame.time.Clock()
    start_simulation(screen, clock)
    pygame.quit()


if __name__ == "__main__":
    main()
