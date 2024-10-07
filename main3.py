import pyautogui
import time
from PIL import ImageGrab, ImageOps
import numpy as np

# Coordinates of the game area where obstacles appear (you need to adjust these based on your screen)
# To find these coordinates, hover over the location on the screen and use pyautogui's `position()` function.
dino_position = (145, 752)  # Example coordinates near the dinosaur
box = (dino_position[0]+90, dino_position[1], dino_position[0]+90+250, dino_position[1]+40)

# NOTE: 
# Uncomment and call the function below to get dino_position the 
# first time you run the program.
#
# Use the value printed for the dino_position value above.
# Function to prompt user to click the dinosaur and set the position
# def get_dinosaur_position():
#     print("Move your mouse over the dinosaur and press Enter.")
#     input()  # Wait for user to press Enter after placing the mouse on the dinosaur
#     dino_position = pyautogui.position()
#     print(f"Dinosaur position captured at: {dino_position}")
#     return dino_position

# Function to detect obstacles
def detect_obstacle(game_area):
    # Capture the game area
    image = ImageGrab.grab(game_area)
    
    # Convert the image to grayscale for processing
    gray_image = ImageOps.grayscale(image)
    
    # Convert the image to a numpy array for pixel analysis
    image_array = np.array(gray_image)
    
    # Set a pixel intensity threshold to detect obstacles (darker pixels)
    # In grayscale, values closer to 255 are lighter, closer to 0 are darker
    obstacle_pixel_threshold = 180  # Pixels darker than this are considered obstacles
    
    # Count how many pixels are darker than the threshold
    obstacle_pixels = np.sum(image_array < obstacle_pixel_threshold)
    
    # print(f"Obstacle pixel count: {obstacle_pixels}")  # Print for debugging
    return obstacle_pixels

# Function to make the dinosaur jump
def jump():
    # pyautogui.keyDown('space')
    # time.sleep(0.05)  # Short pause to ensure the jump is detected
    # pyautogui.keyUp('space')
    pyautogui.press('space')

# Main game loop
def play_game():
    print("Starting game in 3 seconds...")
    time.sleep(3)  # Short delay to switch to the game window
    
    while True:
        # Continuously check for obstacles
        if detect_obstacle(box) > 300:  # Threshold for obstacle detection (tune based on your screen)
            jump()  # Jump when an obstacle is detected
        
        # Small sleep to control game speed
        time.sleep(0.05)

if __name__ == "__main__":
    play_game()
