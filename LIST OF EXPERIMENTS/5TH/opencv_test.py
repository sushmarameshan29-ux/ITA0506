import cv2
import os

# Set the current working directory to the script's folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Read the image
img = cv2.imread("image.jpg")

# Check if the image is loaded
if img is None:
    print("Image not found!")
else:
    # Create a 3x3 kernel
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    # Erode the image
    eroded = cv2.erode(img, kernel, iterations=1)

    # Display the original image
    cv2.imshow("Original Image", img)

    # Display the eroded image
    cv2.imshow("Eroded Image", eroded)

    # Save the output image
    cv2.imwrite("eroded_result.jpg", eroded)

    print("Eroded image saved successfully!")

    # Wait until a key is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()