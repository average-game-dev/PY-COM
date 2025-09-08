import display; import useful; import disk; import input; from error import *
import pygame; import numpy as np

i = input.Input("3.0")()
v = display.VRAM(480, 480)
clock = pygame.time.Clock()

# helpers and shit to make life easier
def write_letters(text, position, cla=v):
    x, y = position
    for char in text:
        cla.write_pixels(useful.font[char], [x, y])
        x += 12

input_text = []

for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-_=[]{};:'\"\\|<,>.?+/ ":
    i.assign_faulty_hook(char)

import pygame

input_text = []

try:
    while True:
        # Process all pending events (including window messages)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise KeyboardInterrupt  # or break the loop gracefully

        # Your game logic / rendering
        write_letters(">".join(input_text), [0, 0])

        for char in i.return_pressed():
            input_text.append(char)

        v.update_screen()

except KeyboardInterrupt:
    pygame.quit()
    exit(0)
