import pygame as pg
import random
import pytmx
import os
from constants import *
from player import *


con = Constants

screen = con.screen
WIDTH = con.WIDTH
HEIGHT = con.HEIGHT


class Infinite_World:
    filenames = [f for f in os.listdir(os.getcwd()) if f.endswith(".tmx")]

    tmlist = [
        pytmx.load_pygame(os.path.join(os.getcwd(), name), pixelalpha=True)
        for name in filenames
    ]

    def __init__(self, player):
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm
        self.camera = Camera(self.width, self.height)

        self.player = player
        self.pos = self.player.position
        self.cam = self.player.camera
        self.width = WIDTH
        self.height = HEIGHT
        self.bgdata = []
        self.next_bg_x = 0  # next background image x coordinate
        self.surf = pg.Surface((3200, 3200))
        self.surf_rect = self.surf.get_rect()

    def convert_tmx_to_surface(self, tm):
        # Create a new surface with the size of the map
        map_surface = pg.Surface((tm.width * tm.tilewidth, tm.height * tm.tileheight))

        # Get the tile images method
        ti = tm.get_tile_image_by_gid

        # Iterate over the layers and the tiles in each layer
        for layer in tm.layers:
            for x, y, gid in layer:
                # Get the tile image
                tile = ti(gid)
                if tile:
                    # Blit the tile image to the correct position on the surface
                    map_surface.blit(tile, (x * tm.tilewidth, y * tm.tileheight))

        # Return the map surface
        return map_surface

    def add_bg(self):
        bg = {}
        tm = random.choice(self.tmlist)
        bg["img"] = self.convert_tmx_to_surface(tm)
        bg["x"] = self.next_bg_x
        bg["y"] = 0
        bg["rect"] = bg["img"].get_rect(topleft=(bg["x"], bg["y"]))
        self.next_bg_x += bg[
            "img"
        ].get_width()  # update x coordinate for the next image
        return bg

    def update(self, camx, camy):
        if (
            not self.bgdata or self.bgdata[-1]["rect"].right < camx + WIDTH
        ):  # add new image if needed
            self.bgdata.append(self.add_bg())

        for bg in self.bgdata[
            :
        ]:  # iterate over a copy of the list because we might modify it
            mrect = pg.Rect((bg["x"] - camx, bg["y"] - camy), bg["img"].get_size())
            screen.blit(bg["img"], mrect)
