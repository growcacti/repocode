   cell_size = 32
        num_levels = 5
        rooms_per_level = (10, 30)
        self.dungeon = Dungeon(num_levels, rooms_per_level, cell_size)






  def update(self, dt):
        mouse_pos = pg.mouse.get_pos()
        self.dungeon.update(dt, mouse_pos)
        if self.dungeon.done:
            self.next = self.dungeon.next
            self.do  self.screen = pg.display.get_surface()
        self.caption = caption
        self.done = False
        self.clock = pg.time.Clock()
        self.fps = 60.0
        self.show_fps = False
        self.current_time = 0.0
        self.keys = pg.key.get_pressed()
        self.state_dict = {}
        self.state_name = None
        self.state = None
        self.fullscreen = Falsene = True
            self.dungeon.done = False
            self.persist["dungeon"] = self.dungeon




def load_all_gfx(directory, colorkey=(0, 0, 0), accept=(".png", ".jpg", ".bmp")):
    """Load all graphics with extensions in the accept argument.  If alpha
    transparency is found in the image the image will be converted using
    convert_alpha().  If no alpha transparency is detected image will be
    converted using convert() and colorkey will be set to colorkey."""
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorkey)
            graphics[name] = img
    return graphics



def strip_from_sheet(sheet, start, size, columns, rows=1):
    """Strips individual frames from a sprite sheet given a start location,
    sprite size, and number of columns and rows."""
    frames = []
    for j in range(rows):
        for i in range(columns):
            location = (start[0] + size[0] * i, start[1] + size[1] * j)
            frames.append(sheet.subsurface(pg.Rect(location, size)))
    return frames


def strip_coords_from_sheet(sheet, coords, size):
    """Strip specific coordinates from a sprite sheet."""
    frames = []
    for coord in coords:
        location = (coord[0] * size[0], coord[1] * size[1])
        frames.append(sheet.subsurface(pg.Rect(location, size)))
    return frames


def get_cell_coordinates(rect, point, size):
    """Find the cell of size, within rect, that point occupies."""
    cell = [None, None]
    point = (point[0] - rect.x, point[1] - rect.y)
    cell[0] = (point[0] // size[0]) * size[0]
    cell[1] = (point[1] // size[1]) * size[1]
    return tuple(cell)


def cursor_from_image(image):
    """Take a valid image and create a mouse cursor."""
    colors = {(0, 0, 0, 255): "X", (255, 255, 255, 255): "."}
    rect = image.get_rect()
    icon_string = []
    for j in range(rect.height):
        this_row = []
        for i in range(rect.width):
            pixel = tuple(image.get_at((i, j)))
            this_row.append(colors.get(pixel, " "))
        icon_string.append("".join(this_row))
    return icon_string


def color_swap(source_image, swap_map):
    """
    Creates a new Surface from the source_image with some or all colors
    swapped for new colors. Colors are swapped according to the
    color pairs in the swap_map dict. The keys and values in swap_map
    can be RGB tuples or pygame color-names. For each key in swap_map,
    all pixels of that color will be replaced by the color that key maps to.
    For example, passing this dict:

    {(0,255,0): (255, 0, 255),
      "black": (255, 0, 0),
      "yellow": "green"}

    would result in green pixels recolored purple, black pixels recolored
    red and yellow pixels recolored green.
    NOTE: This will not work if Pygame's video mode has not been set
    (i.e., you need to call pygame.display.set_mode beforehand).
    """
    img = source_image
    size = img.get_size()
    surf = pg.Surface(size)
    color_surf = pg.Surface(size)
    final = img.copy()
    for original_color, new_color in swap_map.items():
        if isinstance(original_color, str):
            original = pg.Color(original_color)
        else:
            original = original_color
        if isinstance(new_color, str):
            recolor = pg.Color(new_color)
        else:
            recolor = new_color
        color_surf.fill(original)
        surf.set_colorkey(original)
        pg.transform.threshold(
            surf, img, original, (0, 0, 0, 0), recolor, 1, color_surf, True
        )
        final.blit(surf, (0, 0))
    return final


def lerp(color_1, color_2, lerp_val):
    """
    Return a new color that is a linear interpolation of the two
    argument colors.  lerp_val must be between 0 and 1 (inclusive).
    """
    if not (0 <= lerp_val <= 1):
        raise ValueError("Lerp value must be in the range [0,1] inclusive.")
    new = [int(a * (1 - lerp_val) + b * lerp_val) for a, b in zip(color_1, color_2)]
    return pg.Color(*new)



            
