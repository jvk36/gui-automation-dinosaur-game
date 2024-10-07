
# BEFORE RUNNING THE FILES EXECUTE THE FOLLOWING IN THE TERMINAL FROM THE WORKING FOLDER:
pip install -r requirements.txt

## PROJECT INTRO:

The project automates the Google Chrome Dinosaur Game (https://elgoog.im/dinosaur-game/) using Python libraries like pyautogui for controlling mouse and keyboard inputs, and Pillow (PIL) for image processing. The main idea is being able to make the dinosaur jump at the right time by detecting obstacles:

Detect Obstacles: We take screenshots of the game area to identify obstacles.
Jumping Logic: When an obstacle is detected close to the dinosaur, the script will make the dinosaur jump by simulating a keyboard press.
Image Detection: We save a reference image of an obstacle (like a cactus) using Pillow and detect this in the screenshots.

Library Requirements:

pyautogui: for simulating the keypress to jump
Pillow: for screenshot and image detection

## First Attempt - main.py - EXPLANATION:

Game Area Definition:

dino_position represents the coordinates near the dinosaur. We need to adjust this based on where the dinosaur is on your screen.
box defines the area in front of the dinosaur to monitor for obstacles (like cacti). We adjust these dimensions to match the game on your screen.

detect_obstacle():

The game screen area in box is captured using ImageGrab.grab().
The screenshot is converted to grayscale and then to a NumPy array for easier analysis.
The pixel values are summed to detect obstacles. If the sum is below a threshold, it indicates an obstacle in the path.

jump():

This function uses pyautogui to simulate pressing the spacebar, making the dinosaur jump.

play_game():

The main loop continuously checks for obstacles and makes the dinosaur jump if an obstacle is detected.

NOTE 1: dino_position is arbitrary. We need a way to get this info dynamically. 

NOTE 2: The detect_obstacle logic is flawed as the sums are large for white space and so checking below a threshold will not work.

## Second Attempt - main1.py - EXPLANATION:

To dynamically capture the game area and the dinosaur's position when the program starts, we can leverage pyautogui to prompt the user to define the region by clicking on the dinosaur and the obstacle detection zone.

Refactored approach:

Dynamically Capture Dinosaur Position: The user clicks on the dinosaur to get the coordinates.
Automatically Define the Game Area: Based on the position of the dinosaur, we can automatically define the region where obstacles appear.

Obstacle Detection: Once the game area is defined, the program will use the same logic to detect obstacles and trigger jumps.

NOTE: This solves the arbitrary dino_position issue but the detect_obstacle logic is still flawed.

## Third Attempt - main2.py - EXPLANATION: 

Dynamic Dinosaur Position Capture:

The function get_dinosaur_position() prompts the user to place the mouse over the dinosaur and press Enter. This captures the exact screen coordinates of the dinosaur dynamically.

Game Area Definition:

The get_game_area() function takes the dinosaur’s position and automatically defines the area in front of the dinosaur where obstacles appear. The x_offset and box_width variables control the detection area size (which you may need to adjust slightly based on your screen).

Fixing the Obstacle Detection Logic:

Instead of counting the dark pixels (<100), we'll count how many pixels are significantly darker than white.
The logic will be based on detecting obstacles that have pixel values much lower than white (255, 255, 255), so we need to count pixels that are close to black.
We can set an upper threshold to detect darker pixels (for example, pixels below 200 or 180), which should correspond to obstacles.

Updated Code for Obstacle Detection:

Use Grayscale Conversion to reduce computational complexity (same as before).
Detect Darker Pixels: We will look for pixels with a value below a threshold (e.g., 180) to identify obstacles.

## Final Attempt - main3.py - EXPLANATION: 

The logic is pretty much the same as in main2.py with the difference that the dino_position is set to something that worked in our test computer initially. The dynamic dinosaur detection code is commented out and a note added to indicate to use that
code to get the dinosaur position the first time one uses the program. 
