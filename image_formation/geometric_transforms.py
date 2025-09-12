import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('images/original_image.jpg')
print(f'Image shape: {img.shape}')
rows, cols, ch = img.shape

print('Applying Affine Transformation...')
# Near the center points of the rectangle, circle and hexagon of the original image
pts1 = np.float32([[175, 175], [175, 1000], [1000, 175]])
# Near the center points of the rectangle, circle and hexagon of the transformed image
pts2 = np.float32([[455, 300], [785, 1140], [870, 590]])
M = cv.getAffineTransform(pts1,pts2)
output_img = cv.warpAffine(img,M,(cols,rows))

img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
output_img_rgb = cv.cvtColor(output_img, cv.COLOR_BGR2RGB)
transformed_img_rgb = cv.cvtColor(cv.imread('images/transformed_image.jpg'), cv.COLOR_BGR2RGB)
plt.figure(figsize=(12,6))
plt.subplot(131),plt.imshow(img_rgb),plt.title('Original Image')
plt.subplot(132),plt.imshow(transformed_img_rgb),plt.title('Transformed Image')
plt.subplot(133),plt.imshow(output_img_rgb),plt.title('Reverse-Engineered Transformed Image')
plt.show()