# Python Libraries
import pyaudio as p
import numpy as np
import os
import matplotlib.pyplot as plt
import keyboard as k
import threading as t

# Algorithm
from algorithm import destructive_wave, get_frequency_amplitude
from time import sleep

# Ignore Warnings
import warnings
import matplotlib
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)

# Constants
CHUNK = 1024
RATE = 44100
FORMAT = p.paInt16


class SoundData:

    # Add in necessary parameters
    def __init__(self, pitch, amplitude):
        pass

class AudioListener:

    data = [] # A list containing the last 10 chunk readings at all times
    listener = p.PyAudio()
    canceling_sound: SoundData = None

    def listen(self):
        ############ Matplotlib Chart Setup ############
        
        plt.ion() # Interactive mode on

        fig, (ax1, ax2) = plt.subplots(2)
        ax1.set_title("Frequency")
        ax2.set_title("Amplitude")
        
        ############ Matplotlib Chart Setup ############

        # Start Stream
        stream = self.listener.open(
            rate=RATE,
            channels=1,
            format=FORMAT,
            input=True,
            frames_per_buffer=CHUNK
        )

        print("Start recording... (press 'e' to exit)")

        while True:
            # Re-set sample file data
            
            # Terminate if user presses enter
            '''
            if k.is_pressed("e"):
                # Stop stream and terminate channel
                stream.stop_stream()
                stream.close()
                self.listener.terminate()
                # Close and remove audio file
                wf.close()
                os.remove("sample.wav")
                # Terminate Program
                exit(0)
            '''

            # Read chunk
            iteration = stream.read(CHUNK, exception_on_overflow=False)
            self.data.append(iteration)

            # Remove first data if data length is 50
            if len(self.data) >= 50:
                self.data.pop(0)

            # Create Destructive Wave if len(data) > 10
            if len(self.data) > 10:
                # Get frequency and amplitude
                freq_list, amp_list = get_frequency_amplitude(self.data)
                t_audio = (CHUNK * len(freq_list)) / RATE
                t_spectrum = np.linspace(0, t_audio, num=len(freq_list))
                # Debug
                #print(f"\n\nFrequency: {np.sum(freq_list)/len(freq_list)}") # Get average frequency of self.data
                #print(f"Amplitude: {np.sum(amp_list)/len(amp_list)}\n\n") # Get average amplitude of self.data
                print(len(freq_list), len(amp_list), len(t_spectrum))
                # Update Charts
                ax1.plot(t_spectrum, freq_list, color = 'b')
                ax2.plot(t_spectrum, amp_list, color = 'r')
                fig.canvas.draw()
                fig.canvas.flush_events()
                plt.pause(0.05)
                # Put in parameters and return destructive wave data
                destructive_wave(self.data)
                
            
            # Here thread noise_cancel
            # t.Thread(self.noise_cancel)

            # Sleep between iteration (Optional)
            #sleep(.1)


    def noise_cancel(self):
        # Play the canceling sound wave (thread function)
        while True:
            if self.canceling_sound != None:
                pass



if __name__ == "__main__":
    audio_listener = AudioListener()
    audio_listener.listen()