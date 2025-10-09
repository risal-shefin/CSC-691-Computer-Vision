import numpy as np

SOBEL_FILTER_H = np.array([[-1, -2, -1],
                           [0, 0, 0],
                           [1, 2, 1]])
SOBEL_FILTER_V = np.array([[-1, 0, 1],
                           [-2, 0, 2],
                           [-1, 0, 1]])

def apply_convolution(image, filter):
    # Get dimensions
    image_height, image_width = image.shape
    filter_height, filter_width = filter.shape
    pad_h, pad_w = filter_height // 2, filter_width // 2

    # Pad the image to handle boundary cases
    padded_image = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)))
    output = np.zeros_like(image, dtype=np.float32)

    # Perform convolution
    for i in range(image_height):
        for j in range(image_width):
            region = padded_image[i:i+filter_height, j:j+filter_width]
            output[i, j] = np.sum(region * filter)

    return output

def calculate_gradient(img):
    grad_x = apply_convolution(img, SOBEL_FILTER_H)
    grad_y = apply_convolution(img, SOBEL_FILTER_V)
    gradient_magnitude = np.sqrt(grad_x**2 + grad_y**2)
    gradient_angle = np.arctan2(grad_y, grad_x)
    # Normalize angle to [0, 2π]
    gradient_angle = np.where(gradient_angle < 0, gradient_angle + 2 * np.pi, gradient_angle)
    return gradient_magnitude, gradient_angle
