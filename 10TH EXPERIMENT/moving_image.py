import cv2
import tkinter as tk
from tkinter import filedialog
import os


# 10th experiment folder path
save_folder = r"C:\Users\DELL\OneDrive\Desktop\my work\python learning\10th experiment"


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


# -------- Move image to right --------

x = 100   # pixels moved right
y = 50    # pixels moved down

matrix_right = cv2.getRotationMatrix2D(
    (0,0),
    0,
    1
)

matrix_right[0,2] = x
matrix_right[1,2] = y


moved_right = cv2.warpAffine(
    image,
    matrix_right,
    (cols, rows)
)


# -------- Move image to left --------

x = -100
y = -50

matrix_left = cv2.getRotationMatrix2D(
    (0,0),
    0,
    1
)

matrix_left[0,2] = x
matrix_left[1,2] = y


moved_left = cv2.warpAffine(
    image,
    matrix_left,
    (cols, rows)
)


# Display results

cv2.imshow("Original Image", image)

cv2.imshow(
    "Moved Right and Down",
    moved_right
)

cv2.imshow(
    "Moved Left and Up",
    moved_left
)


# Save results in experiment folder

cv2.imwrite(
    os.path.join(save_folder, "moved_right_image.jpg"),
    moved_right
)

cv2.imwrite(
    os.path.join(save_folder, "moved_left_image.jpg"),
    moved_left
)


print("Image movement completed!")
print("Images saved in 10th experiment folder")


cv2.waitKey(0)
cv2.destroyAllWindows()