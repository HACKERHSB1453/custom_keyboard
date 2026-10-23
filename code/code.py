import board
import busio
import keypad
import time
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation, Scanner
from kmk.scanners.keypad import MatrixScanner
from kmk.modules.encoder import EncoderHandler
from kmk.modules.macros import Macros, Tap
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306

def pin(name):
    if name[0] == 'A':
        return int(name[1])
    return int(name[1]) + 8


class MCPScanner(Scanner):

    def __init__(self, i2c, address, rows, cols, encoders=[]):
        self.i2c = i2c
        self.address = address
        self.rows = rows
        self.cols = cols
        self.encoders = encoders
        self.pressed = [[False] * cols for r in range(rows)]
        self.last_a = [1] * len(encoders)
        self.button = [False] * len(encoders)
        self.connected = False
        self.events = []
        self.next_scan = 0
        self.buffer = bytearray(2)

    @property
    def key_count(self):
        return self.rows * self.cols + 3 * len(self.encoders)

    def scan_for_changes(self):
        if not self.events and time.monotonic_ns() > self.next_scan:
            self.next_scan = time.monotonic_ns() + 10000000
            if self.i2c.try_lock():
                try:
                    if not self.connected:
                        self.connect()
                    self.scan()
                except OSError:
                    self.unplugged()
                self.i2c.unlock()

        if self.events:
            return self.events.pop(0)
        return None

    def write(self, register, a, b):
        self.i2c.writeto(self.address, bytes([register, a, b]))

    def read(self):
        self.i2c.writeto_then_readfrom(self.address, bytes([0x12]), self.buffer)
        return self.buffer[0] + self.buffer[1] * 256

    def connect(self):
        self.write(0x00, 255, 255)
        self.write(0x0C, 255, 255)
        self.write(0x14, 0, 0)
        self.connected = True

    def scan(self):
        for r in range(self.rows):
            self.i2c.writeto(self.address, bytes([0x01, 255 - (1 << r)]))
            pins = self.read()

            for c in range(self.cols):
                is_pressed = (pins >> c) & 1 == 0
                if is_pressed != self.pressed[r][c]:
                    self.pressed[r][c] = is_pressed
                    self.send(r * self.cols + c, is_pressed)

        key = self.rows * self.cols
        for e in range(len(self.encoders)):
            a, b, button = self.encoders[e]

            a_now = (pins >> pin(a)) & 1
            if a_now == 0 and self.last_a[e] == 1:
                if (pins >> pin(b)) & 1 == 1:
                    self.tap(key + 1)
                else:
                    self.tap(key)
            self.last_a[e] = a_now

            button_now = (pins >> pin(button)) & 1 == 0
            if button_now != self.button[e]:
                self.button[e] = button_now
                self.send(key + 2, button_now)

            key += 3

    def send(self, key, is_pressed):
        self.events.append(keypad.Event(self.offset + key, is_pressed))

    def tap(self, key):
        self.send(key, True)
        self.send(key, False)

    def unplugged(self):
        self.connected = False
        for r in range(self.rows):
            for c in range(self.cols):
                if self.pressed[r][c]:
                    self.pressed[r][c] = False
                    self.send(r * self.cols + c, False)


i2c = busio.I2C(board.GP1, board.GP0, frequency=400000)

keyboard = KMKKeyboard()
keyboard.matrix = [
    MatrixScanner(
        row_pins=(board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7),
        column_pins=(board.GP8, board.GP9, board.GP10, board.GP11, board.GP12),
        columns_to_anodes=DiodeOrientation.COL2ROW,
    ),
    MCPScanner(i2c, 0x21, rows=6, cols=5, encoders=[('B6', 'B7', 'A5')]),
    MCPScanner(i2c, 0x23, rows=5, cols=5),
    MCPScanner(i2c, 0x24, rows=4, cols=4),
    MCPScanner(i2c, 0x26, rows=4, cols=4, encoders=[('B5', 'B6', 'B4'), ('A4', 'A5', 'A6')]),
]

keyboard.modules.append(Macros())
keyboard.extensions.append(MediaKeys())

encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.GP14, board.GP13, board.GP15, False),)
encoder_handler.map = [((KC.VOLD, KC.VOLU, KC.MUTE),)]
keyboard.modules.append(encoder_handler)

keyboard.extensions.append(Display(
    display=SSD1306(i2c=i2c, device_address=0x3C),
    entries=[
        TextEntry(text='my-kkeb', x=64, y=4, x_anchor='M'),
        TextEntry(text='113 keys', x=64, y=18, x_anchor='M'),
    ],
    width=128,
    height=32,
))


def git(command):
    return KC.MACRO(command, Tap(KC.ENTER))


def git_start(command):
    return KC.MACRO(command)


keyboard.coord_mapping = [
    104, 105, 106, 107,
    108, 109, 110, 111,
    112, 113, 114, 115,
    116, 117, 118, 119,
    120, 121, 122,
    123, 124, 125,

     88,  89,  90,  91,
     92,  93,  94,  95,
     96,  97,  98,  99,
    100, 101, 102, 103,

      4,   9,  14,  19,  24,  29,  20,
      3,   8,  13,  18,  23,  28,  15,
      2,   7,  12,  17,  22,  27,
      1,   6,  11,  16,  21,  26,
                0,   5,  10,

     30,  59,  54,  49,  44,  39,  34,
     35,  58,  53,  48,  43,  38,  33,
          57,  52,  47,  42,  37,  32,
          31,  36,  41,  46,  51,  56,
     50,  45,  40,
     60,  61,  62,

     63,  64,  65,  66,
     68,  69,  70,  71,
     73,  74,  75,  76,
     78,  79,  80,  81,
     86,  87,  85,
          82,
     72,  77,  67,
]

keyboard.keymap = [
    [
        git('git status'),        git('git add .'),         KC.MACRO('git commit -m ""', Tap(KC.LEFT)), git('git push'),
        git('git pull'),          git('git fetch'),         git('git diff'),                           git('git log --oneline'),
        git('git branch'),        git_start('git switch '), git_start('git switch -c '),               git('git stash'),
        git('git stash pop'),     git_start('git merge '),  git('git log --graph --oneline --all'),    git_start('git clone '),
        KC.PGUP, KC.PGDN, KC.HOME,
        KC.BRID, KC.BRIU, KC.NO,

        KC.F1,   KC.F2,  KC.F3,   KC.F4,
        KC.F5,   KC.F6,  KC.F7,   KC.F8,
        KC.F9,   KC.F10, KC.F11,  KC.F12,
        KC.PSCR, KC.INS, KC.HOME, KC.END,

        KC.ESC,  KC.N1, KC.N2, KC.N3, KC.N4, KC.N5,  KC.GRV,
        KC.TAB,  KC.Q,  KC.W,  KC.E,  KC.R,  KC.T,   KC.LBRC,
        KC.CAPS, KC.A,  KC.S,  KC.D,  KC.F,  KC.G,
        KC.LSFT, KC.Z,  KC.X,  KC.C,  KC.V,  KC.B,
                        KC.LCTL, KC.LGUI, KC.SPC,

        KC.EQL,  KC.N6, KC.N7, KC.N8,   KC.N9,  KC.N0,   KC.MINS,
        KC.RBRC, KC.Y,  KC.U,  KC.I,    KC.O,   KC.P,    KC.BSLS,
                 KC.H,  KC.J,  KC.K,    KC.L,   KC.SCLN, KC.QUOT,
                 KC.N,  KC.M,  KC.COMM, KC.DOT, KC.SLSH, KC.RSFT,
        KC.ENT,  KC.BSPC, KC.LALT,
        KC.MPRV, KC.MNXT, KC.MPLY,

        KC.NLCK, KC.PSLS, KC.PAST, KC.PMNS,
        KC.P7,   KC.P8,   KC.P9,   KC.PPLS,
        KC.P4,   KC.P5,   KC.P6,   KC.BSPC,
        KC.P1,   KC.P2,   KC.P3,   KC.DEL,
        KC.P0,   KC.PDOT, KC.PENT,
                 KC.UP,
        KC.LEFT, KC.DOWN, KC.RIGHT,
    ]
]

if __name__ == '__main__':
    keyboard.go()
