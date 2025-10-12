from tkinter import Tk, Label,Frame,Entry,Button

window = Tk()
window.title("Grid vs Pack Comparison")
window.geometry("600x400")

# ========== RIGHT SIDE: PACK EXAMPLE ==========
frame_pack = Frame(window, bg="lightgreen", relief="solid", borderwidth=10,bd = 3, highlightthickness=5,highlightbackground="red",highlightcolor="blue")

frame_pack.pack(side="right", fill="both", expand=True, padx=5, pady=5)
# Title
Label(frame_pack, text="PACK Layout", font=("Arial", 14, "bold"), bg="lightgreen").pack(pady= 10)

# Username (stacked vertically)
Label(frame_pack,text="Username:",bg="lightgreen").pack()
Entry(frame_pack,width= 20).pack(pady= 5)

# Password
Label(frame_pack,text="password:",bg="lightgreen").pack()
Entry(frame_pack,width= 20,show= "*").pack(pady= 5)

# Buttons stacked
Button(frame_pack, text="Login", width=10).pack(pady=5)
Button(frame_pack, text="Cancel", width=10).pack(pady=5)

Label(frame_pack, text="⚠️ Harder to align!\nEverything stacks vertically", bg="lightgreen", fg="darkred", justify="left").pack(pady=10)

# ========== LEFT SIDE: GRID EXAMPLE ==========

frame_grid = Frame(window, bg="lightblue", relief="solid", borderwidth=2)
frame_grid.pack(side="left", fill="both", expand=True, padx=5, pady=5)

# Title
Label(frame_grid, text="GRID Layout", font=("Arial", 14, "bold"), bg="lightblue").grid(row=0, column=0, columnspan=2, pady=10)

# Username
Label(frame_grid, text="Username:", bg="lightblue").grid(row=1, column=0, sticky="e", padx=5, pady=5)
username_entry = Entry(frame_grid, width=20)
username_entry.grid(row=1, column=1, padx=5, pady=5)

# Password
Label(frame_grid, text="Password:", bg="lightblue").grid(row=2, column=0, sticky="e", padx=5, pady=5)
password_entry = Entry(frame_grid, width=20, show="*")
password_entry.grid(row=2, column=1, padx=5, pady=5)

# Buttons in same row
Button(frame_grid, text="Login", width=10).grid(row=3, column=0, padx=5, pady=10)
Button(frame_grid, text="Cancel", width=10).grid(row=3, column=1, padx=5, pady=10)

# Info
Label(frame_grid, text="✅ Perfect for forms!\nAligned in rows & columns", 
         bg="lightblue", fg="darkgreen", justify="left").grid(row=4, column=0, columnspan=2, pady=10)

window.mainloop()
