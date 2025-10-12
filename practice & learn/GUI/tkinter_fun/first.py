from tkinter import Tk,Label


window = Tk()
#window.title("Label Example")
#window.geometry("400x300")

#creating lable widget
mylable = Label(window , text = "Hello world")
#shoving it in to the screen
mylable.pack()

window.mainloop()