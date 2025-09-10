import numpy as np
import pygame
from numba import njit

@njit
def write_pixels_numba(vram, array, pos_y, pos_x):
    h, w = array.shape[0], array.shape[1]
    for y in range(h):
        for x in range(w):
            vram[pos_y + y, pos_x + x, 0] = array[y, x, 0]
            vram[pos_y + y, pos_x + x, 1] = array[y, x, 1]
            vram[pos_y + y, pos_x + x, 2] = array[y, x, 2]
    return pos_x + w

class VRAM:
    def __init__(self, size_x, size_y, scale_x=1, scale_y=1):
        self.vram = np.zeros((size_x, size_y, 3), dtype=np.uint8)
        self.resolution = (size_x, size_y)
        self.scale = (scale_x, scale_y)
        pygame.init()
        self.screen = pygame.display.set_mode((size_x * scale_x, size_y * scale_y))

    def write_pixel(self, color_tuple, position):
        self.vram[position[0], position[1]] = color_tuple

    def write_pixels(self, array, position):
        return write_pixels_numba(self.vram, array, position[1], position[0])

    def read_pixel(self, position):
        return self.vram[position[0], position[1]].tolist()

    def update_screen(self):
        surface = pygame.surfarray.make_surface(np.transpose(self.vram, (1, 0, 2)))
        surface = pygame.transform.scale(surface, self.screen.get_size())  # scale the internal surface
        self.screen.blit(surface, (0, 0))
        pygame.display.flip()

if __name__ == "__main__":
    v = VRAM(480, 480, 2, 2)
    clock = pygame.time.Clock()
    try:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            v.vram = np.random.randint(0, 256, (480, 480, 3), dtype=np.uint8)

            v.update_screen()
            clock.tick(30)
    except KeyboardInterrupt:
        exit(0)
