import keyboard
from error import FuckYouError

name_to_code = {
    "esc": 1,
    "1": 2,
    "2": 3,
    "3": 4,
    "4": 5,
    "5": 6,
    "6": 7,
    "7": 8,
    "8": 9,
    "9": 10,
    "0": 11,
    "-": 12,
    "=": 13,
    "backspace": 14,
    "tab": 15,
    "q": 16,
    "w": 17,
    "e": 18,
    "r": 19,
    "t": 20,
    "y": 21,
    "u": 22,
    "i": 23,
    "o": 24,
    "p": 25,
    "[": 26,
    "]": 27,
    "enter": 28,
    "ctrl": 29,
    "a": 30,
    "s": 31,
    "d": 32,
    "f": 33,
    "g": 34,
    "h": 35,
    "j": 36,
    "k": 37,
    "l": 38,
    ";": 39,
    "'": 40,
    "`": 41,
    "shift": 42,
    "\\": 43,
    "z": 44,
    "x": 45,
    "c": 46,
    "v": 47,
    "b": 48,
    "n": 49,
    "m": 50,
    ",": 51,
    ".": 52,
    "/": 53,
    "rshift": 54,
    "*": 55,  # numpad *
    "alt": 56,
    "space": 57,
    "caps lock": 58,
    "f1": 59,
    "f2": 60,
    "f3": 61,
    "f4": 62,
    "f5": 63,
    "f6": 64,
    "f7": 65,
    "f8": 66,
    "f9": 67,
    "f10": 68,
    "f11": 87,
    "f12": 88,
    "f13": 100,
    "f14": 101,
    "f15": 102,
    "f16": 103,
    "f17": 104,
    "f18": 105,
    "f19": 106,
    "f20": 107,
    "f21": 108,
    "f22": 109,
    "f23": 110,
    "f24": 118,
    "num lock": 69,
    "scroll lock": 70,
    "numpad 7": 71,
    "numpad 8": 72,
    "numpad 9": 73,
    "numpad -": 74,
    "numpad 4": 75,
    "numpad 5": 76,
    "numpad 6": 77,
    "numpad +": 78,
    "numpad 1": 79,
    "numpad 2": 80,
    "numpad 3": 81,
    "numpad 0": 82,
    "numpad .": 83,
    "up": 72,
    "down": 80,
    "left": 75,
    "right": 77,
    "insert": 82,
    "delete": 83,
    "home": 71,
    "end": 79,
    "page up": 73,
    "page down": 81,
}
code_to_name = {
    1: "esc",
    2: "1",
    3: "2",
    4: "3",
    5: "4",
    6: "5",
    7: "6",
    8: "7",
    9: "8",
    10: "9",
    11: "0",
    12: "-",
    13: "=",
    14: "backspace",
    15: "tab",
    16: "q",
    17: "w",
    18: "e",
    19: "r",
    20: "t",
    21: "y",
    22: "u",
    23: "i",
    24: "o",
    25: "p",
    26: "[",
    27: "]",
    28: "enter",
    29: "ctrl",
    30: "a",
    31: "s",
    32: "d",
    33: "f",
    34: "g",
    35: "h",
    36: "j",
    37: "k",
    38: "l",
    39: ";",
    40: "'",
    41: "`",
    42: "shift",
    43: "\\",
    44: "z",
    45: "x",
    46: "c",
    47: "v",
    48: "b",
    49: "n",
    50: "m",
    51: ",",
    52: ".",
    53: "/",
    54: "rshift",
    55: "*",  # numpad *
    56: "alt",
    57: "space",
    58: "caps lock",
    59: "f1",
    60: "f2",
    61: "f3",
    62: "f4",
    63: "f5",
    64: "f6",
    65: "f7",
    66: "f8",
    67: "f9",
    68: "f10",
    69: "num lock",
    70: "scroll lock",
    71: "home",          # was numpad 7
    72: "up",            # was numpad 8
    73: "page up",       # was numpad 9
    74: "numpad -",
    75: "left",          # was numpad 4
    76: "numpad 5",
    77: "right",         # was numpad 6
    78: "numpad +",
    79: "end",           # was numpad 1
    80: "down",          # was numpad 2
    81: "page down",     # was numpad 3
    82: "insert",        # was numpad 0
    83: "delete",        # was numpad .
    87: "f11",
    88: "f12",
    100: "f13",
    101: "f14",
    102: "f15",
    103: "f16",
    104: "f17",
    105: "f18",
    106: "f19",
    107: "f20",
    108: "f21",
    109: "f22",
    110: "f23",
    118: "f24",
}

class v1:
    def __init__(self):
        keyboard.on_press(self.__on_key)
        self.key_dict = {}
    def __on_key(self, event):
        key = None
        if hasattr(event, 'scan_code'):
            key = event.scan_code
        elif hasattr(event, 'name'):
            # fallback to name-to-code map
            key = name_to_code.get(event.name)
        else:
            return  # can’t handle this event

        if key in self.key_dict:
            self.key_dict[key](key)

    def assign_hook(self, key, func):
        if type(key) == int:
            if key in code_to_name:
                self.key_dict[key] = func
        elif type(key) == str:
            if key in name_to_code:
                self.key_dict[name_to_code[key]] = func
class v2:
    def __init__(self):
        self.key_dict = {}
    def assign_hook(self, key, func):
        if type(key) == int:
            if key in code_to_name:
                self.key_dict[key] = func
        elif type(key) == str:
            if key in name_to_code:
                self.key_dict[name_to_code[key]] = func
    def check_input(self, key):
        if type(key) == str: key = name_to_code[key]
        if keyboard.is_pressed(key):
            self.key_dict[key]()
    def check_inputs(self):
        for key in self.key_dict.keys():
            if keyboard.is_pressed(key): self.key_dict[key]()
class v3:
    def __init__(self):
        self.key_dict = {}
        self.prev_state = {}

    def assign_hook(self, key, func):
        if type(key) == int:
            if key in code_to_name:
                self.key_dict[key] = func
                self.prev_state[key] = False
        elif type(key) == str:
            if key in name_to_code:
                key_code = name_to_code[key]
                self.key_dict[key_code] = func
                self.prev_state[key_code] = False

    def assign_faulty_hook(self, key):
        if type(key) == str: key = name_to_code[key]
        self.key_dict[key] = lambda: None

    def check_input(self, key):
        if type(key) == str:
            key = name_to_code[key]
        currently_pressed = keyboard.is_pressed(key)
        if currently_pressed and not self.prev_state.get(key, False):
            # Just pressed now
            self.key_dict[key]()
        self.prev_state[key] = currently_pressed

    def check_inputs(self):
        for key in self.key_dict.keys():
            currently_pressed = keyboard.is_pressed(key)
            if currently_pressed and not self.prev_state.get(key, False):
                self.key_dict[key]()
            self.prev_state[key] = currently_pressed

    def return_pressed(self):
        pressed_list = []
        for key in self.key_dict:
            currently_pressed = keyboard.is_pressed(key)
            if currently_pressed and not self.prev_state.get(key, False):
                pressed_list.append(key)
            self.prev_state[key] = currently_pressed
        return pressed_list


def Input(version: str):
    if version == "1.0":
        return v1
    elif version == "2.0":
        return v2
    elif version == "3.0":
        return v3
    else:
        raise FuckYouError("invalid version")