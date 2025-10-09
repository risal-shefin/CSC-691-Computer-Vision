import numpy as np

def median_filter(img, size=3):
    height, width = img.shape
    filtered_img = np.zeros_like(img)
    
    # Calculate padding
    pad = size // 2
    
    # Pad the image to handle borders
    padded_img = np.pad(img, pad)
    
    # Apply median filter
    for i in range(height):
        for j in range(width):
            # Extract neighborhood window
            window = padded_img[i:i+size, j:j+size]
            # Flatten, sort, and find median
            sorted_values = np.sort(window.flatten())
            median_value = sorted_values[len(sorted_values) // 2]
            filtered_img[i, j] = median_value
    
    return filtered_img