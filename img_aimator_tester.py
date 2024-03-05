import pygame
import sys

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 10  # Adjust this to control the speed of the "animation"

# Colors
WHITE = (255, 255, 255)

# List of image paths
image_paths = [
    "path/to/image1.png",
    "path/to/image2.png",
    ...,
]  # Add your image paths here
images = [pygame.image.load(img_path) for img_path in image_paths]

# Initialize screen and clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Image Viewer")
clock = pygame.time.Clock()

current_image = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Optionally add controls to go to next or previous image using keyboard arrows
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                current_image = (current_image + 1) % len(images)
            elif event.key == pygame.K_LEFT:
                current_image = (current_image - 1) % len(images)

    screen.fill(WHITE)
    # Get the current image and its dimensions
    image = images[current_image]
    img_width, img_height = image.get_size()

    # Draw the current image at the center of the screen
    screen.blit(
        image, ((SCREEN_WIDTH - img_width) // 2, (SCREEN_HEIGHT - img_height) // 2)
    )

    pygame.display.flip()
    clock.tick(FPS)
