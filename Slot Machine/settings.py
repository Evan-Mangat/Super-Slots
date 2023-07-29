# Display settings
DEFAULT_IMAGE_SIZE = (300, 300)
FPS = 120
HEIGHT = 1000
WIDTH = 1600
START_X, START_Y = 0, -300
X_OFFSET, Y_OFFSET = 20, 0

# Images
BG_IMAGE_PATH = 'graphics/0/bg.png'
GRID_IMAGE_PATH = 'graphics/0/gridline.png'
GAME_INDICES = [1, 2, 3] # 0 and 4 are outside of play area
SYM_PATH = 'graphics/0/symbols'

# Text
TEXT_COLOR = 'White'

UI_FONT = 'graphics/font/Pokemon-GB.ttf'
UI_FONT_SIZE = 30
WIN_FONT_SIZE = 110

symbols = {
    'seven': f"{SYM_PATH}/Veilstone_Corner_7.png", 
    'galactic': f"{SYM_PATH}/Veilstone_Corner_Galactic_Symbol.png",
    'bolt': f"{SYM_PATH}/Veilstone_Corner_Lightning_Bolt.png",
    'moon': f"{SYM_PATH}/Veilstone_Corner_Moon_Stone.png",
    'berry': f"{SYM_PATH}/Veilstone_Corner_Berries.png"
}