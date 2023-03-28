import pyautogui
import time
import random
import os
from Xlib import display as xdisplay

# Get the current value of the DISPLAY variable
display = os.environ['DISPLAY']

# Get the active user's display
d = xdisplay.Display(display)
screen = d.screen()
screen_width = screen.width_in_pixels
screen_height = screen.height_in_pixels

while True:
    # Generate a random position within the screen boundaries
    random_x = random.randint(0, screen_width)
    random_y = random.randint(0, screen_height)

    # Get the current mouse position
    current_x, current_y = pyautogui.position()

    # Move the mouse cursor to the random position
    pyautogui.moveTo(random_x, random_y, duration=0.25)

    # Wait for 1-2 seconds
    time.sleep(1 + 1 * (time.time() % 2))

    # Move the mouse cursor back to its original position
    pyautogui.moveTo(current_x, current_y, duration=0.25)

    # Wait for mentioned seconds before repeating the process
    time.sleep(10)
