from tkinter import *

window = Tk()
window.title("Special Midterm Exam in OOP")
window.geometry("300x200+20+10")

lbl = Button(window, text = "Click to Change Color", bg="White", activebackground= "Yellow")
lbl.place(relx=.5, y=100, anchor="center")

window.mainloop()