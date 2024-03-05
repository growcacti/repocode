world_map = [
    ["top_left.tmx", "top.tmx", "top_right.tmx"],
    ["left.tmx", "center.tmx", "right.tmx"],
    ["bottom_left.tmx", "bottom.tmx", "bottom_right.tmx"],
]
self.map_x = 1  # Starting position in the world map (center)
self.map_y = 1
# Check if the player is near the edge of the current map
if player_pos[0] < 0:
    # Move to the left map
    self.map_x -= 1
elif player_pos[0] > self.width:
    # Move to the right map
    self.map_x += 1
elif player_pos[1] < 0:
    # Move to the upper map
    self.map_y -= 1
elif player_pos[1] > self.height:
    # Move to the lower map
    self.map_y += 1
else:
    # The player is not near the edge of the current map
    return

# Load the new map
new_map = Map(f"maps/{world_map[self.map_y][self.map_x]}")

# Determine the new player position
if player_pos[0] < 0:
    new_x = new_map.width - TILESIZE
    new_y = player_pos[1]
elif player_pos[0] > self.width:
    new_x = TILESIZE
    new_y = player_pos[1]
elif player_pos[1] < 0:
    new_x = player_pos[0]
    new_y = new_map.height - TILESIZE
else:  # player_pos[1] > self.height
    new_x = player_pos[0]
    new_y = TILESIZE

# Update the camera and the current map
self.camera.topleft = (new_x - int(WIDTH / 2), new_y - int(HEIGHT / 2))
self.width = new_map.width
self.height = new_map.height
self.current_map = new_map.current_map
