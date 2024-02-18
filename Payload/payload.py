import cv2
import numpy as np
def resize_image(img, binning_factor):
    # Get the input image dimensions
    height, width = img.shape[:2]

    # Compute the dimensions of the resized image
    resized_height = (height // binning_factor) * binning_factor
    resized_width = (width // binning_factor) * binning_factor

    # Resize the image
    resized_img = cv2.resize(img, (resized_width, resized_height))
    return resized_img

def pixel_binning(img, binning_factor):
    # Get the input image dimensions
    height, width = img.shape[:2]

    # Compute the dimensions of the binned image
    binned_height = height // binning_factor
    binned_width = width // binning_factor

    # Reshape the image to a 2D array of pixels in each bin
    reshaped_img = img.reshape(binned_height, binning_factor,
                               binned_width, binning_factor, -1)

    # Compute the average for each bin
    binned_img = reshaped_img.mean(axis=(1, 3))

    return binned_img.astype(np.uint8)

# Load the image
img = cv2.imread('clock_tower.jpeg')

# Resize the image
img = resize_image(img, 4)

# Perform pixel binning with a binning factor of 4
binned_img = pixel_binning(img, 4)

# Save the binned image
cv2.imwrite('clock_tower_binned.jpg', binned_img)

