import pyautogui
import time
from PIL import ImageGrab, ImageOps
import numpy as np

# Coordinates of the game area where obstacles appear (you need to adjust these based on your screen)
# To find these coordinates, hover over the location on the screen and use pyautogui's `position()` function.
dino_position = (145, 752)  # Example coordinates near the dinosaur
box = (dino_position[0]+90, dino_position[1], dino_position[0]+250, dino_position[1]+30)

# Function to detect obstacles
def detect_obstacle():
    # Take a screenshot of the game area where obstacles appear
    image = ImageGrab.grab(box)
    
    # Convert the image to grayscale for better processing
    gray_image = ImageOps.grayscale(image)
    
    # Convert image to a numpy array to analyze pixel data
    image_array = np.array(gray_image)
    
    # Calculate the sum of pixel values to detect any obstacles
    # The higher the sum, the more likely an obstacle is detected
    print(f"Sum: {image_array}")
    return np.sum(image_array)

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
        if detect_obstacle() < 2000:  # Threshold for obstacle detection (tune based on your screen)
            jump()  # Jump when an obstacle is detected
        
        # Small sleep to control game speed
        time.sleep(0.05)

if __name__ == "__main__":
    play_game()
