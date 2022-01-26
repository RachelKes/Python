#! /usr/bin/python3

from tkinter import *


class ColorWindow:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title("Colors")
        self.main_window.geometry("400x200")
        self.red_label = Label(self.main_window, text="Red text", fg="red")
        self.red_label.pack()
        self.orange_label = Label(
            self.main_window, text="Orange text", fg="orange")
        self.orange_label.pack()
        self.yellow_label = Label(
            self.main_window, text="Yellow text", fg="yellow")
        self.yellow_label.pack()
        self.green_label = Label(
            self.main_window, text="Green text", fg="green")
        self.green_label.pack()
        self.blue_label = Label(self.main_window, text="Blue text", fg="blue")
        self.blue_label.pack()
        self.violet_label = Label(
            self.main_window, text="Violet text", fg="violet")
        self.violet_label.pack()
        self.cyan_label = Label(self.main_window, text="Cyan text", fg="cyan")
        self.cyan_label.pack()
        self.magenta_label = Label(
            self.main_window, text="Magenta text", fg="magenta")
        self.magenta_label.pack()
        self.brown_label = Label(
            self.main_window, text="Brown text", fg="brown")
        self.brown_label.pack()
        mainloop()


root = ColorWindow()
