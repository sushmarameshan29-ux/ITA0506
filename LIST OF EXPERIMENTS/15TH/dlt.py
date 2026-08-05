import cv2
import numpy as np
import os

# Load image from the same folder as this script
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "input.jpg")

img = cv2.imread(image_path)

if img is None:
    print("Error: input.jpg not found!")
    exit()

h, w = img.shape[:2]

# Source points
src_pts = np.float32([
    [0, 0],
    [w - 1, 0],
    [0, h - 1],
    [w - 1, h - 1]
])

# Destination points
dst_pts = np.float32([
    [50, 50],
    [w - 80, 20],
    [80, h - 40],
    [w - 40, h - 70]
])

# Compute Homography (DLT)
H, status = cv2.findHomography(src_pts, dst_pts, method=0)

# Apply Perspective Transformation
result = cv2.warpPerspective(img, H, (w, h))

# Save the transformed image
output_path = os.path.join(script_dir, "input_dlt.jpg")
cv2.imwrite(output_path, result)

print("Output image saved as:", output_path)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("DLT Transformation", result)

cv2.waitKey(0)
cv2.destroyAllWindows()