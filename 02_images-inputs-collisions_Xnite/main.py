import arcade
import pyglet
import os

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
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
                print(f"[WARNING] Failed to set the icon on screen: {e}")
        else:
            print(f"[Notice] Icon file not found: {WINDOW_ICON_PATH}]")

    def update(self, delta_time: float) -> None:
        pass

    def on_draw(self):
        self.clear()
        arcade.draw_text(WINDOW_TITLE, 333, 333, arcade.color.BLACK, 99)

if __name__ == "__main__":
    Game()
    arcade.run()
