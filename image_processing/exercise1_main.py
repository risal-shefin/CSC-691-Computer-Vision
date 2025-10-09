import cv2
import numpy as np
import matplotlib.pyplot as plt
from equalize_histogram import equalize_histogram
from contrast_stretch import contrast_stretch

def plot_images(original_img, contrast_stretched_img, histogram_equalized_img):
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 3, 1)
    plt.imshow(original_img, cmap='gray', vmin=0, vmax=255)
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(contrast_stretched_img, cmap='gray', vmin=0, vmax=255)
    plt.title('Contrast Stretched Image')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(histogram_equalized_img, cmap='gray', vmin=0, vmax=255)
    plt.title('Histogram Equalized Image')
    plt.axis('off')

    plt.tight_layout()
    plt.savefig('intensity_transform_hist_comparison_plot.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    # Read image
    img = cv2.imread('images/pyramid_low_contrast.jpg', cv2.IMREAD_GRAYSCALE)

    # Get min and max values from the image
    r_min = np.min(img)
    r_max = np.max(img)
    print(f"Min pixel value: {r_min}, Max pixel value: {r_max}")
    # Apply contrast stretching
    stretched_img = contrast_stretch(img, r_min, r_max)

    # Apply histogram equalization for comparison
    equalized_img = equalize_histogram(img)
    # equalized_img = cv2.equalizeHist(img)
    # Save the stretched image
    # cv2.imwrite('images/pyramid_stretched.jpg', stretched_img.astype(np.uint8))

    # Plot original, stretched, and equalized images
    plot_images(img, stretched_img, equalized_img)