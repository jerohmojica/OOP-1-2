from tkinter import *

window = Tk()

window.title("Special Midterm Exam in OOP")
window.geometry("300x200+20+10")

def demoColorChange():
 button.configure(bg="yellow")

button = Button(window, text = "Click to Change Color", command= demoColorChange)
button.pack()
button.place(relx=.5, y=100, anchor="center")

window.mainloop()