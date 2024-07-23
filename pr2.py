import cv2
import numpy as np

# Step 1: Image Preprocessing
image = cv2.imread('Image.jpeg', cv2.IMREAD_GRAYSCALE)
#desired_width = 400  # Example desired width
#desired_height = 400  # Example desired height
#image = cv2.resize(image, (desired_width, desired_height))

# Step 2: Image Segmentation
_, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

# Step 3: Feature Extraction
square_size = 20  # Example size of each square in pixels
height, width = binary_image.shape
bitmap = np.zeros((height // square_size, width // square_size), dtype=int)

for i in range(0, height, square_size):
    for j in range(0, width, square_size):
        square = binary_image[i:i+square_size, j+j+square_size]
        if np.mean(square) < 128:
            bitmap[i // square_size, j // square_size] = 1
        else:
            bitmap[i // square_size, j // square_size] = 0

# Step 4: Print the Result
print("Bitmap array:")
print(bitmap)
