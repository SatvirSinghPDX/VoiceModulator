#!/usr/bin/env python3

import tkinter as tk
import tkinter.font as tkFont
import wave
from tkinter import PhotoImage
from datetime import datetime
import numpy as np
import playsound as ps
import wave as wv
import soundfile as sf
import pyaudio
import os

# set UI window parameters

app = tk.Tk()
app.geometry("600x400")
app.title("Voice Modulator")
app.configure(bg='black')

# import and store the button icons

startIcon = PhotoImage(file="mic.png")
stopIcon = PhotoImage(file="stop.png")


def effect_1():
    wr = wv.open('output.wav', 'r')
    ww = wv.open('effect1.wav', 'w')

    par = list(wr.getparams())
    ww.setparams(par)

    frame_per_sec = wr.getframerate() // 20
    file_sz = int(wr.getnframes() / frame_per_sec)
    shift = 100 // 20

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
        ww.writeframes(sig.tostring())

    wr.close()
    ww.close()


def effect_2():
    wr = wv.open('output.wav', 'r')
    ww = wv.open('effect2.wav', 'w')

    par = list(wr.getparams())
    ww.setparams(par)

    frame_per_sec = wr.getframerate() // 20
    file_sz = int(wr.getnframes() / frame_per_sec)
    shift = 1000 // 100

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
        ww.writeframes(sig.tostring())

    wr.close()
    ww.close()


def effect_3():
    wr = wv.open('output.wav', 'r')
    ww = wv.open('effect3.wav', 'w')

    par = list(wr.getparams())
    ww.setparams(par)

    frame_per_sec = wr.getframerate() // 20
    file_sz = int(wr.getnframes() / frame_per_sec)
    shift = 4000 // 150

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
        ww.writeframes(sig.tostring())

    wr.close()
    ww.close()


def effect_4():
    data, fs = sf.read('output.wav')
    delay = .25
    gain = .75

    delay_index = int(delay * fs)
    output = [0] * len(data)

    for i in range(0, len(data)):
        output[i] = data[i][0] + gain * data[i - delay_index][0]

    print(output)
    sf.write('effect4.wav', output, fs)


def effect_5():
    CHANNELS = 1
    SWIDTH = 2
    Change_RATE = 3.2

    spf = wv.open('output.wav', 'rb')
    RATE = spf.getframerate()
    signal = spf.readframes(-1)

    wf = wv.open('effect5.wav', 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(SWIDTH)
    wf.setframerate(RATE * Change_RATE)
    wf.writeframes(signal)
    wf.close()


counter = 28800
running = False


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

def Start(label):
    global running
    running = True
    counter_label(label)
    startButton['state'] = 'disabled'
    stopButton['state'] = 'normal'


# Stop function of the stopwatch

def Stop():
    global running
    startButton['state'] = 'normal'
    stopButton['state'] = 'disabled'
    running = False


# Reset function of the stopwatch

def Reset(label):
    global counter
    counter = 28800

    # If rest is pressed after pressing stop.
    if not running:
        resetButton['state'] = 'disabled'
        label['text'] = '00:00:00'

    # If reset is pressed while the stopwatch is running.
    else:
        label['text'] = 'Starting...'


# stopwatch label

label = tk.Label(app, text="00:00:00", fg="white",
                 font="Verdana 30 bold", bg="black")


# record voice function

def record():
    chunk = 1024
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 5
    filename = "output.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Started listening...')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 5 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Stopped listening.')

    # Save the recorded data as a WAV file
    wf = wv.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    ps.playsound(filename)
    effect_1()
    effect_2()
    effect_3()
    effect_4()
    effect_5()


# creation of start listening, stop listening, and reset buttons

startButton = tk.Button(app,
                        command=lambda: [Start(label), record()],
                        image=startIcon,
                        bg="black",
                        activebackground="black",
                        borderwidth=0)
stopButton = tk.Button(app,
                       command=Stop,
                       image=stopIcon,
                       bg="black",
                       activebackground="black",
                       borderwidth=0)
resetButton = tk.Button(app,
                        text='Reset',
                        width=6,
                        command=lambda: Reset(label))

# creation and placement of effect buttons

effect1 = tk.Button(app, text="Effect 1", command=lambda: [ps.playsound('effect1.wav')])
effect1.place(relx=0.4, rely=0.4, anchor=tk.CENTER)
effect2 = tk.Button(app, text="Effect 2", command=lambda: [ps.playsound('effect2.wav')])
effect2.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
effect3 = tk.Button(app, text="Effect 3", command=lambda: [ps.playsound('effect3.wav')])
effect3.place(relx=0.6, rely=0.4, anchor=tk.CENTER)
effect4 = tk.Button(app, text="Effect 4", command=lambda: [ps.playsound('effect4.wav')])
effect4.place(relx=0.4, rely=0.5, anchor=tk.CENTER)
effect5 = tk.Button(app, text="Effect 5", command=lambda: [ps.playsound('effect5.wav')])
effect5.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
effect6 = tk.Button(app, text="Effect 6")
effect6.place(relx=0.6, rely=0.5, anchor=tk.CENTER)
effect7 = tk.Button(app, text="Effect 7")
effect7.place(relx=0.4, rely=0.6, anchor=tk.CENTER)
effect8 = tk.Button(app, text="Effect 8")
effect8.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
effect9 = tk.Button(app, text="Effect 9")
effect9.place(relx=0.6, rely=0.6, anchor=tk.CENTER)

# placement of stopwatch label

label.pack(side=tk.TOP)

# placement of start listening, stop listening, and reset buttons

startButton.pack(side=tk.LEFT)
stopButton.pack(side=tk.RIGHT)
resetButton.pack(side=tk.BOTTOM)

app.mainloop()
