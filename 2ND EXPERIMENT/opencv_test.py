import cv2

# Read the image
img = cv2.imread("2nd.jpg")

# Check whether the image is loaded successfully
if img is None:
    print("Image not found!")
else:
    # Apply Gaussian Blur
    blur = cv2.GaussianBlur(img, (15, 15), 0)

    # Display the original image
    cv2.imshow("Original Image", img)

    # Display the blurred image
    cv2.imshow("Gaussian Blurred Image", blur)

    # Save the blurred image
    cv2.imwrite("blur.jpg", blur)

    print("Blurred image saved successfully!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()