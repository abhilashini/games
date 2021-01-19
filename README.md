![License](https://img.shields.io/static/v1?label=license&message=GPLv3&color=9cf)
![Python](https://img.shields.io/static/v1?label=python&message=v3.6.12&color=9cf)
![Tkinter](https://img.shields.io/static/v1?label=tkinter&message=Python3.6-tk&color=9cf)
![Platform](https://img.shields.io/static/v1?label=platform&message=linux-64|osx-64&color=9cf)
[![Maintainer](https://img.shields.io/static/v1?label=maintainer&message=abhilashini&color=9cf)](https://github.com/abhilashini)
# Games
#### _Collection of games written in Python_

* Snake Game
* Pong
* Turtle Crossing
* Identify the States<br/>
Run _main.py_ in respective folders to launch the game<br/>

**Games that can be directly run on console:**
* rock_paper_scissors.py
* rock_paper_scissors_lizard_spock.py


# How To Play

##### _Download respective files or folders to run locally_

#### Snake Game
1. Grab food without colliding with walls or self
2. Keyboard controls:<br/>
    * <kbd>↑</kbd>, <kbd>→</kbd>, <kbd>↓</kbd> and <kbd>←</kbd> arrow keys to move in the respective position

#### Pong
1. Hit ball with paddle
  2. Keyboard controls:
      * Left Player
         * <kbd>w</kbd>  key - paddle moves upwards
         * <kbd>s</kbd>  key - paddle moves downwards
      * Right Player
         * <kbd>↑</kbd> arrow key - paddle moves upwards
         * <kbd>↓</kbd> arrow key - paddle moves downwards
3. Ball bounces off top and bottom edges of screen

#### Turtle Crossing
1. Turtle can only move upwards (<kbd>↑</kbd> arrow key) 
2. Speed of cars increases with each level

#### Identify the States
1. Run _find_states_in.py_ or _find_states_usa.py_ to launch game for respective countries
2. Game shows an input dialog and identified states so far in dialog's title
    * USA map has 50 States to be identified 
    * India map has 36 places (28 States + 8 Union Territories) to be identifed
      * Places with and in them should be spelled with "and" or "And" (& is not identified)
      * Note: Full and current names have to be provided to identify the places
        - E.g., Odisha, Puducherry
2. If Cancel is selected in input dialog before entering all states, game exits
