Xnite – Arcade Platformer Tutorial

This tutorial walks you through building a small 2D platformer in Python using the Arcade library.

You’ll end up with:

A player that can run, jump, and fast-fall

Solid platforms and walls

Collectible coins with sound effects

A score HUD

Letterbox bars on the sides to fake a 4:3 viewport

A clean structure using arcade.Scene, PhysicsEnginePlatformer, and cameras

The final code lives in main.py.

1. Requirements

Python 3.11+ (you’re on 3.13 in this project)

arcade and pyglet:

pip install arcade


(Arcade will pull in pyglet.)

2. Project Structure

Example layout:

nuttocks/
├─ main.py
├─ assets/
│  ├─ window_icon.ico
│  ├─ player1.webp
│  └─ sounds/
│     ├─ Item.wav
│     └─ Jump.wav


The code expects:

assets/window_icon.ico – window icon

assets/player1.webp – player sprite

assets/sounds/Item.wav – coin pickup sound

assets/sounds/Jump.wav – jump sound

Arcade’s built-in tiles and coins are loaded via :resources:..., so you don’t need to download those.

3. Running the Game

From the project folder:

python main.py


Controls:

Left / Right arrows – move

Up arrow – jump (requires touching the ground + cooldown + re-press)

Down arrow – fast drop

ESC – reset the level (rebuilds the scene and resets score)

4. High-Level Architecture

Everything lives in a single class:

class Game(arcade.Window):
    ...


This class is responsible for:

Creating the game window

Setting up sprites and the scene

Running physics

Handling input

Drawing world + HUD

Key building blocks:

arcade.Scene – groups sprite lists by layer name ("Walls", "Coins", "Player").

arcade.PhysicsEnginePlatformer – handles gravity, ground detection, and collisions.

arcade.Camera2D – one camera for the world, one for the HUD/black bars.

5. Step-by-Step: How the Code Is Built
5.1 Window and core constants

At the top of the file, constants define your game’s “rules”:

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Xnite"

PLAYER_SPEED = 7
PLAYER_JUMP_SPEED = 20
PLAYER_DROP_SPEED = 1
GRAVITY = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5


These make it easy to tweak movement and feel without editing logic everywhere.

The Game constructor:

Calls super().__init__ to create the window.

Optionally sets a custom icon.

Loads sounds (Item.wav, Jump.wav).

Creates text for the score HUD.

Creates two cameras:

self.camera – world camera that follows the player.

self.gui_camera – GUI camera that stays fixed.

Calls self.setup() to build the level.

5.2 The setup() function – building the level

setup() is called:

Once at startup

Again every time you press ESC (to reset the game)

It:

Resets jump state and score display.

Creates a new arcade.Scene:

self.scene = arcade.Scene()


Adds sprite lists to the scene:

self.wall_list = self.scene.add_sprite_list("Walls", use_spatial_hash=True)
self.coin_list = self.scene.add_sprite_list("Coins", use_spatial_hash=True)
player_list = self.scene.add_sprite_list("Player")


Creates the player sprite and adds it to the "Player" list:

self.player_sprite = arcade.Sprite(PLAYER_IMAGE_PATH)
self.player_sprite.center_x = 500
self.player_sprite.center_y = 500
player_list.append(self.player_sprite)


Sets up an input state dict:

self.directions = {"left": False, "right": False, "up": False, "down": False}


Builds the level:

A flat line of ground tiles (grassMid).

A vertical column of crates (boxCrate_double) to act as a wall.

A line of gold coins above.

Creates PhysicsEnginePlatformer:

self.physics_engine = arcade.PhysicsEnginePlatformer(
    self.player_sprite,
    walls=self.wall_list,
    gravity_constant=GRAVITY
)


Resets score and updates the score text:

self.score = 0
self.score_text.text = f"Score: {self.score}"

5.3 Drawing: world vs HUD

on_draw runs every frame.

self.clear() wipes the screen.

World camera is activated:

self.camera.use()
self.scene.draw()


This draws walls, coins, and player in the world.

GUI camera is activated:

self.gui_camera.use()


Now drawing is in screen space, unaffected by camera movement.

Two black rectangles are drawn on the left and right to simulate a 4:3 view inside 16:9:

bar = (WINDOW_WIDTH - WINDOW_HEIGHT * 4 // 3) // 2
arcade.draw_lrbt_rectangle_filled(0, bar, 0, WINDOW_HEIGHT, arcade.color.BLACK)
arcade.draw_lrbt_rectangle_filled(WINDOW_WIDTH - bar, WINDOW_WIDTH, 0, WINDOW_HEIGHT, arcade.color.BLACK)


The score text is drawn on top:

self.score_text.draw()

5.4 Movement, jumping, and physics

on_update(delta_time) handles logic.

Movement:

Every frame, horizontal velocity is reset and then set based on input:

self.player_sprite.change_x = 0
if self.directions["left"] and not self.directions["right"]:
    self.player_sprite.change_x = -PLAYER_SPEED
elif self.directions["right"] and not self.directions["left"]:
    self.player_sprite.change_x = PLAYER_SPEED


Jump cooldown + re-press logic:

jump_cooldown counts down with delta_time.

grounded uses the physics engine’s can_jump and checks vertical speed.

if self.jump_cooldown > 0:
    self.jump_cooldown -= delta_time

grounded = (
    self.physics_engine.can_jump(y_distance=1)
    and self.player_sprite.change_y == 0
)


To prevent holding jump to spam jumps:

When UP is not held, jump_released = True.

A jump only happens if:

UP is pressed

Player is grounded

Cooldown expired

Jump was previously released

if not self.directions["up"]:
    self.jump_released = True

if (
    self.directions["up"]
    and grounded
    and self.jump_cooldown <= 0
    and self.jump_released
):
    self.player_sprite.change_y = PLAYER_JUMP_SPEED
    self.jump_cooldown = 0.75
    self.jump_released = False
    arcade.play_sound(self.jump_sound)


Fast drop:

Holding DOWN (without UP) accelerates downward motion:

if self.directions["down"] and not self.directions["up"]:
    self.player_sprite.change_y -= PLAYER_DROP_SPEED


Physics and collisions:

self.physics_engine.update()


Then coins are checked:

coin_hit_list = arcade.check_for_collision_with_list(
    self.player_sprite, self.coin_list
)

for coin in coin_hit_list:
    coin.remove_from_sprite_lists()
    self.score += 1
    arcade.play_sound(self.collect_coin_sound)
    self.score_text.text = f"Score: {self.score}"


Finally, the camera is moved to the player:

self.camera.position = self.player_sprite.position

5.5 Input handling

Instead of moving the player directly inside on_key_press, the code sets flags in self.directions.

def on_key_press(self, key, modifiers):
    if key == arcade.key.LEFT:
        self.directions["left"] = True
    elif key == arcade.key.RIGHT:
        self.directions["right"] = True
    elif key == arcade.key.UP:
        self.directions["up"] = True
    elif key == arcade.key.DOWN:
        self.directions["down"] = True
    elif key == arcade.key.ESCAPE:
        self.setup()
        return


on_key_release clears those flags. This keeps the actual movement logic centralized in on_update, frame by frame.