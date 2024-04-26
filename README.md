# Frequency & Amplitude w/ Fast Fourier Transform
This project listens to surrounding sounds
The amplitude and frequency computation can all be found in `algorithm.py` file
### Project Setup
Download the project file into your preferred local directory and execute the following commands:
```bash
./modules/Scripts/activate
```
Since the project is set on a virtual environment, this command activates all of the modules installed in the virtual environment
If the project still doesn't run due to missing modules (which is unlikely), you can try manually installing the modules used in the project using pip commands.
For python3:
```bash
pip3 install moduleName
```
For python:
```bash
pip install moduleName
```
Make sure to look up the uninstalled modules from the warning/error messages in `listener.py`

Lastly, make sure to run the program with ```sudo python3 listener.py``` so that the program can access the microphone
### Additional
There's also an experimental algorithm in `algorithm.py` which is meant to generate the destructive wave for the given sound buffer input, however it doesn't as intended.
Maybe I'll get back to this project to fix that later.
