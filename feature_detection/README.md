### Part 1: Blob Detection
The following image shows the blobs detected by SIFT: <br>
<img width="40%" alt="image" src="https://github.com/user-attachments/assets/235ef4be-b4c9-485b-84ce-4aa4077d9a6d" />
<br>
We can see that, in most cases, larger circles correspond to larger blobs, while smaller circles correspond to smaller blobs, which is the expected behavior.
However, there are also some circles that do not align perfectly with any blob, a few span across multiple blobs, and others fail to cover an entire blob. Also, some blobs remain undetected.
These discrepancies occur due to the limitations and approximations in the SIFT algorithm. The probable reasons can be overlapping keypoints, discretization errors, imperfect scale selection, etc.

## Part 2: Tuning blob detection performance
From Part 1, we can observe that some low-contrast blobs near the top of the image were not detected by SIFT.
To capture these weaker features, we can lower the contrast threshold, which allows SIFT to detect keypoints in regions with less intensity variation.
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