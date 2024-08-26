import pygame
from pathlib import Path

BASE_IMG_PATH = str(Path(__file__).parent.parent / 'assets') + '\\'


def load_image(path):
    img = pygame.image.load(str(BASE_IMG_PATH) + path).convert()
    img.set_colorkey((255, 255, 255))
    return img

