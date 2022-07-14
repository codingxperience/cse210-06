# Alien Attack
---
Alien Attack is a fixed shooter game in which the player moves a laser cannon horizontally across the bottom of the screen and fires at aliens overhead. The goal is to eliminate all of the aliens by shooting them.The game ends immediately if the aliens reach the bottom of the screen.The aliens attempt to destroy the player's cannon by firing projectiles. As aliens are defeated, their movement and the game's music both speed up. Defeating all the aliens brings another wave which starts lower, a loop which can continue endlessly. The Alien Attack is played according to the following rules. Player can move left and right using the KEY_LEFT(back arrow) and KEY_RIGHT(forward arrow) and also using the KEY_SPACE to fire at aliens.
```
## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 alien-attack
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.
```
## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- alien-attack        (source code for game)
  +-- game              (specific game classes)
    +-- assets          (game assets) 
    +-- casting         (various actor classes)
    +-- directing       (director and scene manager classes)
    +-- scripting       (various action classes)
    +-- services        (various service classes)
    +-- shared          (game classes with methods)
  +-- __main__.py       (entry point for program)
  +-- constants.py      (game constants)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
* Fred Okorio - oko22002@byui.edu
* Mmusi Hubona - hub22001@byui.edu
* Vaughn Pinnock (mailto:vpinnock@byui.edu)