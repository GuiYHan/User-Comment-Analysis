import datetime
from Tkinter import Tk, Label, Button, Entry, StringVar, N, S, W, E, Text
import ttk
import os


class Dialog(object):
    def __init__(self, master):
        self.master = master
        master.title("User Comment Classify Tool")
        # hotkey
        master.bind('s', self.next_comment)

        # display title:
        title_label = Label(master, text="Comment title: ")
        title_label.grid(row=2, column=0, sticky = W + N, pady=10)

        self.title = StringVar()
        comment_title = Label(master, textvariable=self.title)
        comment_title.grid(row=2, column=3, sticky = W + N, pady=10)
        self.title.set("New Text!")

        # display contents
        body_label = Label(master, text="Comment body: ")
        body_label.grid(row=4, column=0, sticky = W + N)

        self.body = StringVar()
        comment_body = Label(master, textvariable=self.body, wraplength=300)
        comment_body.grid(row=4, column=3, sticky = W + N)
        self.body.set("New Text!")

        # hotkey label
        hotkey1 = Label(master, text="s: next, 1: interface design, 2: customer tunnel")
        hotkey1.grid(row=0, column= 0, columnspan= 4, sticky= S + W)

        hotkey2 = Label(master, text="3: functionality, 4: customer support, 5: Not Applicable")
        hotkey2.grid(row=1, column= 0, columnspan= 4, sticky= S + W)





    def next_comment(self, event=None):
        self.title.set("Next is clicked")
        self.body.set('NEXT OF THE BODYDSHADJASOIDJASIOJDIOASDJIOASSSSSDioadjioasdjioasdjasiodjIODJASIODJiod ajidioas jio')
        pass


if __name__ == "__main__":
    root = Tk()
    root.geometry("500x300")
    my_gui = Dialog(root)
    root.mainloop()

