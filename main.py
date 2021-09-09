#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import pygame
import director
import Menu
import Pong
 
def main():
    dir = director.Director()
    scene_juego = Pong.Pong(dir)
    scene_menu = Menu.Menu(dir)
    dir.change_scene(scene_juego)
    dir.loop(scene_menu, scene_juego)
 
if __name__ == '__main__':
    pygame.init()
    main()