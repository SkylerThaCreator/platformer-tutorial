import arcade
import pyglet
import os

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Xnite"
WINDOW_ICON_PATH = "assets/window_icon.ico"
PLAYER_IMAGE_PATH = "assets/player.webp"
PLAYER_SPEED = 7
PLAYER_JUMP_SPEED = 20
PLAYER_DROP_SPEED = 1
GRAVITY = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5
Item_sound_path = "assets/sounds/Item.wav"
Jump_sound_path = "assets/sounds/Jump.wav"


class Game(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

        if os.path.exists(WINDOW_ICON_PATH):
            try:
                self.set_icon(pyglet.image.load(WINDOW_ICON_PATH))
            except Exception as e:
                print(f"[WARNING] Failed to set icon: {e}")
        else:
            print(f"[NOTICE] Icon not found: {WINDOW_ICON_PATH}")

        # Core things
        self.scene: arcade.Scene | None = None
        self.player_sprite = None
        self.physics_engine = None

        # SpriteLists we still keep refs to (also live inside scene)
        self.wall_list = None
        self.coin_list = None

        # Input state
        self.directions = None
        self.jump_cooldown = 0
        self.jump_released = True

        # Audio
        self.collect_coin_sound = arcade.load_sound(Item_sound_path)
        self.jump_sound = arcade.load_sound(Jump_sound_path)

        # Score / HUD
        self.score = 0
        self.score_text = arcade.Text(
            f"Score: {self.score}",
            20, 20,
            arcade.color.WHITE,
        )

        # Cameras
        self.camera = arcade.Camera2D()      # world
        self.gui_camera = arcade.Camera2D()  # HUD / black bars

        self.setup()
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def setup(self):
        """Set up / reset the game world."""
        self.jump_cooldown = 0
        self.jump_released = True

        # --- SCENE ---
        self.scene = arcade.Scene()

        # Create named sprite lists (draw order = add order)
        # Walls first, then coins, then player on top
        self.wall_list = self.scene.add_sprite_list("Walls", use_spatial_hash=True)
        self.coin_list = self.scene.add_sprite_list("Coins", use_spatial_hash=True)
        player_list = self.scene.add_sprite_list("Player")

        # Player
        self.player_sprite = arcade.Sprite(PLAYER_IMAGE_PATH)
        self.player_sprite.scale = 1
        self.player_sprite.center_x = 500
        self.player_sprite.center_y = 500
        player_list.append(self.player_sprite)

        # Input directions
        self.directions = {
            "left": False,
            "right": False,
            "up": False,
            "down": False
        }

        # Ground
        for x in range(322, 1022, 64):
            wall = arcade.Sprite(
                ":resources:images/tiles/grassMid.png",
                scale=TILE_SCALING
            )
            wall.center_x = x
            wall.center_y = 224
            self.wall_list.append(wall)

        # Vertical column
        coordinate_list = [
            [768, 224], [768, 160], [768, 96],
            [768, 288], [768, 352], [768, 416], [768, 480]
        ]
        for coordinate in coordinate_list:
            wall = arcade.Sprite(
                ":resources:images/tiles/boxCrate_double.png",
                scale=TILE_SCALING
            )
            wall.position = coordinate
            self.wall_list.append(wall)

        # Coins
        for x in range(128, 1250, 256):
            coin = arcade.Sprite(
                ":resources:images/items/coinGold.png",
                scale=COIN_SCALING
            )
            coin.center_x = x
            coin.center_y = 424
            self.coin_list.append(coin)

        # Physics engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite,
            walls=self.wall_list,
            gravity_constant=GRAVITY
        )

        # Reset score
        self.score = 0
        self.score_text.text = f"Score: {self.score}"

    @property
    def player(self):
        return self.player_sprite

    def on_draw(self):
        self.clear()

        # ---- WORLD CAMERA ----
        self.camera.use()
        # Just draw the whole scene now
        self.scene.draw()

        # ---- GUI CAMERA ----
        self.gui_camera.use()
        bar = (WINDOW_WIDTH - WINDOW_HEIGHT * 4 // 3) // 2

        arcade.draw_lrbt_rectangle_filled(
            0, bar,
            0, WINDOW_HEIGHT,
            arcade.color.BLACK
        )
        arcade.draw_lrbt_rectangle_filled(
            WINDOW_WIDTH - bar, WINDOW_WIDTH,
            0, WINDOW_HEIGHT,
            arcade.color.BLACK
        )

        self.score_text.draw()

    def on_update(self, delta_time: float):
        player = self.player

        # Reset horizontal speed each frame
        self.player_sprite.change_x = 0
        if self.directions["left"] and not self.directions["right"]:
            self.player_sprite.change_x = -PLAYER_SPEED
        elif self.directions["right"] and not self.directions["left"]:
            self.player_sprite.change_x = PLAYER_SPEED

        # Jump cooldown
        if self.jump_cooldown > 0:
            self.jump_cooldown -= delta_time

        grounded = (
            self.physics_engine.can_jump(y_distance=1)
            and self.player_sprite.change_y == 0
        )

        # Arm jump when UP released
        if not self.directions["up"]:
            self.jump_released = True

        # Jump
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

        # Fast drop
        if self.directions["down"] and not self.directions["up"]:
            self.player_sprite.change_y -= PLAYER_DROP_SPEED

        # Physics & collisions
        self.physics_engine.update()

        coin_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.coin_list
        )

        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.collect_coin_sound)
            self.score_text.text = f"Score: {self.score}"

        # Camera follow
        self.camera.position = self.player_sprite.position

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
