# !/usr/bin/env python3

import os
import tkinter as tk
import warnings
import wave as wv
from datetime import datetime
from tkinter import PhotoImage, messagebox
import tkinter.font as font
import numpy as np
import playsound as ps
import pyaudio
import soundfile as sf
from randomstr import randomstr
from pydub import AudioSegment

warnings.simplefilter("ignore", DeprecationWarning)

# set UI window parameters

app = tk.Tk()
app.geometry("1000x500")
app.title("Voice Modulator")
app.configure(bg='black')

# import and store the button icons

startIcon = PhotoImage(file="mic.png")
stopIcon = PhotoImage(file="stop.png")

# function that deletes generated .wav files

deleteWavFiles = tk.Button(app,
                           text='Delete .wav files',
                           width=15,
                           command=lambda: remove_files())

myFont = font.Font(family='Helvetica', size=11, weight='bold')

# creation and placement of effect buttons

public_place_button = tk.Button(app, text="Public Place", width=9,
                                command=lambda: [ps.playsound(public_place_effect_file)])
public_place_button.place(relx=0.4, rely=0.5, anchor=tk.CENTER)
public_place_button['font'] = myFont
robot_button = tk.Button(app, text="Robot Voice", width=9, command=lambda: [ps.playsound(robot_effect_file)])
robot_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
robot_button['font'] = myFont
helium_button = tk.Button(app, text="Helium", width=9, command=lambda: [ps.playsound(helium_effect_file)])
helium_button.place(relx=0.6, rely=0.5, anchor=tk.CENTER)
helium_button['font'] = myFont
echo_button = tk.Button(app, text="Echo", width=9, command=lambda: [ps.playsound(echo_effect_file)])
echo_button.place(relx=0.4, rely=0.6, anchor=tk.CENTER)
echo_button['font'] = myFont
chipmunk_button = tk.Button(app, text="Chipmunk", width=9, command=lambda: [ps.playsound(chipmunk_effect_file)])
chipmunk_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
chipmunk_button['font'] = myFont
slowmo_button = tk.Button(app, text="Slow-Mo", width=9, command=lambda: [ps.playsound(slowmo_effect_file)])
slowmo_button.place(relx=0.6, rely=0.6, anchor=tk.CENTER)
slowmo_button['font'] = myFont
reverse_button = tk.Button(app, text="Reverse", width=9, command=lambda: [ps.playsound(reverse_effect_file)])
reverse_button.place(relx=0.4, rely=0.7, anchor=tk.CENTER)
reverse_button['font'] = myFont
rain_button = tk.Button(app, text="Rain", width=9, command=lambda: [ps.playsound(rain_effect_file)])
rain_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
rain_button['font'] = myFont
regular_button = tk.Button(app, text="No effect", width=9, command=lambda: [ps.playsound(regular_effect_file)])
regular_button.place(relx=0.6, rely=0.7, anchor=tk.CENTER)
regular_button['font'] = myFont

# disable the effect buttons when initially running the app

public_place_button['state'] = 'disabled'
robot_button['state'] = 'disabled'
helium_button['state'] = 'disabled'
echo_button['state'] = 'disabled'
chipmunk_button['state'] = 'disabled'
slowmo_button['state'] = 'disabled'
reverse_button['state'] = 'disabled'
rain_button['state'] = 'disabled'
regular_button['state'] = 'disabled'

deleteWavFiles['state'] = 'normal'

public_place_effect_file = ''
robot_effect_file = ''
helium_effect_file = ''
echo_effect_file = ''
chipmunk_effect_file = ''
slowmo_effect_file = ''
reverse_effect_file = ''
rain_effect_file = ''
regular_effect_file = ''


def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print(filename + ' DNE')


# public effect

def public_effect(filename):
    data, fs = sf.read(filename)
    public, rfs = sf.read('public.wav')
    output = [0] * len(data)
    public_len = len(public)

    for i in range(0, len(data)):
        output[i] = data[i][0] + .25 * public[i % public_len][0]

    global public_place_effect_file
    public_place_effect_file = randomstr(length=10) + '.wav'
    sf.write(public_place_effect_file, output, fs)


# robot effect

def robot_effect(filename):
    global robot_effect_file
    robot_effect_file = randomstr(length=10) + '.wav'
    shift = 2500 // 100
    pitch_shift(filename, robot_effect_file, shift)


# helium effect

def helium_effect(filename):
    global helium_effect_file
    helium_effect_file = randomstr(length=10) + '.wav'
    shift = 6000 // 150
    pitch_shift(filename, helium_effect_file, shift)


# echo effect

def echo_effect(filename):
    data, fs = sf.read(filename)
    delay = .25
    gain = .75
    global echo_effect_file
    echo_effect_file = randomstr(length=10) + '.wav'

    delay_index = int(delay * fs)
    output = [0] * len(data)

    for i in range(0, len(data)):
        output[i] = data[i][0] + gain * data[i - delay_index][0]

    # print(output)
    sf.write(echo_effect_file, output, fs)


# chipmunk effect

def chipmunk_effect(filename):
    CHANNELS = 1
    SWIDTH = 2
    Change_RATE = 3.2

    spf = wv.open(filename, 'rb')
    RATE = spf.getframerate()
    signal = spf.readframes(-1)

    global chipmunk_effect_file
    chipmunk_effect_file = randomstr(length=10) + '.wav'

    wf = wv.open(chipmunk_effect_file, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(SWIDTH)
    wf.setframerate(RATE * Change_RATE)
    wf.writeframes(signal)
    wf.close()


# slow motion effect

def slowmo_effect(filename):
    CHANNELS = 1
    SWIDTH = 2
    Change_RATE = 1.5

    spf = wv.open(filename, 'rb')
    RATE = spf.getframerate()
    signal = spf.readframes(-1)
    global slowmo_effect_file
    slowmo_effect_file = randomstr(length=10) + '.wav'

    wf = wv.open(slowmo_effect_file, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(SWIDTH)
    wf.setframerate(RATE * Change_RATE)
    wf.writeframes(signal)
    wf.close()


# reverse audio effect

def reverse_effect(filename):
    loop = AudioSegment.from_wav(filename)
    reversed = loop.reverse()
    global reverse_effect_file
    reverse_effect_file = randomstr(length=10) + '.wav'
    reversed.export(reverse_effect_file, format="wav")


counter = 28800
running = False


# rain effect

def rain_effect(filename):
    data, fs = sf.read(filename)
    rain, rfs = sf.read('rain.wav')
    output = [0] * len(data)
    rain_len = len(rain)

    for i in range(0, len(data)):
        output[i] = data[i][0] + .1 * rain[i % rain_len][0]

    global rain_effect_file
    rain_effect_file = randomstr(length=10) + '.wav'
    sf.write(rain_effect_file, output, fs)


# label that holds the timer

def counter_label(label):
    def count():
        if running:
            global counter

            # To manage the initial delay.
            if counter == 28800:
                display = "Starting..."
            else:
                tt = datetime.fromtimestamp(counter)
                string = tt.strftime("%H:%M:%S")
                display = string

            label['text'] = display

            label.after(1000, count)
            counter += 1

    # Triggering the start of the counter.
    count()


# start function of the stopwatch

def start(label):
    global running
    running = True
    counter_label(label)
    startButton['state'] = 'disabled'
    stopButton['state'] = 'normal'


# stop function of the stopwatch

def stop():
    global running
    startButton['state'] = 'normal'
    stopButton['state'] = 'disabled'
    running = False


# reset function of the stopwatch

def reset(label):
    global counter
    counter = 28800

    # If rest is pressed after pressing stop.
    if not running:
        # resetButton['state'] = 'disabled'
        label['text'] = '00:00:00'

    # If reset is pressed while the stopwatch is running.
    else:
        label['text'] = 'Starting...'


# stopwatch label

label = tk.Label(app, text="00:00:00", fg="white",
                 font="Verdana 60 bold", bg="black")

st = 0


# record voice function

def start_record():
    # reset the timer
    reset(label)
    # start the timer
    start(label)
    deleteWavFiles['state'] = 'disabled'
    global st
    st = 1
    global regular_effect_file
    frames = []
    FORMAT = pyaudio.paInt16  # 16 bits per sample
    CHANNELS = 2
    RATE = 44100  # Record at 44100 samples per second
    CHUNK = 3024

    # Create an interface to PortAudio
    p = pyaudio.PyAudio()
    rand_str = randomstr(length=10, charset='alphanumeric', readable=False, capitalization=False)
    filename = rand_str + ".wav"
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    while st == 1:
        data = stream.read(CHUNK)
        frames.append(data)
        print("recording...")
        app.update()

    # Stop and close the stream
    stream.close()

    # Terminate the PortAudio interface
    p.terminate()

    # Save the recorded data as a WAV file
    wf = wv.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    # enable the effect buttons when recording is finished
    public_place_button['state'] = 'normal'
    robot_button['state'] = 'normal'
    helium_button['state'] = 'normal'
    echo_button['state'] = 'normal'
    chipmunk_button['state'] = 'normal'
    slowmo_button['state'] = 'normal'
    reverse_button['state'] = 'normal'
    rain_button['state'] = 'normal'
    regular_button['state'] = 'normal'
    # play the recorded audio
    ps.playsound(filename)

    regular_effect_file = filename
    public_effect(filename)
    robot_effect(filename)
    helium_effect(filename)
    echo_effect(filename)
    chipmunk_effect(filename)
    slowmo_effect(filename)
    reverse_effect(filename)
    rain_effect(filename)


def stop_record():
    # stop the timer
    stop()
    global st
    st = 0


# creation of start listening, stop listening, and reset buttons

startButton = tk.Button(app,
                        command=lambda: [start_record()],
                        image=startIcon,
                        bg="black",
                        activebackground="black",
                        borderwidth=0)
stopButton = tk.Button(app,
                       command=lambda: [stop_record()],
                       image=stopIcon,
                       bg="black",
                       activebackground="black",
                       borderwidth=0)

# placement of stopwatch label

label.pack(side=tk.TOP)

# placement of start listening, stop listening, and reset buttons

startButton.pack(side=tk.LEFT)
stopButton.pack(side=tk.RIGHT)
deleteWavFiles.pack(side=tk.BOTTOM)


def pitch_shift(filename, output, shift):
    wr = wv.open(filename, 'r')
    ww = wv.open(output, 'w')

    par = list(wr.getparams())
    ww.setparams(par)

    frame_per_sec = wr.getframerate() // 20
    file_sz = int(wr.getnframes() / frame_per_sec)

    for num in range(file_sz):
        data = np.fromstring(wr.readframes(frame_per_sec), dtype=np.int16)
        left = data[0::2]
        right = data[1::2]
        # Take DFT
        left_freq = np.fft.rfft(left)
        right_freq = np.fft.rfft(right)
        # Scale It Up or Down
        left_freq = np.roll(left_freq, shift)
        right_freq = np.roll(right_freq, shift)
        left_freq[0:shift] = 0
        right_freq[0:shift] = 0
        # Take inverse DFT
        left = np.fft.irfft(left_freq)
        right = np.fft.irfft(right_freq)
        # Put it altogether
        sig = np.column_stack((left, right)).ravel().astype(np.int16)
        ww.writeframes(sig)

    wr.close()
    ww.close()


def remove_files():
    MsgBox = tk.messagebox.askquestion('Delete .wav files',
                                       'Are you sure you want to delte the .wav files in the current directory?',
                                       icon='warning')
    if MsgBox == 'yes':
        directory = os.getcwd()

        files_in_directory = os.listdir(directory)
        filtered_files = [file for file in files_in_directory if
                          file.endswith(".wav") and file != 'public.wav' and file != 'rain.wav']
        for file in filtered_files:
            path_to_file = os.path.join(directory, file)
            os.remove(path_to_file)
    else:
        tk.messagebox.showinfo('Voice Modulator', 'No .wav files were deleted')


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        app.destroy()


app.protocol("WM_DELETE_WINDOW", on_closing)

app.mainloop()
