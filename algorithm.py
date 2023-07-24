import numpy as np
import math

def get_frequency_amplitude(data, min_freq=10, max_freq=1500):
    freq_array = []
    amp_array = []
    for d in data:
        # Convert the binary audio data to a NumPy array
        audio_array = np.frombuffer(d, dtype=np.int16)
        
        # Compute the Fast Fourier Transform (FFT) to find the frequency content
        freq_data = np.fft.fft(audio_array)
        magnitudes = np.abs(freq_data)

        # Noisegate to eliminate exteremes
        magnitudes[np.logical_or(magnitudes < min_freq, magnitudes > max_freq)] = min_freq

        # Get frequency
        frequency = np.mean(magnitudes)

        # Calculate the amplitude (peak value) of the audio data
        amplitude = np.max(np.abs(audio_array))

        # Convert to Decibels
        amplitude_decibels = 20 * math.log10(amplitude)

        # Append
        freq_array.append(frequency)
        amp_array.append(amplitude_decibels) 
        
    # Return array if pitch loud enough
    if len(freq_array) != 0:
        return (freq_array, amp_array)



def destructive_wave(frequency, amplitude, duration=np.inf, sample_rate=44100):
    # If under a certain decibel, return None
    if amplitude < 40:
        return None
    
    num_samples = int(duration * sample_rate)

    # Generate a time array for the waveform
    time_array = np.linspace(0, duration, num_samples, endpoint=False)

    # Calculate the angular frequency (omega) based on the desired frequency
    omega = 2 * np.pi * frequency

    # Generate the sound wave using a sine function
    waveform = amplitude * np.sin(omega * time_array)

    return -waveform
