from calculate_histogram import calculate_histogram
import numpy as np

def equalize_histogram(img):
    r_min = np.min(img)
    r_max = np.max(img)
    bin_count = 32   # number of bins for histogram
    bin_size = (r_max - r_min + 1) // bin_count  # size of each bin
    counts, dist, bin_edges = calculate_histogram(img, bins=bin_count)
    cdf = dist.cumsum()  # cumulative distribution function
    new_img = np.zeros_like(img)
    # Map each pixel value to its equalized value using the CDF
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            old_value = img[i, j]
            # Find the bin index for the current pixel value using bin edges
            bin_index = np.digitize(old_value, bin_edges)
            bin_index = np.clip(bin_index, 0, len(cdf) - 1)
            # Map to new value using CDF (scale to 0-255 range)
            new_img[i, j] = int(cdf[bin_index] * 255)
    return new_img