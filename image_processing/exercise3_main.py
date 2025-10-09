from sobel_edge_detector import sobel_edge_detector
from directional_edge_detector import directional_edge_detector
import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    # Load an image
    img = cv2.imread('images/pyramid.jpg', cv2.IMREAD_GRAYSCALE)

    # Apply Sobel edge detector for gradient magnitude
    sobel_edges = sobel_edge_detector(img, threshold=127)

    # Apply directional edge detector for 45-degree edges
    directional_edges = directional_edge_detector(img, [40, 50])

    # Apply Canny edge detection
    canny_edges = cv2.Canny(img, 100, 200)

    # Display all three images
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(sobel_edges, cmap='gray')
    plt.title('Sobel Edge Detection')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(directional_edges, cmap='gray')
    plt.title('Directional Edge Detection (45°)')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(canny_edges, cmap='gray')
    plt.title('Canny Edge Detection')
    plt.axis('off')

    plt.tight_layout()
    plt.savefig('edge_detection_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    main()
