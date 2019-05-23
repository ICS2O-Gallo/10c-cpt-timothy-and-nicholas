import arcade


WIDTH = 1600
HEIGHT = 960

x_background = WIDTH / 2
scroll_left = True
scroll_right = False

# Loading Textures
# title = arcade.load_texture('title.png', 0, 0, 800, 268)
background = arcade.load_texture('title screen background.jpg', 0, 0, 1600, 1200)
bird = arcade.load_texture('bird.png', 0, 0, 1200, 1200)
bird_pos = [[1200, 700], [1300, 720], [1100, 670]]
bird_shift_y = 0
bird_down = False
bird_up = True


def setup():
    arcade.open_window(WIDTH, HEIGHT, "Plane Game Pre-pree-reee")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


def update(delta_time):
    pass


def on_draw():
    arcade.start_render()

    draw_background()
    birds()

def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def draw_background():
    global x_background
    global scroll_left
    global scroll_right

    arcade.draw_texture_rectangle(x_background, HEIGHT / 2, WIDTH, HEIGHT, background)
    arcade.draw_texture_rectangle(x_background + WIDTH, HEIGHT / 2, WIDTH, HEIGHT, background)
    arcade.draw_texture_rectangle(x_background - WIDTH, HEIGHT / 2, WIDTH, HEIGHT, background)
    if x_background == -1600:
        scroll_right = True
        scroll_left = False
    elif x_background == 3200:
        scroll_left = True
        scroll_right = False
    if scroll_right:
        x_background += 0.5
    elif scroll_left:
        x_background -= 0.5


def birds():
    global bird_pos
    global bird_shift_y
    global bird_down
    global bird_up
    for i in range(3):
        arcade.draw_texture_rectangle(bird_pos[i][0], bird_pos[i][1] + bird_shift_y, 100, 100, bird)
    if bird_shift_y == 20:
        bird_down = True
        bird_up = False
    elif bird_shift_y == -20:
        bird_down = False
        bird_up = True
    if bird_up:
        bird_shift_y += 0.5
    if bird_down:
        bird_shift_y -= 0.5

if __name__ == '__main__':
    setup()
