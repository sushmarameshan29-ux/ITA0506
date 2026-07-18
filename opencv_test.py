import cv2

# Read the image
img = cv2.imread("1st.png")

# Check if the image was loaded successfully
if img is None:
    print("Image not found!")
else:
    print("Image loaded successfully!")