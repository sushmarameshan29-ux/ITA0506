import cv2
import os

# Change the working directory to the folder where this script is saved
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Read the image
img = cv2.imread("image.jpg")

# Check if the image is loaded
if img is None:
    print("Image not found!")
else:
    # Create a kernel (3x3 matrix)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    # Dilate the image
    dilated = cv2.dilate(img, kernel, iterations=1)

    # Display the original image
    cv2.imshow("Original Image", img)

    # Display the dilated image
    cv2.imshow("Dilated Image", dilated)

    # Save the output image
    cv2.imwrite("dilated_result.jpg", dilated)

    print("Dilated image saved successfully!")

    # Wait until a key is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()