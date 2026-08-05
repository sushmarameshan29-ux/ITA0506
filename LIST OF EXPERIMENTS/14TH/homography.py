import cv2
import numpy as np
import os

# Get image path
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "input.jpg")

print("Image Path:", image_path)

img = cv2.imread(image_path)

if img is None:
    print("Error: Image not found!")
    exit()

print("Image Loaded Successfully")

h, w = img.shape[:2]

src = np.float32([
    [0, 0],
    [w-1, 0],
    [0, h-1],
    [w-1, h-1]
])

dst = np.float32([
    [50, 50],
    [w-100, 20],
    [80, h-50],
    [w-50, h-80]
])

# Compute Homography Matrix
H, status = cv2.findHomography(src, dst)

# Apply Perspective Transformation
result = cv2.warpPerspective(img, H, (w, h))

# Save the output image
output_path = os.path.join(script_dir, "input_homography.jpg")
cv2.imwrite(output_path, result)

print("Output image saved as:", output_path)

# Display images
cv2.imshow("Original", img)
cv2.imshow("Homography", result)

cv2.waitKey(0)
cv2.destroyAllWindows()