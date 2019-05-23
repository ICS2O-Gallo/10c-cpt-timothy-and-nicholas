import arcade


WIDTH = 1600
HEIGHT = 960

# Loading Textures
# title = arcade.load_texture('title.png', 0, 0, 800, 268)
background = arcade.load_texture('title screen background.jpg', 0, 0, 1600, 1200)
x_background = WIDTH / 2
scroll_left = True
scroll_right = False

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



if __name__ == '__main__':
    setup()
