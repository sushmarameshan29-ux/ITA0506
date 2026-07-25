import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
import os


# 12th experiment folder path
save_folder = r"C:\Users\DELL\OneDrive\Desktop\my work\python learning\12th experiment"


# Select image
root = tk.Tk()
root.withdraw()

image_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
)


# Read image
image = cv2.imread(image_path)

if image is None:
    print("Image not found")
    exit()


# Image size
height, width = image.shape[:2]


# Four points from original image
points1 = np.float32([
    [50, 50],
    [width-50, 50],
    [50, height-50],
    [width-50, height-50]
])


# Destination points
points2 = np.float32([
    [0, 0],
    [width, 100],
    [100, height],
    [width-100, height-100]
])


# Create perspective transformation matrix

matrix = cv2.getPerspectiveTransform(
    points1,
    points2
)


# Apply perspective transformation

perspective_image = cv2.warpPerspective(
    image,
    matrix,
    (width, height)
)


# Display images

cv2.imshow("Original Image", image)

cv2.imshow(
    "Perspective Transformed Image",
    perspective_image
)


# Save output image

cv2.imwrite(
    os.path.join(save_folder, "perspective_image.jpg"),
    perspective_image
)


print("Perspective Transformation completed!")
print("Image saved in 12th experiment folder")


cv2.waitKey(0)
cv2.destroyAllWindows()