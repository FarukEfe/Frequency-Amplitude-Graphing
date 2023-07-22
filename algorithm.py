import numpy as np
import math

CHUNK = 1024
RATE = 44100

def get_frequency_amplitude(data):
    freq_array = []
    amp_array = []
    for d in data:
        # Convert the binary audio data to a NumPy array
        audio_array = np.frombuffer(d, dtype=np.int16)
        
        # Compute the Fast Fourier Transform (FFT) to find the frequency content
        freq_data = np.fft.fft(audio_array)
        magnitudes = np.abs(freq_data)
        
        # Find the dominant frequency bin (bin with highest magnitude)
        dominant_bin = np.argmax(magnitudes)
        frequency = dominant_bin * RATE / CHUNK
        
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



def destructive_wave(data_points):
    # If under a certain decibel, return None
    # Get frequency, amplitude, etc
    pass