import cv2
import numpy as np

# Load the MP4 video
cap = cv2.VideoCapture('sofa.mp4')

# Load the PNG background image with alpha channel
background = cv2.imread('sunset.jpg', cv2.IMREAD_UNCHANGED)

# Define the lower and upper bounds of the green screen color in HSV color space
lower_green = np.array([50, 100, 100])
upper_green = np.array([70, 255, 255])

# Get the frame size and frame rate of the input video
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Create the VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output_video_2.mp4', fourcc, fps, (frame_width, frame_height))

# Loop through the frames of the video
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask for the green screen color
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Invert the mask to get the foreground
    fg = cv2.bitwise_not(mask)

    # Apply the mask to the frame to get the foreground
    fg_frame = cv2.bitwise_and(frame, frame, mask=mask)

    # Resize the background to match the frame size
    resized_background = cv2.resize(background, (frame_width, frame_height))

    # Apply the inverted mask to the background to get the foreground
    fg_background = cv2.bitwise_and(resized_background, resized_background, mask=fg)

    # Combine the foreground and background to get the final frame
    final = cv2.add(fg_frame, fg_background)

    # Write the final frame to the output video
    out.write(final)

    # Show the final frame
    cv2.imshow('Final', final)

    # Wait for the 'q' key to be pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the resources
cap.release()
out.release()
cv2.destroyAllWindows()