class Nme:
    # ... [rest of the initialization]

    def move_and_face_player(self, player_pos):
        """
        Move towards the player's position and adjust the angle to face the player.
        """
        direction_vector = player_pos - self.position
        distance_to_player = direction_vector.length()

        # Normalize the direction vector
        if distance_to_player > 0:
            direction_vector /= distance_to_player

        # Move the enemy towards the player
        self.position += direction_vector * self.velocity

        # Set the enemy's angle to face the player
        self.angle = -math.degrees(atan2(direction_vector.y, direction_vector.x))

    def fire_projectile(self):
        """
        Fires a projectile based on the enemy's position and angle.
        Returns the initial position and direction for the projectile.
        """
        projectile_position = Vector2(self.position)
        projectile_direction = Vector2(
            cos(radians(-self.angle)), sin(radians(-self.angle))
        )

        return projectile_position, projectile_direction

    # ... [rest of the methods]


class Nme:
    # ... [rest of the initialization]

    def move_and_face_player(self, player_pos):
        """
        Move towards the player's position and adjust the angle to face the player.
        """
        direction_vector = player_pos - self.position
        distance_to_player = direction_vector.length()

        # Normalize the direction vector
        if distance_to_player > 0:
            direction_vector /= distance_to_player

        # Move the enemy towards the player
        self.position += direction_vector * self.velocity

        # Set the enemy's angle to face the player
        self.angle = -math.degrees(atan2(direction_vector.y, direction_vector.x))

    def fire_projectile(self):
        """
        Fires a projectile based on the enemy's position and angle.
        Returns the initial position and direction for the projectile.
        """
        projectile_position = Vector2(self.position)
        projectile_direction = Vector2(
            cos(radians(-self.angle)), sin(radians(-self.angle))
        )

        return projectile_position, projectile_direction

    # ... [rest of the methods]


enemy = Nme(some_image, start_x, start_y)
player_position = Vector2(player_x, player_y)

# Every update/frame:
enemy.move_and_face_player(player_position)

# When you want to fire a projectile:
proj_pos, proj_dir = enemy.fire_projectile()
