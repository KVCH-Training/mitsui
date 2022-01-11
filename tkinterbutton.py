import tkinter as tk
from tkinter import ttk

root = tk.Tk() # trying to get specific class inside a class
root.title("displaying an Image")
root.geometry('600x400+50+50')
root.resizable(False, False)

i = 0
    
def bluemed_button():
    #print("clicked")
    global i, button
    i = i + 1
    button.configure(text = "Count: {0}".format(i))
        
button = ttk.Button(root, text = "Count: {0}".format(i), command = bluemed_button)
button.pack()
message = tk.Label(root, text = "hello World!")
message.pack()

root.mainloop()

# widget label
