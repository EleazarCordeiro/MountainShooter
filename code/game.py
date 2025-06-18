#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame.version import PygameVersion

from code.Const import WINDOW_WIDTH, WINDOW_HEIGHT
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self, ):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            menu = Menu(self.window)
            menu.run()
            pass
