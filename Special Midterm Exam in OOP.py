from tkinter import *

window = Tk()

window.title("Special Midterm Exam in OOP")
window.geometry("300x200+20+10")

def changecolor():
 button.configure(bg="yellow")

button = Button(window, text = "Click to Change Color", command= changecolor)
button.pack()
button.place(relx=.5, y=100, anchor="center")

window.mainloop()