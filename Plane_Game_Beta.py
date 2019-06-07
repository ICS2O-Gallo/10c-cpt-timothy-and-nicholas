import arcade
import random

# Global Variables ------------------------------------------------------------
WIDTH = 1600
HEIGHT = 960

bird_pos = [
    [1200, 800],
    [1400, 720],
    [1100, 670]
]
bird_shift_y = 0
bird_up = True
x_background = 800

plane_x = 300
plane_y = HEIGHT / 2
plane_up = True

mouse_x = 0
mouse_y = 0

frame_time = 0

game_over_frametime = 0
game_over_animation = 0

start_click = False
mouse_press = False
mouse_release = False

pressed = False
shop_pressed = False
high_scores_pressed = False
game_main_menu_pressed = False
home_pressed = False
reset_pressed = True
restart_pressed = False
information_pressed = False

score_menu = False
game = False
main_menu = True
dead = False
paused = False
times_paused = 0
information = False
store_menu = False
coin_balance = 99999999999
buy = False
times_bought = 0
cost = 10

# Game Variables --------------------------------------------------------------
star_x_positions = []
star_y_positions = []
coin_x_positions = []
coin_y_positions = []
game_y_plane = HEIGHT / 2
keydown = False
keyup = False
game_frametime = 0
speed = 4
if False:
    plane_speed = 12  # read file | to be added later
else:
    plane_speed = 4

for i in range(10):
    game_x = random.randrange(WIDTH / 2, WIDTH * 2)
    game_y = random.randrange(HEIGHT)
    star_x_positions.append(game_x)
    star_y_positions.append(game_y)

for i in range(5):
    coin_x = random.randrange(WIDTH / 2, WIDTH * 2)
    coin_y = random.randrange(HEIGHT)
    coin_x_positions.append(coin_x)
    coin_y_positions.append(coin_y)

# Loading Textures ------------------------------------------------------------
start = arcade.load_texture('assets/text/start.png', 0, 0, 250, 90)

highscores = arcade.load_texture('assets/sprites/scores.png', 0, 0, 244, 204)

shop = arcade.load_texture('assets/sprites/shop.png', 0, 0, 520, 459)

home = arcade.load_texture('assets/sprites/home.png', 0, 0, 512, 512)

reset = arcade.load_texture('assets/sprites/reset.png', 0, 0, 420, 420)

instructions = arcade.load_texture('assets/text/instructions.png', 0, 0, 702,
                                   262)

pause_background = arcade.Sprite('assets/backgrounds/pause_background.png', 1,
                                 0, 0, WIDTH, HEIGHT, WIDTH / 2,
                                 HEIGHT / 2)

plane = arcade.Sprite('assets/sprites/plane.png', 1, 0, 0, 100, 100, 250,
                      game_y_plane)

pause_text = arcade.Sprite('assets/text/game_paused.tiff', 1, 0, 0, 649, 227,
                           WIDTH / 2, HEIGHT - 200)

gameover = arcade.Sprite('assets/text/gameover.png', 1, 0, 0, 495, 170,
                         WIDTH / 2 + 20, HEIGHT - 160)

plane1 = arcade.Sprite('assets/backgrounds/planecrash1.png', 1, 0, 0, WIDTH,
                       HEIGHT, WIDTH / 2, HEIGHT / 2)

plane2 = arcade.Sprite('assets/backgrounds/planecrash2.png', 1, 0, 0, WIDTH,
                       HEIGHT, WIDTH / 2, HEIGHT / 2)

plane3 = arcade.Sprite('assets/backgrounds/planecrash3.png', 1, 0, 0, WIDTH,
                       HEIGHT, WIDTH / 2, HEIGHT / 2)

plane4 = arcade.Sprite('assets/backgrounds/planecrash4.png', 1, 0, 0, WIDTH,
                       HEIGHT, WIDTH / 2, HEIGHT / 2)

planes = [plane1, plane2, plane3, plane4]

score_title = arcade.Sprite('assets/text/leaderboard.tiff', 1, 0, 0, 590, 190,
                            WIDTH / 2, HEIGHT - 160)

title_plane = arcade.Sprite('assets/sprites/plane.png', 1, 0, 0, 100, 100,
                            plane_x, plane_y)

background = arcade.Sprite('assets/backgrounds/title screen background.jpg', 1,
                           0, 0, 3200, 960, x_background, HEIGHT / 2,
                           HEIGHT / 2)

background2 = arcade.Sprite('assets/backgrounds/title screen background.jpg',
                            1, 0, 0, 3200, 960, x_background + 3200,
                            HEIGHT / 2, HEIGHT / 2)

title_text = arcade.Sprite('assets/text/title.png', 1, 0, 0, 800, 500, 800,
                           500)

bird1 = arcade.Sprite('assets/sprites/bird.png', 1 / 12, 0, 0, 1200, 1200,
                      bird_pos[0][0], bird_pos[0][1] + bird_shift_y)

bird2 = arcade.Sprite('assets/sprites/bird.png', 1 / 12, 0, 0, 1200, 1200,
                      bird_pos[1][0], bird_pos[1][1] + bird_shift_y)

bird3 = arcade.Sprite('assets/sprites/bird.png', 1 / 12, 0, 0, 1200, 1200,
                      bird_pos[2][0], bird_pos[2][1] + bird_shift_y)

info_text = arcade.Sprite('assets/text/information.png', 1, 0, 0, 1418, 985,
                          WIDTH / 2, HEIGHT / 2 + 100)

shop_title = arcade.Sprite('assets/text/shoptitle.tiff', 1, 0, 0, 378, 176,
                           WIDTH / 2, HEIGHT - 125)

coin = arcade.Sprite('assets/sprites/coin.tiff', 50 / 580, 0, 0, 580, 580,
                     WIDTH - 205, HEIGHT - 75)

plane_part = arcade.Sprite('assets/sprites/elevator.png', 0.5, 0, 0, 800, 516,
                           WIDTH / 2, HEIGHT / 2 + 75)
# -----------------------------------------------------------------------------


def setup():
    arcade.open_window(WIDTH, HEIGHT, 'Plane Game')
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
    if main_menu or score_menu or information or store_menu:
        frame_time += 1
    elif game:
        plane_game_logic()


def on_draw():
    arcade.start_render()
    if dead:
        game_over()
    elif main_menu:
        draw_background(0.5)
        title_plane()
        birds()
        draw_button(813, 360, 300, 70, arcade.color.GREEN, start,
                    arcade.color.LIGHT_GREEN, arcade.color.FOREST_GREEN)
        draw_shop_button(1078, 360, 150, 70, arcade.color.DARK_CYAN,
                         shop, arcade.color.LIGHT_BLUE, arcade.color.BLUE_BELL)
        draw_high_scores_button(535, 360, 150, 70, arcade.color.BLACK,
                                highscores, arcade.color.GRAY,
                                arcade.color.LIGHT_GRAY)
        draw_information_button(813, 260, 300, 70,
                                arcade.color.GOLDEN_POPPY, instructions,
                                arcade.color.GOLD, arcade.color.ORANGE_PEEL)
        title_text.draw()
    elif score_menu:
        draw_background(0.5)
        title_plane()
        scores_menu()
        draw_home_button(50, HEIGHT - 50, 50, 50, arcade.color.WHITE, home,
                         arcade.color.LIGHT_GRAY, arcade.color.DARK_BLUE_GRAY)
        draw_reset_button(50, HEIGHT - 125, 50, 50, arcade.color.RED, reset,
                          arcade.color.DARK_RED, arcade.color.PINK)
    elif paused:
        pause_menu()
    elif game:
        plane_game_draw()
    elif information:
        draw_background(0.5)
        title_plane()
        info_menu()
        draw_home_button(50, HEIGHT - 50, 50, 50, arcade.color.WHITE, home,
                         arcade.color.LIGHT_GRAY, arcade.color.DARK_BLUE_GRAY)
    elif store_menu:
        draw_background(0.5)
        title_plane()
        shop_menu()
        draw_home_button(50, HEIGHT - 50, 50, 50, arcade.color.WHITE, home,
                         arcade.color.LIGHT_GRAY, arcade.color.DARK_BLUE_GRAY)


def on_key_press(key, modifiers):
    global keyup, keydown, dead, game, paused, times_paused
    if game:
        if key == arcade.key.DOWN:
            keydown = True
        if key == arcade.key.UP:
            keyup = True
        if key == arcade.key.ESCAPE:
            game = False
            dead = True
            paused = False
            times_paused = 0
        if key == arcade.key.SPACE and not paused and times_paused < 2:
            paused = True
            times_paused += 1
        elif key == arcade.key.SPACE and paused:
            paused = False


def on_key_release(key, modifiers):
    if game:
        global keyup, keydown
        if key == arcade.key.DOWN:
            keydown = False
        if key == arcade.key.UP:
            keyup = False


def on_mouse_press(x, y, button, modifiers):
    global mouse_press
    if button == arcade.MOUSE_BUTTON_LEFT:
        mouse_press = True


def on_mouse_release(x, y, button, modifiers):
    global mouse_press
    if button == arcade.MOUSE_BUTTON_LEFT:
        mouse_press = False


def on_mouse_motion(x, y, dx, dy):
    global mouse_x, mouse_y
    mouse_x = x
    mouse_y = y


def draw_background(scroll_speed):
    global x_background
    background.draw()
    background2.draw()
    x_background -= scroll_speed
    background.center_x -= scroll_speed
    background2.center_x -= scroll_speed
    if x_background == -2400:
        x_background = 800
        background.center_x = 800
        background2.center_x = 4000


def birds():
    global bird_shift_y, bird_up
    bird1.draw()
    bird2.draw()
    bird3.draw()
    if bird_shift_y == 20:
        bird_up = False
    elif bird_shift_y == -20:
        bird_up = True
    if bird_up:
        bird_shift_y += 0.5
    else:
        bird_shift_y -= 0.5
    bird1.center_y = bird_pos[0][1] + bird_shift_y
    bird2.center_y = bird_pos[1][1] + bird_shift_y
    bird3.center_y = bird_pos[2][1] + bird_shift_y


def title_plane():
    global plane_y, plane_up
    plane.draw()
    if frame_time % 60 == 0:
        if random.randint(0, 1) == 1:
            plane_up = False
        else:
            plane_up = True
    if not plane_up and plane_y > 53:
        plane_y -= 2
    elif plane_up and plane_y < HEIGHT - 53:
        plane_y += 2
    if plane_y > HEIGHT - 53:
        plane_up = False
        plane_up = False
    elif plane_y < 53:
        plane_up = True
    plane.center_y = plane_y


def draw_button(x, y, width, height, colour_default, texture, colour_hover,
                colour_press):
    global pressed
    if mouse_x > x - (width / 2) and \
            mouse_x < x + (width / 2) and \
            mouse_y < y + (height / 2) and \
            mouse_y > y - (height / 2) and \
            mouse_press:
        arcade.draw_rectangle_filled(x, y, width, height, colour_press)
        pressed = True
    elif mouse_x > x - (width / 2) and \
            mouse_x < x + (width / 2) and \
            mouse_y < y + (height / 2) and \
            mouse_y > y - (height / 2) and not \
            mouse_press:
        arcade.draw_rectangle_filled(x, y, width, height, colour_hover)
        if pressed:
            game_start()
            pressed = False
    else:
        arcade.draw_rectangle_filled(x, y, width, height, colour_default)
        pressed = False
    arcade.draw_texture_rectangle(x, y, width * 0.9, height, texture)


def draw_shop_button(x, y, width, height, colour_default, texture,
                     colour_hover, colour_press):
    global shop_pressed, main_menu, store_menu
    if mouse_x > x - (width / 2) and \
            mouse_x < x + (width / 2) and \
            mouse_y < y + (height / 2) and \
            mouse_y > y - (height / 2) and \
            mouse_press:
        arcade.draw_rectangle_filled(x, y, width, height, colour_press)
        shop_pressed = True
    elif mouse_x > x - (width / 2) and \
            mouse_x < x + (width / 2) and \
            mouse_y < y + (height / 2) and \
            mouse_y > y - (height / 2) and not \
            mouse_press:
        arcade.draw_rectangle_filled(x, y, width, height, colour_hover)
        if shop_pressed:
            shop_pressed = False
            main_menu = False
            store_menu = True
    else:
        arcade.draw_rectangle_filled(x, y, width, height, colour_default)
        shop_pressed = False
        store_menu = False
    arcade.draw_texture_rectangle(x, y + 5, width, height * 1.15, texture)


def draw_high_scores_button(x, y, width, height, colour_default, texture,
                            colour_hover, colour_press):
    global high_scores_pressed, score_menu, main_menu
    if mouse_x > x - (width / 2) and \
            mouse_x < x + (width / 2) and \
            mouse_y < y + (height / 2) and \
            mouse_y > y - (height / 2) and \
            mouse_press:
        arcade.draw_rectangle_filled(x, y, width, height, colour_press)
        high_scores_pressed = True
    elif mouse_x > x - (width / 2) and \
            mouse_x < x + (width / 2) and \
            mouse_y < y + (height / 2) and \
            mouse_y > y - (height / 2) and not \
            mouse_press:
        arcade.draw_rectangle_filled(x, y, width, height, colour_hover)
        if high_scores_pressed:
            score_menu = True
            main_menu = False
            high_scores_pressed = False
    else:
        arcade.draw_rectangle_filled(x, y, width, height, colour_default)
        high_scores_pressed = False
        score_menu = False
    arcade.draw_texture_rectangle(x, y - 3, width, height * 1.15, texture)


def draw_home_button(x, y, width, height, colour_default, texture,
                     colour_hover, colour_press):
    global home_pressed, main_menu, score_menu, information, store_menu
    if mouse_x > x - (width / 2) and \
            mouse_x < x + (width / 2) and \
            mouse_y < y + (height / 2) and \
            mouse_y > y - (height / 2) and \
            mouse_press:
        arcade.draw_rectangle_filled(x, y, width, height, colour_press)
        home_pressed = True
    elif mouse_x > x - (width / 2) and \
            mouse_x < x + (width / 2) and \
            mouse_y < y + (height / 2) and \
            mouse_y > y - (height / 2) and not \
            mouse_press:
        arcade.draw_rectangle_filled(x, y, width, height, colour_hover)
        if home_pressed:
            home_pressed = False
            main_menu = True
            if score_menu:
                score_menu = False
            elif information:
                information = False
            elif store_menu:
                store_menu = False
    else:
        arcade.draw_rectangle_filled(x, y, width, height, colour_default)
        home_pressed = False
    arcade.draw_texture_rectangle(x, y, width * 0.95, height * 0.95, texture)


def draw_reset_button(x, y, width, height, colour_default, texture,
                      colour_hover, colour_press):
    global reset_pressed
    if mouse_x > x - (width / 2) and \
            mouse_x < x + (width / 2) and \
            mouse_y < y + (height / 2) and \
            mouse_y > y - (height / 2) and \
            mouse_press:
        arcade.draw_rectangle_filled(x, y, width, height, colour_press)
        reset_pressed = True
    elif mouse_x > x - (width / 2) and \
            mouse_x < x + (width / 2) and \
            mouse_y < y + (height / 2) and \
            mouse_y > y - (height / 2) and not \
            mouse_press:
        arcade.draw_rectangle_filled(x, y, width, height, colour_hover)
        if reset_pressed:
            reset_pressed = False
            scores_reset = open('scores.txt', 'w')
            scores_reset.write("")
    else:
        arcade.draw_rectangle_filled(x, y, width, height, colour_default)
        reset_pressed = False
    arcade.draw_texture_rectangle(x, y, width * 0.95, height * 0.95, texture)


def draw_restart_button(x, y, width, height, colour_default, texture,
                        colour_hover, colour_press):
    global restart_pressed, dead, game, game_frametime
    if mouse_x > x - (width / 2) and \
            mouse_x < x + (width / 2) and \
            mouse_y < y + (height / 2) and \
            mouse_y > y - (height / 2) and \
            mouse_press:
        arcade.draw_rectangle_filled(x, y, width, height, colour_press)
        restart_pressed = True
    elif mouse_x > x - (width / 2) and \
            mouse_x < x + (width / 2) and \
            mouse_y < y + (height / 2) and \
            mouse_y > y - (height / 2) and not \
            mouse_press:
        arcade.draw_rectangle_filled(x, y, width, height, colour_hover)
        if restart_pressed:
            restart_pressed = False
            dead = False
            game = True
            game_frametime = 0
    else:
        arcade.draw_rectangle_filled(x, y, width, height, colour_default)
        restart_pressed = False
    arcade.draw_texture_rectangle(x, y, width * 0.95, height * 0.95, texture)


def draw_game_main_menu_button(x, y, width, height, colour_default, texture,
                               colour_hover, colour_press):
    global game_main_menu_pressed, main_menu, dead, game_frametime
    if mouse_x > x - (width / 2) and \
            mouse_x < x + (width / 2) and \
            mouse_y < y + (height / 2) and \
            mouse_y > y - (height / 2) and \
            mouse_press:
        arcade.draw_rectangle_filled(x, y, width, height, colour_press)
        game_main_menu_pressed = True
    elif mouse_x > x - (width / 2) and \
            mouse_x < x + (width / 2) and \
            mouse_y < y + (height / 2) and \
            mouse_y > y - (height / 2) and not \
            mouse_press:
        arcade.draw_rectangle_filled(x, y, width, height, colour_hover)
        if game_main_menu_pressed:
            game_main_menu_pressed = False
            main_menu = True
            dead = False
            game_frametime = 0
    else:
        arcade.draw_rectangle_filled(x, y, width, height, colour_default)
        game_main_menu_pressed = False
    arcade.draw_texture_rectangle(x, y, width * 0.95, height * 0.95, texture)


def draw_information_button(x, y, width, height, colour_default, texture,
                            colour_hover, colour_press):
    global information_pressed, information, main_menu
    if mouse_x > x - (width / 2) and \
            mouse_x < x + (width / 2) and \
            mouse_y < y + (height / 2) and \
            mouse_y > y - (height / 2) and \
            mouse_press:
        arcade.draw_rectangle_filled(x, y, width, height, colour_press)
        information_pressed = True
    elif mouse_x > x - (width / 2) and \
            mouse_x < x + (width / 2) and \
            mouse_y < y + (height / 2) and \
            mouse_y > y - (height / 2) and not \
            mouse_press:
        arcade.draw_rectangle_filled(x, y, width, height, colour_hover)
        if information_pressed:
            information_pressed = False
            information = True
            main_menu = False
    else:
        arcade.draw_rectangle_filled(x, y, width, height, colour_default)
        information_pressed = False
        information = False
    arcade.draw_texture_rectangle(x + 5, y, width * 0.8, height * 0.8, texture)


def plane_game_draw():
    arcade.set_background_color(arcade.color.DARK_MIDNIGHT_BLUE)
    arcade.draw_text(str(game_frametime), WIDTH - 50, HEIGHT - 20,
                     arcade.color.WHITE)
    for x_star, y_star in zip(star_x_positions, star_y_positions):
        arcade.draw_circle_filled(x_star, y_star, 2, arcade.color.WHITE)
    for x_coin, y_coin in zip(coin_x_positions, coin_y_positions):
        draw_coin = arcade.Sprite('assets/sprites/coin.tiff', 25 / 580, 0, 0,
                                  580, 580, x_coin, y_coin)
        draw_coin.draw()
    plane_movement()
    plane.draw()


def plane_game_logic():
    global speed, game_frametime
    if not paused:
        game_frametime += 1
        coin_star_drawing()
        if game_frametime % 120 == 0 and game_frametime != 0:
            speed += 0.35
        plane_collision()


def scores_menu():
    score_title.draw()
    height = 700
    scores_read = open('scores.txt', 'r')
    scores_save = []

    for length in scores_read:
        scores_save.append(int(length.replace(', \n', '')))
    scores_read.close()
    scores_save.sort(reverse=True)
    if 10 > len(scores_save) != 0:
        for i in range(len(scores_save)):
            if i == 0:
                arcade.draw_text(f'[{i + 1}]: {str(scores_save[i])}',
                                 WIDTH / 2, height, arcade.color.GOLD, 24)
            elif i == 1:
                arcade.draw_text(f'[{i + 1}]: {str(scores_save[i])}',
                                 WIDTH / 2, height, arcade.color.SILVER, 24)
            elif i == 2:
                arcade.draw_text(f'[{i + 1}]: {str(scores_save[i])}',
                                 WIDTH / 2, height, arcade.color.BRONZE, 24)
            else:
                arcade.draw_text(f'[{i + 1}]: {str(scores_save[i])}',
                                 WIDTH / 2, height, arcade.color.BLACK, 24)
            height -= 70
    elif len(scores_save) >= 10:
        for i in range(10):
            if i == 0:
                arcade.draw_text(f'[{i + 1}]: {str(scores_save[i])}',
                                 WIDTH / 2, height, arcade.color.GOLD, 24)
            elif i == 1:
                arcade.draw_text(f'[{i + 1}]: {str(scores_save[i])}',
                                 WIDTH / 2, height, arcade.color.SILVER, 24)
            elif i == 2:
                arcade.draw_text(f'[{i + 1}]: {str(scores_save[i])}',
                                 WIDTH / 2, height, arcade.color.BRONZE, 24)
            else:
                arcade.draw_text(f'[{i + 1}]: {str(scores_save[i])}',
                                 WIDTH / 2, height, arcade.color.BLACK, 24)
            height -= 70
    else:
        arcade.draw_text('No game progress is present', WIDTH / 2 - 180,
                         HEIGHT / 2, arcade.color.BLACK, 24)


def coin_star_drawing():
    for x_range in range(len(star_x_positions)):
        star_x_positions[x_range] -= speed
        if star_x_positions[x_range] <= 0:
            star_y_positions[x_range] = random.randrange(0, HEIGHT)
            star_x_positions[x_range] = random.randrange(WIDTH, WIDTH * 2)
    for x_range in range(len(coin_x_positions)):
        coin_x_positions[x_range] -= speed
        if coin_x_positions[x_range] <= 0:
            coin_y_positions[x_range] = random.randrange(0, HEIGHT)
            coin_x_positions[x_range] = random.randrange(WIDTH, WIDTH * 2)
        for star in range(len(star_x_positions)):
            if (star_y_positions[star] + 13 >= coin_y_positions[x_range] >=
                star_y_positions[star] - 13) and (
                    star_x_positions[star] + 13 >= coin_x_positions[x_range] >=
                    star_x_positions[star] - 13):
                coin_y_positions[x_range] = random.randrange(0, HEIGHT)
                coin_x_positions[x_range] = random.randrange(WIDTH, WIDTH * 2)


def plane_movement():
    global game_y_plane
    if game_y_plane >= 50:
        if keydown:
            game_y_plane -= plane_speed
    if game_y_plane <= HEIGHT - 50:
        if keyup:
            game_y_plane += plane_speed
    plane.center_y = game_y_plane


def reset_stats():
    global star_x_positions, star_y_positions, game_y_plane, keydown, keyup,\
        speed, dead
    global game, times_paused
    scores = open('scores.txt', 'a')
    scores.write(f'{str(game_frametime)}, \n')
    scores.close()
    star_x_positions = []
    star_y_positions = []
    game_y_plane = HEIGHT / 2
    keydown = False
    keyup = False
    speed = 4
    for i in range(10):
        game_x = random.randrange(WIDTH / 2, WIDTH * 2)
        game_y = random.randrange(HEIGHT)
        star_x_positions.append(game_x)
        star_y_positions.append(game_y)
    dead = True
    game = False
    times_paused = 0


def plane_collision():
    global coin_balance
    for detect in range(len(coin_x_positions)):
        if ((212 <= coin_x_positions[detect] <= 296) and (
                coin_y_positions[detect] - 62 <= game_y_plane <=
                coin_y_positions[detect] + 62)):
            coin_balance += 1
            print(coin_balance)
            coin_y_positions[detect] = random.randrange(0, HEIGHT)
            coin_x_positions[detect] = random.randrange(WIDTH, WIDTH * 2)
    for detect in range(len(star_x_positions)):
        if ((200 <= star_x_positions[detect] <= 284) and (
                star_y_positions[detect] - 50 <= game_y_plane <=
                star_y_positions[detect] + 50)) or \
                ((300 >= star_x_positions[detect] >= 285) and (
                        star_y_positions[detect] - 22 <= game_y_plane <=
                        star_y_positions[detect] + 22)):
            reset_stats()


def game_start():
    global main_menu, game
    main_menu = False
    game = True
    print('game started')


def game_over_background():
    global game_over_frametime, game_over_animation
    planes[game_over_animation].draw()

    if game_over_frametime % 15 == 0 and game_over_frametime != 0:
        game_over_animation += 1

    if game_over_animation == 4:
        game_over_animation = 0
    game_over_frametime += 1


def game_over():
    game_over_background()
    gameover.draw()
    draw_restart_button(WIDTH / 2, 500, 100, 100, arcade.color.ORANGE, reset,
                        arcade.color.GOLD, arcade.color.YELLOW)
    draw_game_main_menu_button(WIDTH / 2, 350, 100, 100, arcade.color.RED,
                               home, arcade.color.DARK_RED, arcade.color.PINK)
    arcade.draw_rectangle_filled(WIDTH / 2 - 10, HEIGHT - 290, 200, 48,
                                 arcade.color.LIGHT_GRAY)
    arcade.draw_text(f'Score: {game_frametime}', WIDTH / 2 - 75, HEIGHT - 300,
                     arcade.color.BLACK, 24)


def pause_menu():
    pause_text.draw()
    for x_star, y_star in zip(star_x_positions, star_y_positions):
        arcade.draw_circle_filled(x_star, y_star, 2, arcade.color.WHITE)
    for x_coin, y_coin in zip(coin_x_positions, coin_y_positions):
        draw_coin = arcade.Sprite('assets/sprites/coin.tiff', 25 / 580, 0, 0,
                                  580, 580, x_coin, y_coin)
        draw_coin.draw()
    plane.draw()
    arcade.draw_text(str(game_frametime), WIDTH - 50, HEIGHT - 20,
                     arcade.color.WHITE)
    pause_background.draw()


def info_menu():
    info_text.draw()


def shop_menu():
    global cost, upgrade_speed
    cost = 10 * (1.15 ** times_bought)
    upgrade_speed = 1 / (1.1 ** times_bought)

    shop_title.draw()
    arcade.draw_rectangle_filled(WIDTH - 150, HEIGHT - 75, 175, 60,
                                 arcade.color.LIGHT_GRAY)
    coin.draw()
    arcade.draw_text(str(coin_balance), WIDTH - 160, HEIGHT - 88,
                     arcade.color.BLACK, 24, font_name='arial', bold=True)
    birch_colour = [255, 235, 208]
    light_wood_colour = [168, 101, 9]
    wood_pressed_colour = [133, 60, 8]
    wood_colour = [161, 64, 5]
    wood_backdrop_colour = [236, 160, 88]
    arcade.draw_rectangle_filled(WIDTH / 2, HEIGHT / 2, 850, 516, birch_colour)
    arcade.draw_rectangle_filled(WIDTH / 2, HEIGHT / 2 + 75, 600, 300,
                                 wood_backdrop_colour)
    draw_buy_button(WIDTH / 2, 250, 100, 50, light_wood_colour, wood_colour,
                    wood_pressed_colour)
    plane_part.draw()
    arcade.draw_text('Elevator Upgrade', WIDTH / 2 - 100, 365,
                     arcade.color.BLACK, 24)
    arcade.draw_text(f'Cost: {cost:.2f}', WIDTH / 2 - 100, 340,
                     arcade.color.BLACK, 24)
    arcade.draw_text(f'Current Speed: {plane_speed:.2f} + ', WIDTH / 2 - 100,
                     315, arcade.color.BLACK, 24)
    arcade.draw_text(f'{upgrade_speed:.2f}', WIDTH / 2 + 175, 315,
                     arcade.color.GREEN, 24)
    arcade.draw_text('Buy', WIDTH / 2 - 25, 235, arcade.color.BLACK, 28)


def draw_buy_button(x, y, width, height, colour_default,
                     colour_hover, colour_press):
    global buy, plane_speed, times_bought, coin_balance
    if mouse_x > x - (width / 2) and \
            mouse_x < x + (width / 2) and \
            mouse_y < y + (height / 2) and \
            mouse_y > y - (height / 2) and \
            mouse_press:
        arcade.draw_rectangle_filled(x, y, width, height, colour_press)
        buy = True
    elif mouse_x > x - (width / 2) and \
            mouse_x < x + (width / 2) and \
            mouse_y < y + (height / 2) and \
            mouse_y > y - (height / 2) and not \
            mouse_press:
        arcade.draw_rectangle_filled(x, y, width, height, colour_hover)
        if buy:
            buy = False
            if coin_balance > cost:
                plane_speed += upgrade_speed
                times_bought += 1
                coin_balance -= cost
            else:
                print('Can not afford')
    else:
        arcade.draw_rectangle_filled(x, y, width, height, colour_default)
        buy = False


if __name__ == '__main__':
    setup()
