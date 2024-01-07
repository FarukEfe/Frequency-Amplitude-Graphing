# Python Libraries
import pyaudio as p
import numpy as np
import os
import matplotlib.pyplot as plt
import threading as t
from pygame import mixer, sndarray

# Algorithm
from algorithm import get_frequency_amplitude
from time import sleep

# Ignore Warnings
import warnings
import matplotlib
#warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)

# Constants
CHUNK = 1024
RATE = 44100
FORMAT = p.paInt16

class AudioListener:

    data = [] # A list containing the last 10 chunk readings at all times
    listener = p.PyAudio()
    
    def listen(self):
        ############ Matplotlib Chart Setup ############
        
        plt.ion() # Interactive mode on

        fig, (ax1, ax2) = plt.subplots(2, figsize=(8,6))
        plt.xlim(-1,0)
        plt.tight_layout(pad=4)
        ############ Matplotlib Chart Setup ############

        # Start Stream
        stream = self.listener.open(
            rate=RATE,
            channels=1,
            format=FORMAT,
            input=True,
            frames_per_buffer=CHUNK
        )

        print("Start recording...")

        # Lifecycle
        while True:
            # Read chunk
            iteration = stream.read(CHUNK, exception_on_overflow=False)
            self.data.append(iteration)

            # Remove first data if data length is 50
            if len(self.data) >= 50:
                self.data.pop(0)

            # Chart data if length exceeds 10 items
            if len(self.data) > 10:
                # Get frequency and amplitude
                freq_list, amp_list = get_frequency_amplitude(self.data)
                t_audio = (CHUNK * len(freq_list)) / RATE
                t_spectrum = np.linspace(-t_audio, 0, num=len(freq_list))

                ########## Update Charts ##########
                # Clear previous data
                ax1.cla()
                ax2.cla()

                # Reset ylim
                ax1.set_ylim(ymin=0, ymax=1500)
                ax2.set_ylim(ymin=25, ymax=125)
                plt.xlim(-1,0)

                # Addtitle
                ax1.set_xlabel("Time (s)")
                ax1.set_ylabel("Frequency (Hz)")
                ax2.set_xlabel("Time (s)")
                ax2.set_ylabel("Amplitude (Db)")

                # Plot new data
                ax1.plot(t_spectrum, freq_list, color = 'b')
                ax2.plot(t_spectrum, amp_list, color = 'r')
                fig.canvas.draw()

                # Flush events
                fig.canvas.flush_events()
                ########## Update Charts Complete ##########


if __name__ == "__main__":
    audio_listener = AudioListener()
    audio_listener.listen()
