# Creating a timer application that asks the user to put in a number and the software counts down
# very rudimentary timer and count down (form scratch ah haha)
import time
# imports
import tkinter as tk
# literally just using this for error management
import _tkinter
from PIL import Image
import ttkbootstrap as ttk
import threading
# FOR MY METER!!
Image.CUBIC = Image.BICUBIC

# starting to build the window
window = ttk.Window(themename="minty")
window.title("My Timer")
window.geometry("500x400")

# label for instructions
title_of_software = ttk.Label(window, text="Countdown", font='"Morning Breeze" 24')
title_of_software.pack()

# entry for numbers
number_var = tk.IntVar()
entry_line = ttk.Entry(window, textvariable=number_var)
entry_line.pack()


# update function
def count():
    """
    Actually does the counting down
    """
    countdown = number_var.get()
    circle['amountused'] = countdown
    if countdown > 0:
        entry_line['state'] = 'disabled'
        entry_line['text'] = ''
        error_mes['text'] = ''
        countdown -= 1
        circle['amountused'] = countdown
        # update the label
        number_var.set(countdown)
        # update changed on window
        window.update()
        # wait one second
        window.after(1000, count)
    if countdown <= 0:
        number_var.set(0)
        entry_line['text'] = number_var
        entry_line['state'] = 'enabled'


# button stuff
# function for button to WORK!
def go():
    """
       Activates the counting down
       """
    try:
        error_mes['text'] = ''
        countdown = number_var.get()
        if countdown <= 0:
            error_mes['text'] = "Please enter a number greater than 0!"
        else:
            count()
    except _tkinter.TclError:
        error_mes['text'] = "This isn't a number!"
        number_var.set(0)


def pause():
    """
Pauses timer, can unpause
    """
    countdown = number_var.get()
    if countdown == 0:
        pause_button.pack_forget()
    else:
        pause_button.pack()
        error_mes['text'] = 'Paused'
        time.sleep()
        print("pause!")


def stop():
    """
Stops timer i.e. ends early.
    """
    error_mes['text'] = 'Stopped'
    countdown = number_var.get()
    entry_line['text'] = number_var
    entry_line['state'] = 'enabled'


# button for pressing :)
go_button = ttk.Button(window, text="Go!", command=go)
go_button.pack(pady=10)

# button for pausing :)
pause_button = ttk.Button(window, text="Pause!", command=pause)

# button for stopping :)
stop_button = ttk.Button(window, text="Stop!", command=stop)
stop_button.pack()

# error messaging labels
error_mes = ttk.Label(window, font='"Morning Breeze" 20')
error_mes.pack()

# progress bar
circle = ttk.Meter(window, showtext=False, metersize=100)
circle.pack()

# label for actual counting down
numbers_label = ttk.Label(window, textvariable=number_var, font='"Morning Breeze" 50', padding=50)
numbers_label.pack()

# running said window
window.mainloop()
