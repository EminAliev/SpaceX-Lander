""" window configuration """
WINDOW_TITLE = "SpaceX Lander"
GAME_FPS = 60
<<<<<<< HEAD
WIDTH, HEIGHT = 1280, 720
SCREEN_SIZE = (WIDTH, HEIGHT)
=======
FULLSCREEN = True
WIDTH, HEIGHT = 1920, 1080  # set your screen size even if fullscreen
SCREEN_SIZE = (WIDTH, HEIGHT)

""" colors """
>>>>>>> 57763962c216d281139f4edd55c293d3e853df42
GREEN = (120, 240, 120)
YELLOW = (255, 250, 111)
WHITE = (255, 255, 255)
RED = (209, 50, 50)
SPACE = (0, 20, 0)
BLACK = (0, 0, 0)
<<<<<<< HEAD
BLUE = (50, 50, 250)
# ROCKET_IMAGE = "images/test-sprite-24x28.png"
ROCKET_LAUNCHER_IMAGE = "images/launch-vehicle.png"
ROCKET_LAUNCHER_SIZE = (60, 160)
PLATFORM_IMAGE = "images/platform.png"  # 550x150 / 11x3
PLATFORM_SIZE = (132, 36)
=======
BLUE = (0, 52, 88)
GRAY = (167, 169, 172)

""" images """
MENU_BACKGROUND_IMAGE = "images/menu_background.jpg"
ROCKET_LAUNCHER_IMAGE = "images/launch-vehicle.png"
PLATFORM_IMAGE = "images/platform.png"  # 550x150 / 11x3
>>>>>>> 57763962c216d281139f4edd55c293d3e853df42
BACKGROUND_IMAGE_LEVEL_1 = "images/Ocean-View-sm.jpg"
SAD_ELON = "images/sadElonMusk.png"

""" sizes """
ROCKET_LAUNCHER_SIZE = (HEIGHT / 32 * 3, HEIGHT / 4)
PLATFORM_SIZE = (HEIGHT/12/3*11, HEIGHT/12)
ELON_HEIGHT = int(HEIGHT/4)
ELON_SIZE = (int(ELON_HEIGHT * 1.5), ELON_HEIGHT)  # GOD

""" rocket configuration """
ANGLE = 1  # Step of rocket rotating
SPEED = HEIGHT / 10000  # Rocket's booster speed
GRAVITY_VECTOR = (0, SPEED/2)  # Strength of gravity
FONT = "fonts/spaceranger.ttf"
