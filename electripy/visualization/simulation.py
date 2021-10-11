import pygame
from electripy.visualization import settings, colors
from electripy.visualization.screen import Screen
from electripy.physics.charges import Proton, Electron
from numpy import array


LEFT = 1
RIGHT = 3


def start_simulation(screen:Screen, clock: pygame.time.Clock) -> None:
    while True:
        clock.tick(settings.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
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
