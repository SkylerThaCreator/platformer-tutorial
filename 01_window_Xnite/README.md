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
import arcade

window = arcade.Window(1280, 720, "Xnite")
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

window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
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

    def on_draw(self):
        """Render the screen."""
        self.clear()

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
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
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
WINDOW_ICON_PATH = "assets/window_icon.ico"

class Game(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        arcade.set_background_color(arcade.color.SKY_BLUE)
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
