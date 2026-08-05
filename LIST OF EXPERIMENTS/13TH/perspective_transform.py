import cv2
import numpy as np
import os

# Get the current script folder
script_dir = os.path.dirname(os.path.abspath(__file__))

# Input video path (place captured_video.mp4 in the 13th experiment folder)
video_path = os.path.join(script_dir, "captured_video.mp4")

# Output video path
output_path = os.path.join(script_dir, "perspective_output.mp4")

# Open the video
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video.")
    exit()

# Get video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Source points
src = np.float32([
    [0, 0],
    [width - 1, 0],
    [0, height - 1],
    [width - 1, height - 1]
])

# Destination points
dst = np.float32([
    [50, 50],
    [width - 50, 20],
    [80, height - 50],
    [width - 80, height - 20]
])

# Perspective transformation matrix
M = cv2.getPerspectiveTransform(src, dst)

# Process video
while True:
    ret, frame = cap.read()

    if not ret:
        break

    transformed = cv2.warpPerspective(frame, M, (width, height))

    # Save transformed frame
    out.write(transformed)

    # Display
    cv2.imshow("Original Video", frame)
    cv2.imshow("Perspective Transformation", transformed)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

print("Perspective transformed video saved successfully!")
print("Saved at:", output_path)