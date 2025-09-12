import numpy as np
import matplotlib.pyplot as plt
import sampling_quantization

signal_freq = 5.0 # in Hz
duration = 2 # in seconds
sampling_freq = 8 # in Hz
num_bits = 3 # 3-bit quantization (8 levels: 0 - 7)
min_signal = -1 # min signal value
max_signal = 1 # max signal value
mean = 0
std_dev = 0.1 # noise level

def add_Gaussian_noise(signal, mean, std):
    mag = np.max(signal) - np.min(signal) # magnitude of the signal
    noise = np.random.normal(mean, std * mag, len(signal))
    return signal + noise

def get_noisy_signal(t):    # returns noisy signal by adding Gaussian noise
    signal = sampling_quantization.original_signal(t)
    noisy_signal = add_Gaussian_noise(signal, mean, std_dev)
    return noisy_signal

plt.subplots(1, 1, figsize=(12, 5))

t_points = np.linspace(0, duration, 1000, endpoint=False) # 1000 points in [0, duration)
cont_signal = get_noisy_signal(t_points)
plt.plot(t_points, cont_signal, label='continuous signal')

n = int(sampling_freq * duration)   # count of sampled points
t_sampled = np.linspace(0, duration, n, endpoint=False) # the n sampled points in [0, duration)
sampled_signal = get_noisy_signal(t_sampled)
plt.plot(t_sampled, sampled_signal, label='sampled signal')

num_levels = 2**num_bits    # count of level = 2^num_bits 
qs = np.round((sampled_signal - min_signal) / (max_signal - min_signal) * (num_levels - 1)) # quantized signal levels
qv = min_signal + qs * (max_signal - min_signal) / (num_levels - 1) # quantized signal values
plt.step(t_sampled, qv, where='post', label=f'Quantized Signal ({num_bits} bits)', color='r', linestyle='--')

# Error Calculation
print("Computing Errors...")
base_cont_signal = sampling_quantization.original_signal(t_points)  # original continuous signal (without noise)
mse = np.mean((base_cont_signal - cont_signal) ** 2)
rmse = np.sqrt(mse)
psnr = 10 * np.log10((max_signal ** 2) / mse)
print(f'Mean Squared Error (MSE): {mse:.6f}')
print(f'Root Mean Squared Error (RMSE): {rmse:.6f}')
print(f'Peak Signal-to-Noise Ratio (PSNR): {psnr:.2f} dB')

plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.show()
