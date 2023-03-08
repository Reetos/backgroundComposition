import cv2
from moviepy.editor import *
import numpy as np

# Load the video clip with the green screen background
video = VideoFileClip("sofa.mp4")

# Load the background image
background = ImageClip("sunset.jpg").set_duration(video.duration)

# Define the green screen color
green = (76, 118, 54)

# Create a mask that extracts the green screen
def create_mask(frame):
    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    # Define the range of green color in HSV
    lower_green = np.array([50, 50, 50])
    upper_green = np.array([70, 255, 255])
    # Create a mask that extracts the green screen
    mask = cv2.inRange(hsv, lower_green, upper_green)
    # Convert the mask to RGB color space
    mask_rgb = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
    return mask_rgb

mask = video.fl_image(create_mask)

# Composite the green screen with the new background image
final = CompositeVideoClip([background, mask.set_position("center")])

# Write the output video file
final.write_videofile("output_video.mp4")
