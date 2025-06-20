# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.RGB import RGB
from kmk.modules.encoder import EncoderHandler
# from kmk.modules.layers import Layers


# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# layers = Layers()
# keyboard.modules.append(layers)

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((board.GP26, board.GP27, board.GP7), (board.GP28, board.GP29, board.GP0))


# Define your pins here!
PINS = [board.GP1, board.GP2, board.GP4, board.GP3]


rgb = RGB(pixel_pin=board.GP6, num_pixels=4)
keyboard.extensions.append(rgb)
rgb.set_mode(RGB.MODE.RAINBOW)


# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    KC.Macro(Press(KC.LCMD), Tap(KC.C), Release(KC.LCMD)),
     KC.Macro(Press(KC.LCMD), Tap(KC.V), Release(KC.LCMD)), 
     KC.MACRO("ambassadordoge"),
     KC.MACRO(":skull:")]

encoder_handler.map = [
    (KC.VOLD, KC.VOLU, KC.MUTE), 
    (KC.UP, KC.DOWN, None)]


# Start kmk!
if __name__ == '__main__':
    keyboard.go()