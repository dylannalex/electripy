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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                possition = array([mx, my])
                if event.button == LEFT:
                    charge = Proton(possition)
                elif event.button == RIGHT:
                    charge = Electron(possition)
                else:
                    continue
                screen.add_charge(charge)
            # Key down events:
            elif event.type == pygame.KEYDOWN:
                key_pressed = pygame.key.name(event.key)
                if key_pressed == settings.KEYS["clear_screen"]:
                    screen.clear()
                if key_pressed == settings.KEYS["increment_scale_factor"]:
                    screen.increment_scale_factor()
                if key_pressed == settings.KEYS["decrement_scale_factor"]:
                    screen.decrement_scale_factor()
                if key_pressed == settings.KEYS["show_force_array"]:
                    screen.show_force_array()

        pygame.display.update()


def main():
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
