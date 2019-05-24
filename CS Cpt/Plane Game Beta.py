import arcade
import random

WIDTH = 1600
HEIGHT = 960

# Loading Textures
title_text = arcade.load_texture('title.png', 0, 0, 505, 150)
background = arcade.load_texture('title screen background - Copy.jpg', 0, 0, 3194, 1200)
bird = arcade.load_texture('bird.png', 0, 0, 1200, 1200)
plane = arcade.load_texture('plane.png', 0, 0, 420, 420)
start = arcade.load_texture('start.png', 0, 0, 250, 90)

# Global Variables -----------------------------------------------------------------------------------------------------
bird_pos = [
    [1200, 800],
    [1400, 720],
    [1100, 670]
]
bird_shift_y = 0
bird_down = False
bird_up = True
x_background = WIDTH / 2
scroll_left = True
scroll_right = False

plane_x = 300
plane_y = HEIGHT / 2
plane_up = True
plane_down = False

background_repetitions = 1
mouse_x = 0
mouse_y = 0

frame_time = 0

main_menu = True
mouse_press = False
mouse_release = False
pressed = False


def setup():
    arcade.open_window(WIDTH, HEIGHT, "Plane Game Pre-pree-reee")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1 / 60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press
    window.on_mouse_release = on_mouse_release
    window.on_mouse_motion = on_mouse_motion

    arcade.run()


def update(delta_time):
    global frame_time
    if main_menu:
        frame_time += 1


def on_draw():
    arcade.start_render()

    draw_background(0.5)
    title_plane()
    birds()
    title()
    draw_button(800, 360, 300, 70, arcade.color.GREEN, start, arcade.color.LIGHT_GREEN, arcade.color.FOREST_GREEN)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    global mouse_press
    if button == arcade.MOUSE_BUTTON_LEFT:
        mouse_press = True


def on_mouse_release(x, y, button, modifiers):
    global mouse_press
    if button == arcade.MOUSE_BUTTON_LEFT:
        mouse_press = False


def on_mouse_motion(x, y, dx, dy):
    global mouse_x
    global mouse_y
    mouse_x = x
    mouse_y = y


def draw_background(scroll_speed):
    global x_background
    global scroll_left
    global scroll_right

    arcade.draw_texture_rectangle(x_background, HEIGHT / 2, WIDTH, HEIGHT, background)
    arcade.draw_texture_rectangle(x_background + WIDTH, HEIGHT / 2, WIDTH, HEIGHT, background)
    x_background -= scroll_speed
    if x_background == -800:
        x_background = 800


def birds():
    global bird_pos
    global bird_shift_y
    global bird_down
    global bird_up
    for i in range(len(bird_pos)):
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


def title_plane():
    global plane_y
    global plane_up
    global plane_down
    arcade.draw_texture_rectangle(plane_x, plane_y, 100, 100, plane)
    if frame_time % 60 == 0:
        if random.randint(0, 1) == 1:
            plane_down = True
            plane_up = False
        else:
            plane_up = True
            plane_down = False
    if plane_down and plane_y > 53:
        plane_y -= 2
    elif plane_up and plane_y < HEIGHT - 53:
        plane_y += 2
    if plane_y > HEIGHT - 53:
        plane_down = True
        plane_up = False
    elif plane_y < 53:
        plane_down = False
        plane_up = True


def title():
    arcade.draw_texture_rectangle(WIDTH / 2, 500, 800, 268, title_text)


def draw_button(x, y, width, height, colour_default, texture, colour_hover, colour_press):
    global pressed
    if mouse_x > x - (width / 2) and mouse_x < x + (width / 2) and mouse_y < y + (height / 2) and mouse_y > y - (
            height / 2) and mouse_press:
        arcade.draw_rectangle_filled(x, y, width, height, colour_press)
        pressed = True
    elif mouse_x > x - (width / 2) and mouse_x < x + (width / 2) and mouse_y < y + (height / 2) and mouse_y > y - (
            height / 2) and not mouse_press:
        arcade.draw_rectangle_filled(x, y, width, height, colour_hover)
        if pressed:
            game_start()
            pressed = False
    else:
        arcade.draw_rectangle_filled(x, y, width, height, colour_default)
        pressed = False
    arcade.draw_texture_rectangle(x, y, width * 0.9, height, texture)


def game_start():
    global main_menu
    main_menu = False
    print('game started')


if __name__ == '__main__':
    setup()
