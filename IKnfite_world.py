class Infinite_World:
    path = "gx/bg"
    filenames = [f for f in os.listdir(path) if f.endswith(".png")]
    imagelist = [
        pg.image.load(os.path.join(path, name)).convert_alpha() for name in filenames
    ]

    def __init__(self, player):
        self.player = player
        self.cam = self.player.camera
        self.bgdata = []
        self.next_bg_x = 0  # ne
        self.next_bg_y = 0

    def add_bg(self):
        bg = {}
        bg["img"] = random.choice(self.imagelist)
        bg["x"] = self.next_bg_x
        bg["y"] = self.next_bg_y
        bg["rect"] = bg["img"].get_rect(topleft=(bg["x"], bg["y"]))
        self.next_bg_x += bg[
            "img"
        ].get_width()  # update x coordinate for the next image
        self.next_bg_y += bg[
            "img"
        ].get_height()  # update x coordinate for the next image

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

            if (
                bg["rect"].right < camx
            ):  # if the image is completely out of the screen to the left
                self.bgdata.remove(bg)  # remove it
