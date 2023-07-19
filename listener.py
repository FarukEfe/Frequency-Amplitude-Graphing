# Python Libraries
import pyaudio as p
import wave as w
import os
import matplotlib.pyplot as plt
import keyboard as k
import threading as t

# Algorithm
from descructiveWave import desctuctive_wave
from time import sleep

# Ignore Warnings
import warnings
import matplotlib
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)

CHUNK = 1024
FORMAT = p.paInt16
RATE = 44100

class SoundData:

    # Add in necessary parameters
    def __init__(self, pitch, amplitude):
        pass

class AudioListener:

    data = []
    listener = p.PyAudio()
    canceling_sound: SoundData = None

    def listen(self):
        # Open sample file
        wf = w.open("sample.wav", "w")
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)

        # Matplotlib Chart Setup
        figure = plt.figure(figsize=(15,5))
        ax = figure.add_subplot(111)
        ax.set_title("Audio Spectrum ")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Signal Wave")
        line1, = ax.plot(0,0,"b-")
        plt.rcParams['interactive'] == True

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
                # Populate sample file
                wf.writeframes(b''.join(self.data))
                # Get frequency, amplitude, and other data needed
                freq = wf.getframerate() # Frequency
                n_samples = wf.getnframes() # Number of Samples
                t_audio = n_samples / freq # Audio Time
                # Update spectrum display
                line1.set_ydata(freq)
                wf.getnframes()
                print(freq)
                figure.canvas.draw()
                figure.canvas.flush_events()
                # Put in parameters and return destructive wave data
                # find_destructive(self.data)
                # Empty the .wav file
                
            
            # Here thread noise_cancel
            # t.Thread(self.noise_cancel)

            # Sleep between iteration
            sleep(0.2)

    def noise_cancel(self):
        # Play the canceling sound wave (thread function)
        while True:
            if self.canceling_sound != None:
                pass



if __name__ == "__main__":
    audio_listener = AudioListener()
    audio_listener.listen()