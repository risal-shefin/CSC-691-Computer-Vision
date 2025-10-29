The `blob_detection.ipynb` contains the necessary code for this assignment.

### Part 1: Blob Detection
The following image shows the blobs detected by SIFT: <br>
<img width="40%" alt="image" src="https://github.com/user-attachments/assets/235ef4be-b4c9-485b-84ce-4aa4077d9a6d" />
<br>
We can see that, in most cases, larger circles correspond to larger blobs, while smaller circles correspond to smaller blobs, which is the expected behavior.
However, there are also some circles that do not align perfectly with any blob, a few span across multiple blobs, and others fail to cover an entire blob. Also, some blobs remain undetected.
These discrepancies occur due to the limitations and approximations in the SIFT algorithm. The probable reasons can be overlapping keypoints, discretization errors, imperfect scale selection, etc.

## Part 2: Tuning blob detection performance
From Part 1, we can observe that some low-contrast blobs near the top of the image were not detected by SIFT.
To capture these, we can lower the contrast threshold, which allows SIFT to detect keypoints in regions with less intensity variation.
However, this also increases the chance of detecting noisy or irrelevant points (false positives).
To mitigate this, we can lower the edge threshold, which helps filter out more features that are more edge-like than blob-like. <br>
After some experimentation, using `contrastThreshold = 0.01` and `edgeThreshold = 8` produced a good balance between sensitivity and reliability.
The following image shows the results obtained with this configuration. <br>
<img width="40%" alt="image" src="https://github.com/user-attachments/assets/0bee86a3-3577-4ac7-b559-f86766f86fc1" /> <br>
The number of detected keypoints is 551, which is higher than the part 1. Let's compare side by side this result with the previous one, consisting of 387 key points: <br>
<p align="center">
  <img src="https://github.com/user-attachments/assets/235ef4be-b4c9-485b-84ce-4aa4077d9a6d" alt="Before" width="40%"/>
  <img src="https://github.com/user-attachments/assets/0bee86a3-3577-4ac7-b559-f86766f86fc1" alt="After" width="40%"/>
</p>
It can be observed that the right image detects more circles overall. However, it also includes many small circles in regions without clear blobs - these are noisy detections resulting from the lower contrast threshold.
The edge threshold helps suppress some of this noise, but not all of it. <br>
An interesting observation is that a few circles present in the bottom area of the left image are missing in the right image.
This occurs because the edge threshold is more restrictive now, causing certain features to be discarded as edge-like rather than blob-like.

## Part 3: Descriptors
A SIFT descriptor is a 128-dimensional feature vector that contains the appearance of the region around a keypoint detected by the SIFT algorithm. To compute the descriptor, a region (typically 16x16 pixels) centered on the keypoint is divided into 16 smaller subregions arranged in a 4×4 grid. For each subregion, a histogram of local gradient orientations is calculated, usually with 8 bins representing angles from 0° to 360°. Concatenating these 16 histograms (16 x 8 = 128) produces the final 128-dimensional SIFT descriptor. The following image shows such histograms of a descriptor: <br>
<img width="50%" alt="image" src="https://github.com/user-attachments/assets/d9bcc938-083e-43cc-9781-fa7bb6c66388" /> <br>
It can be observed that many histograms show strong peaks around bins 4-6, indicating that the gradients point mostly around 180° - 315°.
Now let's see the location and orientation of the keypoint corresponding to this descriptor: <br>
<img width="40%" alt="image" src="https://github.com/user-attachments/assets/797fd5c7-5a71-46e1-8622-9f9d7c892edc" /> <br>
The blue point marks the SIFT keypoint at location (25.1, 96.5), and the red arrow's length represents the scale (how large the local patch is), the value of which is around 22.16 pixels. Its orientation represents the dominant gradient direction at that location. The angle is indeed around 315°.

## Part 4: Feature Matching
The following image shows the top 50 matches of the example image and the transformed image: <br>
<img width="60%" alt="image" src="https://github.com/user-attachments/assets/5efe0448-f521-4ad0-81fd-0eeaf7246cbb" /> <br>

## Part 5: SIFT matching with your own images
The following two images show the results of SIFT feature matching using my own captured images: <br>
<img width="30%" alt="image" src="https://github.com/user-attachments/assets/5b369903-5ab9-4bc2-930b-4d05d969d36d" />
<img width="30%" alt="image" src="https://github.com/user-attachments/assets/01f50786-e0b1-4213-9042-fafee32f4107" />
