import cv2
import tkinter as tk
from tkinter import filedialog
import os


# 9th experiment folder path
save_folder = r"C:\Users\DELL\OneDrive\Desktop\my work\python learning\9th experiment"


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


# -------- Clockwise Rotation --------

clockwise = cv2.rotate(
    image,
    cv2.ROTATE_90_CLOCKWISE
)


# -------- Counter Clockwise Rotation --------

counter_clockwise = cv2.rotate(
    image,
    cv2.ROTATE_90_COUNTERCLOCKWISE
)


# Display images

cv2.imshow("Original Image", image)

cv2.imshow(
    "Clockwise Rotation",
    clockwise
)

cv2.imshow(
    "Counter Clockwise Rotation",
    counter_clockwise
)


# Save images in 9th experiment folder

cv2.imwrite(
    os.path.join(save_folder, "clockwise_image.jpg"),
    clockwise
)

cv2.imwrite(
    os.path.join(save_folder, "counter_clockwise_image.jpg"),
    counter_clockwise
)


print("Rotation completed successfully!")
print("Images saved in 9th experiment folder")


cv2.waitKey(0)
cv2.destroyAllWindows()