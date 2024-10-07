import pyautogui
import time
from PIL import ImageGrab, ImageOps
import numpy as np

JUMP_KEY = 'space'

# Function to prompt user to click the dinosaur and set the position
def get_dinosaur_position():
    print("Move your mouse over the dinosaur and press Enter.")
    input()  # Wait for user to press Enter after placing the mouse on the dinosaur
    dino_position = pyautogui.position()
    print(f"Dinosaur position captured at: {dino_position}")
    return dino_position

# Function to automatically define the game area based on the dinosaur's position
def get_game_area(dino_position):
    # Define the area in front of the dinosaur where obstacles appear
    # The x and y offsets here are an estimate, adjust them if needed
    x_offset = 90
    y_offset = 0
    box_width = 250
    box_height = 40
    
    box = (dino_position[0] + x_offset, dino_position[1] + y_offset, 
           dino_position[0] + x_offset + box_width, dino_position[1] + y_offset + box_height)
    
    print(f"Game area defined as: {box}")
    return box

# Function to detect obstacles in the defined game area
def detect_obstacle(game_area):
    # Capture the game area
    image = ImageGrab.grab(game_area)
    
    # Convert the image to grayscale for processing
    gray_image = ImageOps.grayscale(image)
    
    # Convert the image to a numpy array for pixel analysis
    image_array = np.array(gray_image)
    
    # Sum the pixel values to detect obstacles
    sum_of_pixels =  np.sum(image_array)
    print(f"Obstacle Detection Threshold Value: {sum_of_pixels}")
    return sum_of_pixels

# Function to make the dinosaur jump
def jump():
    pyautogui.press(JUMP_KEY)

# Main game loop
def play_game():
    # Step 1: Capture the dinosaur's position dynamically
    dino_position = get_dinosaur_position()
    
    # Step 2: Define the game area based on the dinosaur's position
    game_area = get_game_area(dino_position)
    
    print("Starting game in 3 seconds...")
    time.sleep(3)  # Short delay to switch to the game window
    
    while True:
        # Step 3: Continuously check for obstacles
        if detect_obstacle(game_area) < 5000:  # Adjust the threshold as needed
            jump()
        
        # Small sleep to avoid overwhelming the system
        time.sleep(0.05)

if __name__ == "__main__":
    play_game()
