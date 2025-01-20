import os
import pygame
import sys
import math


# функции игры
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def movement(x, y, s, cx, cy):
    g = ((x - cx) * 2 + (y - cy) * 2) * 0.5
    if g == 0:
        return
    if g == 0:
        g = 1
    u = math.asin((y - cy) / g)
    res = [int(round(abs(s * math.cos(u)))), int(round(abs(s * math.cos(math.pi / 2 - u))))]
    if cx == x and cy == y:
        return None
    if x < cx:
        res[0] = x + res[0]
    else:
        res[0] = x - res[0]
    if y < cy:
        res[1] = y + res[1]
    else:
        res[1] = y - res[1]

    return res

