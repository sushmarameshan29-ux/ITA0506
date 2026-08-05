import cv2
import os

# Get current folder path
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "input.png")

# Read the image
img = cv2.imread(image_path)

if img is None:
    print("Error: input.png not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Perform Canny Edge Detection
edges = cv2.Canny(gray, 100, 200)

# Save the output image
output_path = os.path.join(script_dir, "canny_output.png")
cv2.imwrite(output_path, edges)

print("Output saved as:", output_path)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Canny Edge Detection", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()