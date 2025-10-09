from calculate_gradient import calculate_gradient
import numpy as np

def directional_edge_detector(img, direction_range):
    # Get gradient magnitude and direction from calculate_gradient
    gradient_mag, gradient_angle = calculate_gradient(img)

    min_angle, max_angle = direction_range
    # Convert angles from degrees to radians
    min_angle = np.radians(min_angle)
    max_angle = np.radians(max_angle)

    # Create binary mask based on direction range
    binary_map = ((gradient_angle >= min_angle) & (gradient_angle <= max_angle)).astype(int)
    # Apply threshold to gradient magnitude and combine with direction filter
    # mag_threshold = 0.1 * np.max(gradient_mag)  # Adjust threshold as needed
    # mag_binary = (gradient_mag > mag_threshold).astype(int)
    # binary_map = binary_map * mag_binary

    return binary_map
