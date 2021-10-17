# ElectriPy :zap:

<p align="center">
  <img width="400" height="400" src="../media/electripy-demo.gif?raw=true">
</p>

Visualize the electric field of a point charges network.

## :electric_plug: Installation

Install ElectriPy package:

```
$ pip install electripy
```

You are all done! To start the simulation type:

```
$ python -m electripy
```

_NOTE:_ you need to have **Python** and **pip** installed.

## :electric_plug: Controls

- Right click to add an electron
- Left click to add a proton
- Press <kbd>r</kbd> to remove all charges from screen
- Press <kbd>+</kbd> to increment vector scale
- Press <kbd>-</kbd> to decrement vector scale
- Press <kbd>space</kbd> to display or hide force array components
- Press <kbd>m</kbd> to change mode

## :electric_plug: Modes
### Electric Field:
This mode let you display an electric field vector at mouse position.
You can also show or hide its components and modify the scale. 
This mode does not hide charges' force vector.

### Electric Force:
This is the default mode when you start running ElectriPy. This mode
let you modify the scale of all charges' electric force vector and
display or hide their components.
When this mode is activated the electric field vector is hiden.

_NOTE:_ controls are the same for both modes. <kbd>+</kbd>, <kbd>-</kbd>
and <kbd>space</kbd> keys will scale either electric field vector or
electric force vectors depending on the current mode.

