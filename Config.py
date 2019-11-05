""" window configuration """
WINDOW_TITLE = "SpaceX Lander"
GAME_FPS = 60

FULLSCREEN = False
WIDTH, HEIGHT = 1600, 900 # set your screen size even if fullscreen
SCREEN_SIZE = (WIDTH, HEIGHT)

""" colors """

GREEN = (120, 240, 120)
YELLOW = (255, 250, 111)
WHITE = (255, 255, 255)
RED = (209, 50, 50)
SPACE = (0, 20, 0)
BLACK = (0, 0, 0)

BLUE = (50, 50, 250)
# ROCKET_IMAGE = "images/test-sprite-24x28.png"
ROCKET_LAUNCHER_IMAGE = "images/launch-vehicle.png"
ROCKET_LAUNCHER_SIZE = (60, 160)
PLATFORM_IMAGE = "images/platform.png"  # 550x150 / 11x3
PLATFORM_SIZE = (132, 36)

BLUE = (0, 52, 88)
GRAY = (167, 169, 172)

""" images """
MENU_BACKGROUND_IMAGE = "images/menu_background.jpg"
ROCKET_LAUNCHER_IMAGE = "images/launch-vehicle-2.png"
ROCKET_LAUNCHER_GAS_IMAGE = "images/launch-vehicle-gas-1.png"
PLATFORM_IMAGE = "images/platform.png"  # 550x150 / 11x3

BACKGROUND = ["images/background-1.jpg", "images/background-2.jpg", "images/background-3.jpg",
              "images/background-4.jpg"]
SAD_ELON = "images/sadElonMusk.png"
HAPPY_ELON = "images/happyElonMusk.png"

""" sizes """
ROCKET_LAUNCHER_SIZE = (int(HEIGHT / 32 * 3), int(HEIGHT / 4))
ROCKET_LAUNCHER_GAS_SIZE = (int(HEIGHT / 32 * 3), int(HEIGHT / 4.7))
PLATFORM_SIZE = (HEIGHT / 12 / 3 * 11, HEIGHT / 12)
ELON_HEIGHT = int(HEIGHT / 4)
ELON_SIZE = (int(ELON_HEIGHT * 1.5), ELON_HEIGHT)  # GOD
FONT_SIZE = int(HEIGHT / 24)
BIG_FONT_SIZE = int(HEIGHT / 20)

""" rocket configuration """
ANGLE = 0.5  # Step of rocket rotating
SPEED = HEIGHT / 50000  # Rocket's booster speed
GRAVITY_VECTOR = (0, SPEED / 2)  # Strength of gravity
FONT = "fonts/spaceranger.ttf"

""" files """
FILE_SCORE = "score.txt"
