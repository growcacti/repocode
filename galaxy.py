import pygame as pg
import random
from constants import Constants
from player import Player

con = Constants
screen = con.screen
W = con.W
H = con.H
W2 = con.W2
H2 = con.H2
QW = W / 4
HW = W / 2
HH = H / 2
QH = H / 4


screen = con.screen


WIDTH = con.WIDTH
HEIGHT = con.HEIGHT
WHITE = con.WHITE

pg.init()


RED = (255, 0, 0)

# Game Setup


screen = pg.display.set_mode((WIDTH, HEIGHT))


class Expanding_Galaxy:
    def __init__(self, player):
        self.colorlist = [
            pg.Color(color_name)
            for color_name in [
                "white",
                "gray59",
                "turquoise1",
                "mediumspringgreen",
                "lavender",
                "cyan1",
                "cyan2",
                "aquamarine",
                "aquamarine2",
                "antiquewhite",
                "gray70",
                "gray80",
                "maroon",
                "khaki",
                "darkturquoise",
                "cornsilk",
                "azure",
                "linen",
                "aliceblue",
                "ivory1",
                "snow",
                "paleturquoise1",
            ]
        ]

        self.surfaces = [pg.Surface((6, 6)).convert_alpha() for _ in range(18)]

        for surf in self.surfaces:
            color_name = random.choice(
                self.colorlist
            )  # Randomly select color for each surface
            radius = random.randint(1, 2)
            pos = (3, 3)
            pg.draw.circle(surf, color_name, pos, radius)

        self.player = player
        self.cam = self.player.camera
        self.camx, self.camy = self.cam
        self.bgdata = []
        self.player = player
        self.x = 1000
        self.y = 1000
        self.w = W
        self.H = H

    def coordinates(self, camx, camy, objw, objh):
        self.camxx = 2 * self.camx
        self.camyy = 2 * self.camy
        self.camrect = pg.Rect(self.camx, self.camy, W, H)
        while 1:
            self.startx = int(self.camx) - (W) // 1
            self.stopx = int(self.camx) + (W2) // 1
            self.starty = int(self.camy) - (H) // 1
            self.stopy = int(self.camy) + (H2) // 1
            self.rx = random.randint(self.startx, self.stopx)
            self.ry = random.randint(self.starty, self.stopy)
            self.objrect = pg.Rect(self.rx, self.ry, objw, objh)
            if not self.objrect.colliderect(self.camrect):
                return self.rx, self.ry

    def add_bg(self, camx, camy):
        self.bg = {}

        self.bg["img"] = self.starlist

        self.bg["width"] = 6
        self.bg["height"] = 6

        self.bg["x"], self.bg["y"] = self.coordinates(
            camx, camy, self.bg["width"], self.bg["height"]
        )
        self.bg["rect"] = pg.Rect(
            (self.bg["x"], self.bg["y"], self.bg["width"], self.bg["height"])
        )

        return self.bg

    def boundaries(self, camx, camy, bg):
        # Return False if camx and camy are more than
        # a half-window length beyond the edge of the window.
        self.bounds_left = self.camx - W
        self.bounds_top = self.camy - H
        self.boundsrect = pg.Rect(self.bounds_left, self.bounds_top, W2 * 2, H2 * 2)
        self.objrect = pg.Rect(
            self.bg["x"], self.bg["y"], self.bg["width"], self.bg["height"]
        )
        return not self.boundsrect.colliderect(self.objrect)

    def bgupdate(self, camx, camy):
        self.camx, self.camy = camx, camy

        if len(self.bgdata) < 3000000:
            self.bgdata.append(self.add_bg(self.camx, self.camy))

        for bg in self.bgdata:
            mrect = pg.Rect(
                (bg["x"] - self.camx, bg["y"] - self.camy, bg["width"], bg["height"])
            )
            for surf in self.surfaces:
                screen.blit(surf, mrect)

        self.bgdata = [
            bg for bg in self.bgdata if not self.boundaries(self.camx, self.camy, bg)
        ]

        return self.starlist, mrect  # (This line remains unchanged)
