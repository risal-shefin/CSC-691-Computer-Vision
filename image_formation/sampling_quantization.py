import numpy as np
import matplotlib.pyplot as plt

signal_freq = 5.0 # in Hz
duration = 2 # in seconds
sampling_freq = 8 # in Hz
num_bits = 3 # 3-bit quantization (8 levels: 0 - 7)
min_signal = -1 # min signal value
max_signal = 1 # max signal value

def original_signal(t):
    return np.sin(2 * np.pi * signal_freq * t)

plt.subplots(1, 1, figsize=(12, 5))

t_points = np.linspace(0, duration, 1000, endpoint=False) # 1000 points in [0, duration)
cont_signal = original_signal(t_points)
plt.plot(t_points, cont_signal, label='continuous signal')

n = int(sampling_freq * duration)
t_sampled = np.linspace(0, duration, n, endpoint=False)
sampled_signal = original_signal(t_sampled)
plt.plot(t_sampled, sampled_signal, label='sampled signal')

qs = np.round((sampled_signal - min_signal) / (max_signal - min_signal) * (num_bits - 1))
qv = min_signal + qs * (max_signal - min_signal) / (num_bits - 1)
plt.step(t_sampled, qv, where='post', label=f'Quantized Signal ({num_bits} bits)', color='r', linestyle='--')

plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.show()