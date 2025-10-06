## Exercise 1: Reverse Engineering 2D Transformations
In the given transformed image, we can observe that all the parallel lines in the input image remain parallel. So, we can apply `Affine Transformation`. To apply the affine transformation using `OpenCV`, we need three points from the input image and their corresponding locations in the output image. For that, we can utilize the approximate center coordinates of the red-colored rectangle, circle, and hexagon in the given images. The following figure shows the output with this approach:
<img width="1025" height="344" alt="image" src="https://github.com/user-attachments/assets/cb21caa4-d193-4415-b192-b1fb808ee72d" />

## Exercise 2: Thin Lens Law and F-Number Plots
The figure below presents the plot of lens-to-image distance $z_i$ as a function of object distance $z_o$ for four different focal lengths $f$.
<img width="590" height="481" alt="image" src="https://github.com/user-attachments/assets/6d094f2d-3edb-403a-862d-cf470d56d431" /> <br>
The plot shows that the lens-to-image distance decreases as the object distance increases, and eventually the reduction reaches a saturation point. At this stage, objects at infinity can be projected without adjusting the sensor position. Another notable point is that the lens-to-image distance becomes shorter when the focal length is smaller.

The figure below presents the plot of the aperture diameter ($D$) as a function of the focal length ($f$) for several popular f-numbers:
<img width="595" height="479" alt="image" src="https://github.com/user-attachments/assets/a0a09285-401e-410f-8b8e-9bcc33c214c9" /> <br>
We can observe from the plot that the lower the f-number, the higher the aperture, and the aperture increases with the increment of the focal length for a fixed f-number. <br>
The following are the aperture diameters (D = f/f#) for each given lens of the exercise in order to achieve their stated maximum f-number: <br>
i. f=24mm, f# = 1.4. So, D = 24/1.4 = 17.14mm <br>
ii. f=50mm, f#=1.8. So, D = 50/1.8 = 27.78mm <br>
iii. f=70-200mm, f#=2.8. For, f = 70mm, D = 70/2.8 = 25mm. For f=200mm, D = 200/2.8 = 71.43mm. So, the aperture range will be = 25-71.43mm. <br>
iv. f=400mm, f#=2.8. So, D = 400/2.8 = 142.86mm. <br>
v. f=600mm, f#4.0. So, D = 600/4.0 = 150mm. <br>

## Exercise 3: Sampling and Quantization
The following plot shows the original, sampled, and quantized signals:
<img width="1019" height="435" alt="image" src="https://github.com/user-attachments/assets/18d08e3b-0518-4385-a170-36ee9676b08b" /> <br>
We can observe significant data loss in the sampled and quantized signals with respect to the original signal. <br>

To find a reasonable sampling frequency to capture the true shape of the signal, let's think of the Nyquist-Shannon Theorem at first. The theorem states that the sampling frequency must be at least twice the highest spatial frequency. The given signal's frequency is 5Hz. So, according to the Nyquist-Shannon Theorem, the sampling frequency must be at least $2\times 5 = 10$ Hz. Now, if we observe the original signal from the beginning, the sinusoidal curve reaches the maximum once, the minimum once, and zero twice in one cycle. These four stages of each cycle are needed to capture the true shape of the signal. Since the signal frequency is = 5 and in one cycle, there are four stages, the sampling frequency should be at least = $4\times 5 = 20$ Hz. The following plot shows the result with sampling frequency = 20 Hz:
<img width="1024" height="433" alt="image" src="https://github.com/user-attachments/assets/ec0a82ac-fa8f-451d-a566-9e7595ba7eb4" /> <br>
We can observe significant improvement and true shape capturing here. <br>
To minimize errors, the sampling frequency should be increased. A higher sampling rate reduces aliasing and better preserves the original signal’s shape. Similarly, reducing quantization error requires increasing the number of quantization levels. With too few levels, the quantized values cannot represent the signal accurately, leading to larger errors.

## Exercise 4: Noise and error analysis
The following plot shows the noisy signal and the corresponding sampled and quantized signals:
<img width="1012" height="442" alt="image" src="https://github.com/user-attachments/assets/520d3b6c-5f33-44bb-8d71-6128913e8b17" /> <br>
In all signals, we can observe significant distortions compared to the signals in our previous exercise. The following are the error metrics comparing the noisy continuous signal with the original continuous signal:
- Mean Squared Error (MSE): 0.039156
- Root Mean Squared Error (RMSE): 0.197880
- Peak Signal-to-Noise Ratio (PSNR): 14.07 dB
