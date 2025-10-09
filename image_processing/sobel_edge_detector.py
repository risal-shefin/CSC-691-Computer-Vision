from calculate_gradient import calculate_gradient
import numpy as np

def sobel_edge_detector(img, threshold):
    # calculate_gradient uses sobel filters to compute the gradient magnitude and angle
    gradient_magnitude, _ = calculate_gradient(img)

    # Apply binary threshold
    binary_edge_map = np.where(gradient_magnitude > threshold, 255, 0)

    return binary_edge_map.astype(np.uint8)
