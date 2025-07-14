###  Xnite Platformer 02 Drawing, Input, Movement, and Collisions

In this phase of **Xnite**’s development, we bring the world to life. 
This is where **Xnite** starts feeling like a real game.
This part lays the foundation for everything interactive: images, movement, input, and collisions.

## Add clouds to assets folder  -1)

 -   Put the clouds folder in the assets folder and the cloud images in the clouds folder, label the one cloud cloud_1.png

##  Start with code so far 0)

```python
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
```

## add cloud as sprite 1)


```python
import arcade
import pyglet
import os

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Xnite"
WINDOW_ICON_PATH = "assets/window_icon.ico"

# cloud path
CLOUD_IMAGE_PATH = "assets/clouds/cloud_1.png"

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

            # load cloud
        self.clouds = arcade.SpriteList()
        cloud_sprite = arcade.Sprite(CLOUD_IMAGE_PATH)
        cloud_sprite.center_x = 333
        cloud_sprite.center_y = 500
        self.clouds.append(cloud_sprite)
        self.cloud_texture = arcade.load_texture(CLOUD_IMAGE_PATH)
        self.cloud_sprite = arcade.Sprite(self.cloud_texture)

    def update(self, delta_time: float) -> None:
        pass

    def on_draw(self):
        self.clear()
        arcade.draw_text(WINDOW_TITLE, 333, 333, arcade.color.BLACK, 99)

        # draw cloud
        self.clouds.draw()  

if __name__ == "__main__":
    Game()
    arcade.run()
```

## add rectangle 2) 


```python
import arcade
import pyglet
import os

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Xnite"
WINDOW_ICON_PATH = "assets/window_icon.ico"
CLOUD_IMAGE_PATH = "assets/clouds/cloud_1.png"

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
        self.clouds = arcade.SpriteList()
        cloud_sprite = arcade.Sprite(CLOUD_IMAGE_PATH)
        cloud_sprite.center_x = 333
        cloud_sprite.center_y = 500
        self.clouds.append(cloud_sprite)
        self.cloud_texture = arcade.load_texture(CLOUD_IMAGE_PATH)
        self.cloud_sprite = arcade.Sprite(self.cloud_texture)

    def on_draw(self):
        self.clear()

        # Draw rectangle using correct spelling: LRBT = left, right, bottom, top
        arcade.draw_lrbt_rectangle_filled(300, 650, 300, 450, arcade.color.BLUE)
        
        arcade.draw_text(WINDOW_TITLE, 333, 333, arcade.color.BLACK, 99)
        self.clouds.draw()  

    def update(self, delta_time: float) -> None:
        pass

if __name__ == "__main__":
    Game()
    arcade.run()
```

## add user inputs 3)

```python
import arcade
import pyglet
import os

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Xnite"
WINDOW_ICON_PATH = "assets/window_icon.ico"
CLOUD_IMAGE_PATH = "assets/clouds/cloud_1.png"

# add cloud speed
CLOUD_SPEED = 1

class Game(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        arcade.set_background_color(arcade.color.SKY_BLUE)
        if os.path.exists(WINDOW_ICON_PATH):
            try:
                self.set_icon(pyglet.image.load(WINDOW_ICON_PATH))
            except Exception as e:
                print(f"[WARNING] Failed to set icon: {e}")
        else:
            print(f"[NOTICE] Icon not found: {WINDOW_ICON_PATH}")
        self.clouds = arcade.SpriteList()
        cloud_sprite = arcade.Sprite(CLOUD_IMAGE_PATH)
        cloud_sprite.center_x = 333
        cloud_sprite.center_y = 500
        self.clouds.append(cloud_sprite)

        # Track key states
        self.directions = {
            "left": False,
            "right": False,
            "up": False,
            "down": False
        }

    def on_draw(self):
        self.clear()
        arcade.draw_lrbt_rectangle_filled(300, 650, 300, 450, arcade.color.BLUE)
        arcade.draw_text(WINDOW_TITLE, 333, 333, arcade.color.BLACK, 99)
        self.clouds.draw()

    def on_update(self, delta_time: float):

        # sprites are always in lists of sprites, so the first cloud in the clouds list
        cloud = self.clouds[0]

        # Horizontal movement
        if self.directions["left"] and not self.directions["right"]:
            cloud.center_x -= CLOUD_SPEED
        elif self.directions["right"] and not self.directions["left"]:
            cloud.center_x += CLOUD_SPEED

        # Vertical movement    
        if self.directions["up"] and not self.directions["down"]:
            cloud.center_y += CLOUD_SPEED
        elif self.directions["down"] and not self.directions["up"]:
            cloud.center_y -= CLOUD_SPEED

    # watch for pressing arrows
    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.directions["left"] = True
        elif key == arcade.key.RIGHT:
            self.directions["right"] = True
        elif key == arcade.key.UP:
            self.directions["up"] = True
        elif key == arcade.key.DOWN:
            self.directions["down"] = True

    # watch for unpressing arrows
    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.directions["left"] = False
        elif key == arcade.key.RIGHT:
            self.directions["right"] = False
        elif key == arcade.key.UP:
            self.directions["up"] = False
        elif key == arcade.key.DOWN:
            self.directions["down"] = False

if __name__ == "__main__":
    Game()
    arcade.run()

```


## add collisions and make cloud list just one cloud 4)

```python
import arcade
import pyglet
import os

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Xnite"
WINDOW_ICON_PATH = "assets/window_icon.ico"
CLOUD_IMAGE_PATH = "assets/clouds/cloud_1.png"
CLOUD_SPEED = 1
RECT_LEFT = 300
RECT_RIGHT = 650
RECT_BOTTOM = 300
RECT_TOP = 450

class Game(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        arcade.set_background_color(arcade.color.SKY_BLUE)
        if os.path.exists(WINDOW_ICON_PATH):
            try:
                self.set_icon(pyglet.image.load(WINDOW_ICON_PATH))
            except Exception as e:
                print(f"[WARNING] Failed to set icon: {e}")
        else:
            print(f"[NOTICE] Icon not found: {WINDOW_ICON_PATH}")
        self.clouds = arcade.SpriteList()

        # New SpriteList for rectangle
        self.rect_sprites = arcade.SpriteList()  

        # Cloud Sprite
        cloud_sprite = arcade.Sprite(CLOUD_IMAGE_PATH)
        cloud_sprite.center_x = 333
        cloud_sprite.center_y = 500
        self.clouds.append(cloud_sprite)
        
        # Create rectangle sprite
        self.rect_sprite = arcade.SpriteSolidColor(
            width=RECT_RIGHT - RECT_LEFT,
            height=RECT_TOP - RECT_BOTTOM,
            color=arcade.color.BLUE
        )
        self.rect_sprite.center_x = (RECT_LEFT + RECT_RIGHT) / 2
        self.rect_sprite.center_y = (RECT_BOTTOM + RECT_TOP) / 2
        self.rect_sprites.append(self.rect_sprite)  # Add to SpriteList
        
        self.directions = {
            "left": False,
            "right": False,
            "up": False,
            "down": False
        }

    # Cleaner access to the first cloud sprite
    @property
    def cloud(self):
        return self.clouds[0]

    def on_draw(self):
        self.clear()
        cloud = self.cloud  # [MODIFIED]
        
        # Check for collision between cloud and rectangle sprite
        in_bounds = arcade.check_for_collision(cloud, self.rect_sprite)
        
        # Change colors based on collision
        self.rect_sprite.color = arcade.color.YELLOW if in_bounds else arcade.color.BLUE
        text_color = arcade.color.WHITE if in_bounds else arcade.color.BLACK
        
        # Draw
        self.rect_sprites.draw()  # Draw the SpriteList

        arcade.draw_text(WINDOW_TITLE, 333, 333, text_color, 99)
        self.clouds.draw()


    def on_update(self, delta_time: float):
        cloud = self.cloud  # [MODIFIED]
        if self.directions["left"] and not self.directions["right"]:
            cloud.center_x -= CLOUD_SPEED
        elif self.directions["right"] and not self.directions["left"]:
            cloud.center_x += CLOUD_SPEED
        if self.directions["up"] and not self.directions["down"]:
            cloud.center_y += CLOUD_SPEED
        elif self.directions["down"] and not self.directions["up"]:
            cloud.center_y -= CLOUD_SPEED

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.directions["left"] = True
        elif key == arcade.key.RIGHT:
            self.directions["right"] = True
        elif key == arcade.key.UP:
            self.directions["up"] = True
        elif key == arcade.key.DOWN:
            self.directions["down"] = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.directions["left"] = False
        elif key == arcade.key.RIGHT:
            self.directions["right"] = False
        elif key == arcade.key.UP:
            self.directions["up"] = False
        elif key == arcade.key.DOWN:
            self.directions["down"] = False

if __name__ == "__main__":
    Game()
    arcade.run()

```



### Finished code below
### Finished code below
### Finished code below

### Finished code below
### Finished code below
### Finished code below

### Finished code below
### Finished code below
### Finished code below



```python
import arcade
import pyglet
import os

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Xnite"
WINDOW_ICON_PATH = "assets/window_icon.ico"
CLOUD_IMAGE_PATH = "assets/clouds/cloud_1.png"
CLOUD_SPEED = 1
RECT_LEFT = 300
RECT_RIGHT = 650
RECT_BOTTOM = 300
RECT_TOP = 450

class Game(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        arcade.set_background_color(arcade.color.SKY_BLUE)
        if os.path.exists(WINDOW_ICON_PATH):
            try:
                self.set_icon(pyglet.image.load(WINDOW_ICON_PATH))
            except Exception as e:
                print(f"[WARNING] Failed to set icon: {e}")
        else:
            print(f"[NOTICE] Icon not found: {WINDOW_ICON_PATH}")
        self.clouds = arcade.SpriteList()
        self.rect_sprites = arcade.SpriteList()  
        cloud_sprite = arcade.Sprite(CLOUD_IMAGE_PATH)
        cloud_sprite.center_x = 333
        cloud_sprite.center_y = 500
        self.clouds.append(cloud_sprite)
        self.rect_sprite = arcade.SpriteSolidColor(
            width=RECT_RIGHT - RECT_LEFT,
            height=RECT_TOP - RECT_BOTTOM,
            color=arcade.color.BLUE
        )
        self.rect_sprite.center_x = (RECT_LEFT + RECT_RIGHT) / 2
        self.rect_sprite.center_y = (RECT_BOTTOM + RECT_TOP) / 2
        self.rect_sprites.append(self.rect_sprite)
        self.directions = {
            "left": False,
            "right": False,
            "up": False,
            "down": False
        }

    @property
    def cloud(self):
        return self.clouds[0]

    def on_draw(self):
        self.clear()
        cloud = self.cloud  
        in_bounds = arcade.check_for_collision(cloud, self.rect_sprite)
        self.rect_sprite.color = arcade.color.YELLOW if in_bounds else arcade.color.BLUE
        text_color = arcade.color.WHITE if in_bounds else arcade.color.BLACK
        self.rect_sprites.draw()  
        arcade.draw_text(WINDOW_TITLE, 333, 333, text_color, 99)
        self.clouds.draw()

    def on_update(self, delta_time: float):
        cloud = self.cloud  
        if self.directions["left"] and not self.directions["right"]:
            cloud.center_x -= CLOUD_SPEED
        elif self.directions["right"] and not self.directions["left"]:
            cloud.center_x += CLOUD_SPEED
        if self.directions["up"] and not self.directions["down"]:
            cloud.center_y += CLOUD_SPEED
        elif self.directions["down"] and not self.directions["up"]:
            cloud.center_y -= CLOUD_SPEED

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.directions["left"] = True
        elif key == arcade.key.RIGHT:
            self.directions["right"] = True
        elif key == arcade.key.UP:
            self.directions["up"] = True
        elif key == arcade.key.DOWN:
            self.directions["down"] = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.directions["left"] = False
        elif key == arcade.key.RIGHT:
            self.directions["right"] = False
        elif key == arcade.key.UP:
            self.directions["up"] = False
        elif key == arcade.key.DOWN:
            self.directions["down"] = False

if __name__ == "__main__":
    Game()
    arcade.run()

```
