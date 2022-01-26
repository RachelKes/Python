#! /usr/bin/python3

from tkinter import *


class RadioButton:
    def __init__(self):
        self.root = Tk()
        self.root.title("Radio Button")
        # top frame
        self.top_frame = Frame(self.root)
        self.radio_var = StringVar()
        self.radio_var.set('English')
        self.rb1 = Radiobutton(self.top_frame, text='English',
                               variable=self.radio_var, value="English", command=self.show_choice)
        self.rb2 = Radiobutton(self.top_frame, text="Spanish",
                               variable=self.radio_var, value="Spanish", command=self.show_choice)
        self.rb3 = Radiobutton(self.top_frame, text="French",
                               variable=self.radio_var, value="French", command=self.show_choice)
        self.rb4 = Radiobutton(self.top_frame, text="Arabic",
                               variable=self.radio_var, value="Arabic", command=self.show_choice)
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.rb4.pack()
        self.top_frame.pack()
        # bottom_frame
        self.bottom_frame = Frame(self.root)
        self.choice_label = Label(self.bottom_frame, text="Language:")
        self.value = StringVar()
        self.choice_value = Label(self.bottom_frame, textvariable=self.value)
        self.choice_label.pack(side="left")
        self.choice_value.pack(side="left")
        self.bottom_frame.pack()

        mainloop()

    def show_choice(self):
        language = self.radio_var.get()
        self.value.set(language)


root = RadioButton()
