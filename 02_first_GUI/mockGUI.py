from tkinter import *

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Barkeeper 4.0")

        master.geometry('640x480')
        Frame(master, bg="orange") #doesn't work

        self.label = Label(master, text="Barkeeper 4.0", font=("Arial Bold",50))
        self.label.pack()

        self.greet_button = Button(master, text="Starten", command=self.starten)
        self.greet_button.pack()

        self.close_button = Button(master, text="Beenden", command=master.quit)
        self.close_button.pack()

        Beschreibung = "Willkommen zur Beschreibung!"
        self.T = Text(master, height = 5, width = 52)
        self.T.pack()

        self.T.insert(END, Beschreibung)

    def starten(self):
        print("Programm startet")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
