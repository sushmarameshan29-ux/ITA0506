import cv2
from tkinter import filedialog
import tkinter as tk
import os

# 8th experiment folder path
save_folder = r"C:\Users\DELL\OneDrive\Desktop\my work\python learning\8th experiment"

# Select input image
root = tk.Tk()
root.withdraw()

image_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
)

# Read image
img = cv2.imread(image_path)

if img is None:
    print("Image not found")
    exit()


# -------- Scale Bigger --------

bigger_image = cv2.resize(
    img,
    None,
    fx=2,
    fy=2,
    interpolation=cv2.INTER_LINEAR
)


# -------- Scale Smaller --------

smaller_image = cv2.resize(
    img,
    None,
    fx=0.5,
    fy=0.5,
    interpolation=cv2.INTER_AREA
)


# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Bigger Image", bigger_image)
cv2.imshow("Smaller Image", smaller_image)


# Save inside 8th experiment folder

cv2.imwrite(
    os.path.join(save_folder, "bigger_image.jpg"),
    bigger_image
)

cv2.imwrite(
    os.path.join(save_folder, "smaller_image.jpg"),
    smaller_image
)


print("Images saved successfully in 8th experiment folder!")

cv2.waitKey(0)
cv2.destroyAllWindows()