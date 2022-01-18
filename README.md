# ElectriPy :zap:

[![Downloads](https://pepy.tech/badge/electripy)](https://pepy.tech/project/electripy)
![licence](https://img.shields.io/github/license/dylannalex/electripy?color=blue)

<p align="center">
  <img width="400" height="400" src="../media/electripy-demo.gif?raw=true">
</p>

Visualize the electric field of a point charges network.

## :electric_plug: Installation

Install Pygame and ElectriPy package:

```
$ pip install pygame
$ pip install electripy
```

You are all done! To start the simulation type:

```
$ python -m electripy
```

_NOTE:_ you need to have **Python** and **pip** installed.

## :electric_plug: Controls

- <kbd>right click</kbd> to add an electron
- <kbd>left click</kbd> to add a proton
- <kbd>CTRL</kbd> + <kbd>Z</kbd> to remove last charge added
- <kbd>CTRL</kbd> + <kbd>Y</kbd> to add last charge removed 
- <kbd>R</kbd> to remove all charges from screen
- <kbd>E</kbd> to show/hide the electric field
- <kbd>+</kbd> to increment the electric field brightness
- <kbd>-</kbd> to decrement  the electric field brightness
- <kbd>F</kbd> to show/hide electric force vectors
- <kbd>M</kbd> to show/hide electric field vector at cursor position
- <kbd>SPACE</kbd> to show/hide vectors components

## :electric_plug: Physics

You can check out a simple explanation of the physics used to make ElectriPy
[HERE](./PHYSICS.md).
