"""
The main error handling script.
"""

class DisplayError(Exception):
    def __init__(self, message: str = "A general display error has occurred.", *args):
        super().__init__(f"{message} {args}")

class DiskError(Exception):
    def __init__(self, message: str = "A general disk error has occurred.", *args):
        super().__init__(f"{message} {args}")

class InputError(Exception):
    def __init__(self, message: str = "A general input error has occurred.", *args):
        super().__init__(f"{message} {args}")

class Error(Exception):
    def __init__(self, message: str = "An inexplicable general error that some dumbass didn't classify.", *args):
        super().__init__(f"{message} {args}")

class FuckYouError(Exception):
    def __init__(self, message: str = "An error has occurred that could've been stopped with some more manual static analysis or you, the user, fucked up in a very bad way.", *args):
        super().__init__(f"{message} {args}")

class WTFError(Exception):
    def __init__(self, *args):
        super().__init__("How the fuck did this happen? One of three things occurred:\n"
        "1: A work of god has fucked this up.\n"
        "2: A cosmic ray has flipped a bit in your RAM causing the program to crash\n"
        "3: The Pharaoh's Curse has struck\n\n"
        f"It is up to you to figure out which one happened. {args}")
