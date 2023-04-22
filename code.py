print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP2,board.GP3,board.GP4,board.GP5)
keyboard.row_pins = (board.GP7,board.GP6)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Media key support
media_keys = MediaKeys()
keyboard.extensions.append(media_keys)

# Layer support
layers_ext = Layers()
keyboard.modules.append(layers_ext)

# Shortcuts
#Locks Windows
WINLOCK = KC.LGUI(KC.L)
#Mutes microphone in Windows using PowerToys
MICMUTE = KC.LGUI(KC.LSHIFT(KC.A))
#Launches the task viewer in Windows
TASKVIEW = KC.LGUI(KC.TAB)
#SLEEPWIN = (KC.LGUI,KC.X)(KC.A,KC.U)

# Layer Keys
MOMENTARY = KC.MO(1)
MAINL = KC.DF(0)

#[1][2][3][4 Rotary]
#[5][6][7][8]
#F20 is mapped to AHK sleep Windows script

keyboard.keymap = [
    [#Layer 0
    WINLOCK,KC.PSCREEN,KC.F20,KC.AUDIO_MUTE,
     MICMUTE,KC.MEDIA_PLAY_PAUSE,TASKVIEW,MOMENTARY],
     [#Layer 1
    KC.F19,KC.F18,KC.F17,KC.F16,
      KC.PSCREEN,KC.E,KC.F,KC.TRANS,]
]

encoder_handler = EncoderHandler()
encoder_handler.divisor = 2
encoder_handler.pins = ((board.GP1, board.GP0, None),)
encoder_handler.map = (((KC.VOLD, KC.VOLU,),),)
keyboard.modules.append(encoder_handler)

if __name__ == '__main__':
    keyboard.go()
