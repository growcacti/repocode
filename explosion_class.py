import pygame


class Explosion:
    def __init__(self, position, images):
        self.position = position
        self.images = images
        self.index = 0
        self.image = images[self.index]
        self.rect = self.image.get_rect(center=position)
        self.alive = True
        self.frame_counter = 0  # Counter for frames
        self.frame_rate = 3  # Change image every 3 frames

    def update(self):
        self.frame_counter += 1
        if self.frame_counter >= self.frame_rate:
            self.index += 1
            self.frame_counter = 0  # Reset the frame counter
            if self.index >= len(self.images):
                self.alive = False
                return
            self.image = self.images[self.index]


# Assume you have initialized pygame and loaded a list of images into 'explosion_images'

explosion = Explosion((100, 100), explosion_images)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    explosion.update()

    # Render the explosion or other game elements
    # ... your rendering code here ...

    pygame.display.flip()
    clock.tick(60)  # Limit to 60 frames per second
