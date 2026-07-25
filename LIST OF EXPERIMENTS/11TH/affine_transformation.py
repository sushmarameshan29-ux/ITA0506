import cv2
import tkinter as tk
from tkinter import filedialog
import os
import numpy as np


# 11th experiment folder path
save_folder = r"C:\Users\DELL\OneDrive\Desktop\my work\python learning\11th experiment"


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


# Get image size
rows, cols = image.shape[:2]


# -------- Select three points from original image --------

points1 = np.float32([
    [50, 50],
    [200, 50],
    [50, 200]
])


# -------- Destination points --------

points2 = np.float32([
    [10, 100],
    [200, 50],
    [100, 250]
])


# Create affine transformation matrix

matrix = cv2.getAffineTransform(
    points1,
    points2
)


# Apply transformation

affine_image = cv2.warpAffine(
    image,
    matrix,
    (cols, rows)
)


# Display images

cv2.imshow("Original Image", image)

cv2.imshow(
    "Affine Transformed Image",
    affine_image
)


# Save output

cv2.imwrite(
    os.path.join(save_folder, "affine_image.jpg"),
    affine_image
)


print("Affine Transformation completed!")
print("Image saved in 11th experiment folder")


cv2.waitKey(0)
cv2.destroyAllWindows()