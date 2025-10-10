# Repository 2: Basic Image Processing

## Exercise 1: Intensity Transformations and Histogram Equalization
Entry Point: `exercise1_main.py` is the entry point of this exercise. <br>
The following figure shows the original image, stretched, and equalized histograms side-by-side. <br>
<img width="3570" height="883" alt="image" src="https://github.com/user-attachments/assets/36a412d6-d24a-43a7-a6f1-3880c68b9a22" />
The original low-contrast image looks grayish having a little variation between dark and bright regions. 
The contrast stretching enhances the overall contrast evenly across the image, and the image appears more natural. 
In the histogram equalized image, some areas appear overly bright or too dark - for example, the sky and sand look extreme. 
This happens because histogram equalization redistributes pixel intensities based on their frequency, grouping many pixels into the same brightness ranges. 
As a result, while overall contrast is enhanced, the image can appear unnatural or harsh in certain areas.

## Exercise 2: Non-Linear Filtering and Edge Detection
Entry point: `exercise2_main.py`. <br>
The following figure shows the comparison of gradient magnitudes between the noisy image and the filtered image. <br>
<img width="3433" height="2369" alt="image" src="https://github.com/user-attachments/assets/b04d402b-39cf-4fce-bf0f-a48911518f14" />
The noisy image contains many isolated black and white pixels. 
When computing the gradient magnitude, these sharp intensity changes between individual noise pixels and their neighbors are falsely detected as edges.
As a result, the gradient magnitude image is filled with random bright spots, representing false high gradients that do not correspond to real object boundaries.<br>
The median filter replaces each pixel with the median of its local neighborhood, effectively removing the isolated salt-and-pepper noise while preserving real edges.
Consequently, when the gradient magnitude is computed, the result now highlights true structural edges (e.g., pyramids, horizon, clouds) instead of noise artifacts.
The overall gradient map becomes cleaner, smoother, and more meaningful.

## Exercise 3: Simple Sobel-based edge detector
Entry point: `exercise3_main.py`. <br>
Original Image: <br>
<img width="481" height="321" alt="image" src="https://github.com/user-attachments/assets/506fea12-df51-4d82-ae30-fac07cb0d25a" /> <br>
The following figure shows the images obtained after applying the Sobel edge detector, the directional edge detector, and the Canny edge detector:
<img width="4470" height="1083" alt="image" src="https://github.com/user-attachments/assets/e2ed2efd-b417-4694-8077-cfc2f9370921" />
We can observe that the image from the directional edge detector looks very noisy. Since this method only prioritized the angle, weak and noisy gradients
also got picked up in this process. If we filter out the small magnitudes (e.g., discarding values having <= 10% of the max magnitude) from the output of the directional edge detector,
we will obtain outputs like the following:
<img width="4470" height="1083" alt="image" src="https://github.com/user-attachments/assets/5584a34b-fc8f-4a2a-9b51-a2ea709cadb7" />
Here, the output of the directional edge detector looks much cleaner. Now, let's discuss the impact of different edge detection methods on the original image. <br>
**Sobel Edge Detection:** The Sobel edge detection method detects edges by computing the gradient magnitude using horizontal and vertical derivatives. It highlights almost all significant transitions in intensity.
As a result, the resultant image looks dense and somewhat noisy. <br>
**Directional Edge Detection**: This filter isolates edges whose gradient direction falls around 45 degrees. As a result, only edges oriented roughly diagonally are visible. Other edges are suppressed. <br>
**Canny Edge Detection:** It combines gradient computation, non-maximum suppression, and hysteresis thresholding. As a result, it is a very robust method for edge detection.
From the above figure, it can be observed that the detected edges obtained by this method are thin, continuous, and less noisy. Unwanted texture and random noise are suppressed, leaving only the most significant boundaries (e.g., the pyramid shapes and horizon).