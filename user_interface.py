#!/usr/bin/env python3

import tkinter as tk
import tkinter.font as tkFont
from tkinter import PhotoImage
from datetime import datetime

# set UI window parameters

app = tk.Tk()
app.geometry("600x400")
app.title("Voice Modulator")
app.configure(bg='black')

# import and store the button icons

startIcon = PhotoImage(file="mic.png")
stopIcon = PhotoImage(file="stop.png")

counter = 28800
running = False


def counter_label(label):
    def count():
        if running:
            global counter

            # To manage the intial delay.
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
    if running == False:
        resetButton['state'] = 'disabled'
        label['text'] = '00:00:00'

    # If reset is pressed while the stopwatch is running.
    else:
        label['text'] = 'Starting...'

# stopwatch label


label = tk.Label(app, text="00:00:00", fg="white",
                 font="Verdana 30 bold", bg="black")

# creation of start listening, stop listening, and reset buttons

startButton = tk.Button(app,
                        command=lambda: Start(label),
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

effect1 = tk.Button(app, text="Effect 1")
effect1.place(relx=0.4, rely=0.4, anchor=tk.CENTER)
effect2 = tk.Button(app, text="Effect 2")
effect2.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
effect3 = tk.Button(app, text="Effect 3")
effect3.place(relx=0.6, rely=0.4, anchor=tk.CENTER)
effect4 = tk.Button(app, text="Effect 4")
effect4.place(relx=0.4, rely=0.5, anchor=tk.CENTER)
effect5 = tk.Button(app, text="Effect 5")
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
