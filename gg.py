import pygame
from pygame.locals import *
import random

# Set screen size and road dimensions
size = width, height = (1200, 800)
road_w = int(width / 1.6)  # Width of the road
roadmark_w = int(width / 80)  # Width of the road markings
right_lane = width / 2 + road_w / 4  # Center of the right lane
left_lane = width / 2 - road_w / 4   # Center of the left lane

speed = 1  # Initial speed of the opposing car

# Initialize Pygame
pygame.init()

running = True
screen = pygame.display.set_mode((size))
pygame.display.set_caption("Dev Car Game")
screen.fill((60, 220, 0))  # Fill background with light green

pygame.display.update()

# Load car images and set initial positions
car = pygame.image.load("car.png")
car_loc = car.get_rect()
car_loc.center = right_lane, height * 0.8  # Place car in right lane near bottom

car2 = pygame.image.load("othercar.png")
car2_loc = car.get_rect()
car2_loc.center = left_lane, height * 0.2  # Place opposing car in left lane near top

counter = 0

while running:
    counter += 1

    # Increase difficulty every 5000 frames (adjust as needed)
    if counter == 5000:
        speed += 0.15  # Increase speed
        counter = 0
        print("LEVEL UP", speed)

    # Move opposing car down the screen
    car2_loc[1] += speed

    # Reset opposing car position when it goes off-screen
    if car2_loc[1] > height:
        if random.randint(0, 1) == 0:  # Randomly choose lane
            car2_loc.center = right_lane, -200  # Place car off-screen, right lane
        else:
            car2_loc.center = left_lane, -200   # Place car off-screen, left lane

    # Check for collision (basic implementation, can be improved)
    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 250:
        print("LAMAO DEATH")
        break  # Exit the game loop

    # Handle user input for car movement
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w / 2), 0])  # Move left (half road width)
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_w / 2), 0])   # Move right (half road width)

    # Draw the road and road markings
    pygame.draw.rect(screen, (50, 50, 50), (width / 2 - road_w / 2, 0, road_w, height))  # Gray road
    pygame.draw.rect(screen, (255, 240, 60), (width / 2 - roadmark_w / 2, 0, roadmark_w, height))  # Yellow road marking (center)
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 - road_w / 2 + roadmark_w * 2, 0, roadmark_w, height))  # White road marking (left)
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 + road_w / 2 - roadmark_w * 3, 0, roadmark_w, height))  # White road marking (right)

    # Draw the cars on the screen
    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)