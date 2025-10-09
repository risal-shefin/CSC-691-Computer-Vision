import cv2
import numpy as np
from calculate_gradient import calculate_gradient
from median_filter import median_filter
import matplotlib.pyplot as plt

# Load an image with salt and pepper noise
img = cv2.imread('images/pyramid_salt_pepper.jpg', cv2.IMREAD_GRAYSCALE)
grad_magnitude, _ = calculate_gradient(img)

# Apply the median filter
filtered_img = median_filter(img)
grad_magnitude_filtered_img = calculate_gradient(filtered_img)

# Plot the gradient magnitudes
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(grad_magnitude, cmap='gray')
plt.title('Gradient Magnitude - Original')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(filtered_img, cmap='gray')
plt.title('Filtered Image')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(grad_magnitude_filtered_img, cmap='gray')
plt.title('Gradient Magnitude - Filtered')
plt.axis('off')

plt.tight_layout()
plt.savefig('gradient_comparison.png', dpi=300, bbox_inches='tight')
plt.show()
