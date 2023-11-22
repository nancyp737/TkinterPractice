# actual tk modules
import tkinter as tk
# imports widgets etc.
import ttkbootstrap as ttk

def add():
    """
Adds the user's text to the list
    """
    #first get the users input (in the text box)
    user_input = entry_Text.get()
    if user_input == "":
        output_Text.set("Please add text!")
    else:
        #Grab the text in the label (to save it)
        save_input = output_Label.cget("text")
        #Add in the new list
        updated_input = user_input  + "\n"+ save_input
        output_Text.set(updated_input)

    #update the size?
    window.update_idletasks()
    window.geometry(f"500x{window.winfo_reqheight()}")

# window
window = ttk.Window(themename="minty")
# Title of window (at the top)
window.title("Project #2")
# Size of the window
window.geometry("500x150")

# title on GUI
# master equals the parent
title_label = ttk.Label(master=window, text="What do you need to do today?", font='"Morning Breeze" 24')
title_label.pack()

# input field
input_frame = ttk.Frame(master=window)
entry_Text = tk.StringVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_Text)
button = ttk.Button(master=input_frame, text="Add", command=add)

entry.pack(side="left", padx=10)
button.pack(side="right")
input_frame.pack(pady=10)

#output
output_Text = tk.StringVar()
output_Label = ttk.Label(master=window,
                         text="",
                         font='"Morning Breeze" 24',
                         textvariable=output_Text)
output_Label.pack()


# running the GUI
window.mainloop()
