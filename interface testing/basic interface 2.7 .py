import sys

from Tkinter import *
import ttk

class Main:

    def Done():
            mtext = text.get()
            print(mtext)


    def __init__(self, root):
        self.text = StringVar()
        self.root = root
        self.label = Label(root,text="test1")
        self.label.place(x=100,y=50)

        self.label2 = Label(root,text="test2")
        self.label2.place(x=100,y=70)

        self.button = Button(root,text="ok", command = self.Done)
        self.button.place(x=300,y=200)



        self.textbox = Entry(root,textvariable = self.text)
        self.textbox.place(x=150, y=50)

        self.textbox1 = Entry(root)
        self.textbox1.place(x=150, y=70)
        self.text2 = StringVar()

        self.combo = ttk.Combobox(self.root, textvariable = self.text).pack()

    def Done(self):
         mtext = self.text.get()
         print(mtext)



mGui = Tk()
gui = Main(mGui)
mGui.geometry('450x450+200+200')
mGui.mainloop()
