import sys
from Tkinter import *
import ttk
import tkFont as font



class Interface():
    '''Displays the main menu where the user will select what they want to search
       for and how they want it to be searched '''
    def __init__(self, root):
        self.root = root
    value = "#000"
    def lables(self):
        ''' displays the labels on the main page'''
        font.nametofont('TkDefaultFont').configure(size=15)
        MyFont = font.Font(size=20)#Changes the font size
        self.lableItems = Label(root,text="Items", font=MyFont)
        self.lableItems.configure(background='white')
        self.lableItems.pack()

        self.lableType = Label(root,text="Type")
        self.lableType.configure(background='white')
        self.lableType.place(x=100,y=70)

        self.lableTime = Label(root,text="Time")
        self.lableTime.configure(background='white')
        self.lableTime.place(x=100,y=110)

        self.lableSearching = Label(root,text="Searching")
        self.lableSearching.configure(background='white')
        self.lableSearching.place(x=60,y=150)

        self.lableSorting = Label(root,text="Sorting")
        self.lableSorting.configure(background='white')
        self.lableSorting.place(x=80,y=190)

        


    def okButton(self):
        ''' prints the values the user has choosen '''
        self.value_of_comboType = self.comboType.get()
        self.value_of_comboTime = self.comboTime.get()
        self.value_of_comboSearching = self.comboSearching.get()
        self.value_of_comboSorting = self.comboSorting.get()
        dic = { "type":self.value_of_comboType, "time":self.value_of_comboTime,
                "searching":self.value_of_comboSearching,
                "sorting":self.value_of_comboSorting,
                "colour":Interface.value
                } 
        
        print(dic["type"],dic["time"],dic["searching"],dic["sorting"],dic["colour"])

        #root.destroy()
        #root2 = Tk()
        #root2.geometry('450x450+200+200')
    

    def comboboxs(self):
          ''' displays the comboboxes on the main page'''
          self.comboType = ttk.Combobox(self.root)
          self.comboType.bind(self.comboType)
          self.comboType.place(x=190,y=80)
          #Place holder values atm
          self.comboType.config(values = ("a","b","c"))
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
        ''' displays the button on the main page'''
        self.buttonOk = Button(self.root,text="Ok", command = self.okButton)
        self.buttonOk.place(x=350,y=350)
           
           
         

    def slider(self):
        ''' displays the slider on the main page'''
        self.sliderColour = Scale(root, orient =HORIZONTAL,length=200,
          width=15,sliderlength=15,
          from_=0,to=4095,
          command=self.print_value)
       
        self.sliderColour.place(x=100,y=380)
        self.sliderColour.configure(background='white')
    def done(self):
        ''' close the main page and opens up a new one'''
        #root.destroy()
        #root2 = Tk()
        #root2.geometry('450x450+200+200') 

    def print_value(self,value):
        '''sets the value of the colours on the slider ''' 

        v = int(value)
        col = (hex(v)[2:])

        Interface.value = "#{}".format(col)

        
        # if value == "0":
        #     Interface.value = "blue"
            
        # elif value == "1":
        #     Interface.value = "black"

        # elif value == "2":
        #     Interface.value = "red"

        # elif value == "3":
        #     Interface.value = "green"    

        canvas.itemconfig(rectangleColour, fill=Interface.value)    
           
        
class Info(Interface):
    def __init__(self, root):
        #Interface.__init__(self,root)
        self.root = root
        #root = Tk()
        #gui = Interface(root)
          


    
    def okButton1(self):
     
        self.buttonOk = Button(self.root,text="Ok",command = self.close)
        self.buttonOk.place(x=350,y=350)

    def showMeAgainButton(self):
        self.buttonShowAgain = Button(self.root,text="Don't show me again")
        self.buttonShowAgain.place(x=50 , y=350)
    def close(self):
        self.buttonShowAgain.place_forget()
        self.buttonOk.place_forget()
        gui.lables()
        gui.comboboxs()
        gui.buttons()
        gui.slider()
        canvas.pack(padx=10,pady=240)
        
          
   

















root = Tk()
gui = Info(root)
gui.okButton1()
gui.showMeAgainButton()
root.configure(background='white')
font.nametofont('TkDefaultFont').configure(size=15)
#gui.lables()
#gui.comboboxs()
#gui.buttons()
#gui.slider()
canvas = Canvas(root, width=100, height=90)
rectangleColour=canvas.create_rectangle(3,7,3+100,7+100,fill=Interface.value)
canvas.configure(background='white')
canvas.pack(padx=10,pady=240)
canvas.pack_forget()

root.geometry('450x600+200+200')        
root.mainloop()
