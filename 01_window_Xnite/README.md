#  Xnite Platformer

This README was made during development of **Xnite** to help organize and track progress.

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

## Set up to code (Step 0)

1. Download and install Python (make sure to check "Add to PATH").
2. Open terminal and run:

   ```bash
   pip install arcade

3. Create this folder structure:

```
Xnite/
├── main.py
├── README.md
├── assets/
└─── window_icon.ico
```


4. Save your main script as main.py in the Xnite/ folder.

5. Put your window icon in the assets/ folder.
## Begin Coding

---

### Step 1 — Create a basic window

```python
# Import arcade
import arcade

# Create the window
window = arcade.Window(1280, 720, "Xnite")

# Run the game loop
arcade.run()
```

---

### Step 2 — Use constants for readability

```python
import arcade

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Xnite"

# Create the window
window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

# Run the game loop
arcade.run()
```

---

### Step 3 — Create a Game class

```python
import arcade

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Xnite"

class Game(arcade.Window):
    def __init__(self):
        """Initialize the game window and settings."""
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # arcade's on_draw will barely count as clearing and rewriting the screen at very roughly 60fps
    def on_draw(self):
        """Render the screen."""
        self.clear()

# Run the game only if this file is executed directly
if __name__ == "__main__":
    Game()
    arcade.run()
```

---

### Step 4 — Set background color

```python
import arcade

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Xnite"

class Game(arcade.Window):
    # When Game() launches, run this code first
    def __init__(self):
        # Open game window, set size & title
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        # Sky Blue Background
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def on_draw(self):
        self.clear()

if __name__ == "__main__":
    Game()
    arcade.run()
```

---

### Step 5 — Draw text on screen

```python
import arcade

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Xnite"

class Game(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def on_draw(self):
        self.clear()
        # Draw text of window title on screen
        arcade.draw_text(WINDOW_TITLE, 333, 333, arcade.color.BLACK, 99)

if __name__ == "__main__":
    Game()
    arcade.run()
```

---

### Step 6 — Add update loop (60fps)

```python
import arcade

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Xnite"

class Game(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def on_draw(self):
        self.clear()
        arcade.draw_text(WINDOW_TITLE, 333, 333, arcade.color.BLACK, 99)

    #Better 60fps dynamic slow, probably
    def update(self, delta_time: float):
        pass  # Placeholder

if __name__ == "__main__":
    Game()
    arcade.run()
```

---

### Step 7 — Set a window icon

```python
import arcade
import pyglet

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Xnite"

# Add a variable

WINDOW_ICON_PATH = "assets/window_icon.ico"

class Game(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        arcade.set_background_color(arcade.color.SKY_BLUE)

        #add the icon to the window
        self.set_icon(pyglet.image.load(WINDOW_ICON_PATH))

    def on_draw(self):
        self.clear()
        arcade.draw_text(WINDOW_TITLE, 333, 333, arcade.color.BLACK, 99)

    def update(self, delta_time: float):
        pass

if __name__ == "__main__":
    Game()
    arcade.run()
```

---

### Step 8 — Use `os` to safely load the icon

```python
import arcade
import pyglet

# Import os module
import os

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Xnite"
WINDOW_ICON_PATH = "assets/window_icon.ico"

class Game(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

        # checks if on pc, and tries to use window icon in window, but let's it slide if it doesn't work
        if os.path.exists(WINDOW_ICON_PATH):
            try:
                self.set_icon(pyglet.image.load(WINDOW_ICON_PATH))
            except Exception as e:
                print(f"[Warning] Failed to set icon: {e}")
        else:
            print(f"[Notice] Icon file not found: {WINDOW_ICON_PATH}")

        arcade.set_background_color(arcade.color.SKY_BLUE)

    def on_draw(self):
        self.clear()
        arcade.draw_text(WINDOW_TITLE, 333, 333, arcade.color.BLACK, 99)

    def update(self, delta_time: float):
        pass

if __name__ == "__main__":
    Game()
    arcade.run()
```

---

## ✅ Final Code Snapshot

```python
import arcade
import pyglet
import os

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Xnite"
WINDOW_ICON_PATH = "assets/window_icon.ico"

class Game(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        arcade.set_background_color(arcade.color.SKY_BLUE)

        if os.path.exists(WINDOW_ICON_PATH):
            try:
                self.set_icon(pyglet.image.load(WINDOW_ICON_PATH))
            except Exception as e:
                print(f"[Warning] Failed to set icon: {e}")
        else:
            print(f"[Notice] Icon file not found: {WINDOW_ICON_PATH}")

    def on_draw(self):
        self.clear()
        arcade.draw_text(WINDOW_TITLE, 333, 333, arcade.color.BLACK, 99)

    def update(self, delta_time: float):
        pass

if __name__ == "__main__":
    Game()
    arcade.run()
```
