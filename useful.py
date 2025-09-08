import numpy as np
from PIL import Image, ImageSequence
import display
v = display.VRAM

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-_=[]{};:'\"\\|<,>.?+/ "

def process_gif_frames_to_font_dict(filename):
    im = Image.open(filename)
    font_dict = {}

    for i, frame in enumerate(ImageSequence.Iterator(im)):
        if i >= len(chars):
            break  # stop if more frames than chars

        char = chars[i]
        rgba = frame.convert("RGBA")
        data = np.array(rgba)  # shape (H, W, 4)
        rgb = data[..., :3]    # ignore alpha for now


        # Optional: You can do grayscale or alpha processing here if you want,
        # but if you want raw RGB, just store it as is.
        font_dict[char] = rgb

    return font_dict

font = process_gif_frames_to_font_dict("font.gif")

class FrameBuffer:
    """
    Mostly deprecated. Only use for specific purposes.
    """
    def __init__(self, size_x, size_y):
        self.frame = np.zeros((size_x, size_y, 3), dtype=np.uint8)

    def write_pixel(self, color_tuple, position):
        self.frame[position[0], position[1]] = color_tuple

    def write_pixels(self, array, position):
        for y, x in np.ndindex(array.shape[0], array.shape[1]):
            self.write_pixel(array[y, x], [position[1] + y, position[0] + x])
        return x + 1

    def read_pixel(self, position):
        return self.frame[position[0], position[1]].tolist()

    def zero_frame(self):
        self.frame = np.zeros(self.frame.shape, dtype=np.uint8)