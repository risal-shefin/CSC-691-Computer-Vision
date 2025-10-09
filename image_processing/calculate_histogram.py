import numpy as np

def calculate_histogram(img, bins):
    # Flatten the image to 1D array
    flat_img = img.flatten()

    # Calculate histogram
    counts, bin_edges = np.histogram(flat_img, bins=bins)

    # Calculate normalized histogram (probability distribution)
    dist = counts / np.sum(counts)
    return counts, dist, bin_edges