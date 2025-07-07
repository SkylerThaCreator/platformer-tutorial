###  Xnite Platformer

This README was made during development of Xnite to help organize and track progress on dev of **Xnite**.

**Xnite** is a full-featured 2D platformer where you play as a knight who can run, jump, dash, double jump, and wall jump through a zombie-infested island. Your goal? Rescue the princess, or something.

Built in Python using the [Arcade](https://api.arcade.academy) library.

---

## Current Features (Step -2)

- Game window initialized with:
  - Custom title (`"Xnite"`)
  - 1280×720 resolution
  - Sky-blue background
  - Custom icon (Windows only, optional)

---

## Requirements (Step -1)

- Python 3.13+
- Arcade 3.3.0+

---

## Begin Coding (Step 0)

### Initial Setup

1. Download and install Python (make sure to check "Add to PATH").
2. Open terminal and run:

   ```bash
   pip install arcade

3. Create this folder structure:
Xnite/
├── main.py
├── README.md
├── assets/
└──── window_icon.ico

4. Save your main script as main.py in the Xnite/ folder.

5. Put your window icon in the assets/ folder.

1) Create the window, it takes 3 lines of code for displaying blank window in arcade

# Import arcade module into python interpreter
import arcade

# Create the window
window = arcade.Window(1280, 720, "XNite)

# Run the game loop
arcade.run()

2) Cleaned up with constant variables and names

import arcade

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Xnite"

window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

# Run the game loop
arcade.run()

3) Added and called Game() class and ran Game(arcade.Window) loop

import arcade

# constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Xnite"

class Game(arcade.Window):
    def __init__(self):
        """Initialize the game window and settings."""
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    def on_draw(self):
        """Render the screen."""
        self.clear()

if __name__ == "__main__":
    Game()
    arcade.run()

4) set background to sky blue

import arcade

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Xnite"

class Game(arcade.Window):
    def __init__(self):
        """Initialize the game window and settings."""
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def on_draw(self):
        """Render the screen."""
        self.clear()

# Run the game loop
if __name__ == "__main__":
    arcade.run()

5) put text on the screen

import arcade

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Xnite"

class Game(arcade.Window):
    def __init__(self):
        """Initialize the game window and settings."""
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def on_draw(self):
        """Render the screen."""
        self.clear()
        arcade.draw_text(WINDOW_TITLE, 333, 333, arcade.color.BLACK, 99)


# Run the game loop
if __name__ == "__main__":
    arcade.run()

6) calls update() to pass for ez 60fps cap

import arcade

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Xnite"

class Game(arcade.Window):
    def __init__(self):
        """Initialize the game window and settings."""
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def on_draw(self):
        """Render the screen."""
        self.clear()
        arcade.draw_text(WINDOW_TITLE, 333, 333, arcade.color.BLACK, 99)

    def update(self, delta_time: float) -> None:
        """Update game logic. Called ~60 times per second."""
        pass    

# Run the game loop
if __name__ == "__main__":
    arcade.run()

7) add window icon path and set the window icon

import arcade
import pyglet

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Xnite"
WINDOW_ICON_PATH = "assets/window_icon.ico"

class Game(arcade.Window):
    def __init__(self):
        """Initialize the game window and settings."""
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.set_icon(pyglet.image.load(WINDOW_ICON_PATH))

    def on_draw(self):
        """Render the screen."""
        self.clear()
        arcade.draw_text(WINDOW_TITLE, 333, 333, arcade.color.BLACK, 99)

    def update(self, delta_time: float) -> None:
        """Update game logic. Called ~60 times per second."""
        pass    

# Run the game loop
if __name__ == "__main__":
    Game()
    arcade.run()

8) import and use os and try the icon and give up to default and tell why if it doesnt work

import arcade
import pyglet
import os

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Xnite"
WINDOW_ICON_PATH = "assets/window_icon.ico"

class Game(arcade.Window):
    """Main game window for Xnite."""

    def __init__(self):
        """Initialize the game window and settings."""
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # Attempt to load and set a custom window icon (non-critical)
        if os.path.exists(WINDOW_ICON_PATH):
            try:
                self.set_icon(pyglet.image.load(WINDOW_ICON_PATH))
            except Exception as e:
                print(f"[Warning] Failed to set icon: {e}")
        else:
            print(f"[Notice] Icon file not found: {WINDOW_ICON_PATH}")

    def on_draw(self):
        """Render the screen."""
        self.clear()
        ### text, x, y, arcade font color, font size
        arcade.draw_text(WINDOW_TITLE, 333, 333, arcade.color.BLACK, 99)

    def update(self, delta_time: float) -> None:
        """Update game logic. Called ~60 times per second."""
        pass


if __name__ == "__main__":
    Game()
    arcade.run()


### Finished code below
### Finished code below
### Finished code below

### Finished code below
### Finished code below
### Finished code below

import arcade
import pyglet
import os

####### Window configuration constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Xnite"
WINDOW_ICON_PATH = "assets/window_icon.ico"

class Game(arcade.Window):
    """Main game window for Xnite."""

    def __init__(self):
        """Initialize the game window and settings."""
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # Attempt to load and set a custom window icon (non-critical)
        if os.path.exists(WINDOW_ICON_PATH):
            try:
                self.set_icon(pyglet.image.load(WINDOW_ICON_PATH))
            except Exception as e:
                print(f"[Warning] Failed to set icon: {e}")
        else:
            print(f"[Notice] Icon file not found: {WINDOW_ICON_PATH}")

    def on_draw(self):
        """Render the screen."""
        self.clear()
        ### text, x, y, arcade font color, font size
        arcade.draw_text(WINDOW_TITLE, 333, 333, arcade.color.BLACK, 99)

    def update(self, delta_time: float) -> None:
        """Update game logic. Called ~60 times per second."""
        pass


if __name__ == "__main__":
    Game()
    arcade.run()

