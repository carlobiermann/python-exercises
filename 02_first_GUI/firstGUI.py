from tkinter import * 

window = Tk()

window.title("Barkeeper 4.0")

lbl = Label(window, text="Barkeeper 4.0", font=("Arial Bold",50))

lbl.grid(column=4, row=0)

window.geometry('640x480')

btn = Button(window, text="Routine starten", highlightbackground="orange", fg="blue")

btn.grid(column=0, row=1)

window.mainloop()
