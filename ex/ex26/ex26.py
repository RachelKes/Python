#! /usr/bin/python3

# demonstrates the use of Frame widgets

from tkinter import *


class FrameWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("Frame Test")
        self.top_frame = Frame(self.root)
        self.bottom_frame = Frame(self.root)
        self.l1 = Label(self.top_frame, text="Red label", fg="red")
        self.l1.pack(side="top")
        self.l2 = Label(self.top_frame, text="Green label", fg="green")
        self.l2.pack(side="top")
        self.l3 = Label(self.top_frame, text="Blue label", fg="blue")
        self.l3.pack(side="top")
        self.l4 = Label(self.bottom_frame, text="Magenta label", fg="magenta")
        self.l4.pack(side="left")
        self.l5 = Label(self.bottom_frame, text="Cyan label", fg="cyan")
        self.l5.pack(side="left")
        self.top_frame.pack()
        self.bottom_frame.pack()
        mainloop()


root = FrameWindow()
