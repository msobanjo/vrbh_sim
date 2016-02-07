import sys
from Tkinter import *
import ttk
import tkFont as font

class Interface():
    '''Displays the main menu where the user will select what they want to search
       for and how they want it to be searched '''
    def __init__(self, root):
        self.root = root

    def lables(self):
        font.nametofont('TkDefaultFont').configure(size=15)
        MyFont = font.Font(size=20)
        self.lableItems = Label(root,text="Items", font=MyFont)
        self.lableItems.pack()

        self.lableType = Label(root,text="Type")
        self.lableType.place(x=100,y=70)

        self.lableTime = Label(root,text="Time")
        self.lableTime.place(x=100,y=110)

        self.lableSearching = Label(root,text="Searching")
        self.lableSearching.place(x=60,y=150)

        self.lableSorting = Label(root,text="Sorting")
        self.lableSorting.place(x=80,y=190)

    def comboboxs(self):
          self.textItems = StringVar()
          self.comboItems = ttk.Combobox(self.root, textvariable = self.textItems)
          self.comboItems.place(x=190,y=80)
          #Place holder values atm
          self.comboItems.config(values = ("a","b","c"))
          #self.text.get()

          self.textTime = StringVar()
          self.comboTime = ttk.Combobox(self.root, textvariable = self.textTime)
          self.comboTime.place(x=190,y=120)
          self.comboTime.config(values = ("a","b","c"))

          self.textSearching = StringVar()
          self.comboSearching = ttk.Combobox(self.root, textvariable = self.textSearching)
          self.comboSearching.place(x=190,y=160)
          self.comboSearching.config(values = ("a","b","c"))

          self.textSorting = StringVar()
          self.comboSorting = ttk.Combobox(self.root, textvariable = self.textSorting)
          self.comboSorting.place(x=190,y=200)
          self.comboSorting.config(values = ("a","b","c"))

    def buttons(self):
           self.buttonOk = Button(self.root,text="Ok", command = self.done)
           self.buttonOk.place(x=350,y=300)
           
         

    def slider(self):
        self.sliderValue = StringVar()
        #Need to fix
        self.sliderColour = Scale(root, orient =HORIZONTAL,length=200,width=15,sliderlength=15,from_=0,to=10,variable=self.sliderValue,command=self.print_value)
        self.sliderColour.place(x=100,y=350)
    def done(self):
          root.destroy()
          root2 = Tk()
          root2.geometry('450x450+200+200') 
    def print_value(self):
        print self.sliderValue  
              
          
   


















root = Tk()
gui = Interface(root)
gui.lables()
gui.comboboxs()
gui.buttons()
gui.slider()
canvas = Canvas(root, width=100, height=90)
d1=canvas.create_rectangle(3,7,3+90,7+80,fill="#000088")
canvas.pack(padx=10,pady=240)
root.geometry('450x600+200+200')        
root.mainloop()
