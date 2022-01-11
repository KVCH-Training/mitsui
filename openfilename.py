import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

root = tk.Tk() # trying to get specific class inside a class
root.title("displaying an Image")
root.geometry('600x400+50+50')
root.resizable(False, False)

i = 0
    
def browse_files():
    # print("clicked")
    filedir = fd.askopenfilename(title="Open a file", initialdir = "C:/windows")
    # when we specify file path we could list all available file names in list box
        
button = ttk.Button(root, text = "Browse Files", command = browse_files)
button.pack()
message = tk.Label(root, text = "hello World!")
message.pack()

root.mainloop()

# widget label
