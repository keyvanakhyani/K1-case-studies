from tkinter import Label,Tk,Button
from tkinter import messagebox

window = Tk()

# ========== 1. Basic Button ==========
def basic_click():
    label_result.config(text="Basic button clicked!")

Label(window, text="1. Basic Button", font=("Arial", 12, "bold")).pack(pady=(10, 5))
btn_basic = Button(window, text="Click Me!", command=basic_click)
btn_basic.pack()

# ========== Result Label ==========
label_result = Label(
    window,
    text="Click buttons to see results here!",
    font=("Arial", 11),
    bg="lightyellow",
    relief="solid",
    padx=10,
    pady=5
)
label_result.pack(fill="y", side="bottom", pady=10, padx=10)

buttton4 = Button(window,text="Click Me!",width= 20,state = "disabled")
def button_clicked():
    buttton4.config(state="normal")  
    print("Button was clicked!")

buttton1 = Button(window,text="Click Me!",width= 20,command= button_clicked)
buttton1.pack(pady= 10)

buttton4.pack(pady= 10)
buttton2 = Button(window,text="Click Me!",width= 10)
buttton2.pack(pady= 10)
buttton3 = Button(window,text="Click Me!",pady=50,padx= 50,relief="groove")
buttton3.pack(pady= 10)
button5 = Button(window, text="Hand Cursor", cursor="hand2")
button5.pack(pady= 10)
window.mainloop()

