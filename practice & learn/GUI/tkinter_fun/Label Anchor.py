import tkinter as tk

# Create main window
window = tk.Tk()
window.title("Label Anchor Example")
window.geometry("500x600")

# Title
title = tk.Label(
    window,
    text="Anchor determines text position within the label",
    font=("Arial", 12, "bold"),
    bg="lightgray"
)
title.pack(fill="x", pady=10)

# anchor='center' (default) - text in center
label1 = tk.Label(
    window,
    text="anchor='center' (default)",
    width=30,
    height=3,
    bg="lightblue",
    anchor="center",
    relief="solid",
    borderwidth=2
)
label1.pack(pady=5)

# anchor='w' (west/left)
label2 = tk.Label(
    window,
    text="anchor='w' (West/Left)",
    width=30,
    height=3,
    bg="lightgreen",
    anchor="w",
    relief="solid",
    borderwidth=2
)
label2.pack(pady=5)

# anchor='e' (east/right)
label3 = tk.Label(
    window,
    text="anchor='e' (East/Right)",
    width=30,
    height=3,
    bg="lightyellow",
    anchor="e",
    relief="solid",
    borderwidth=2
)
label3.pack(pady=5)

# anchor='n' (north/top)
label4 = tk.Label(
    window,
    text="anchor='n' (North/Top)",
    width=30,
    height=3,
    bg="lightcoral",
    anchor="n",
    relief="solid",
    borderwidth=2
)
label4.pack(pady=5)

# anchor='s' (south/bottom)
label5 = tk.Label(
    window,
    text="anchor='s' (South/Bottom)",
    width=30,
    height=3,
    bg="lightpink",
    anchor="s",
    relief="solid",
    borderwidth=2
)
label5.pack(pady=5)

# anchor='nw' (northwest/top-left)
label6 = tk.Label(
    window,
    text="anchor='nw' (Top-Left)",
    width=30,
    height=3,
    bg="lavender",
    anchor="nw",
    relief="solid",
    borderwidth=2
)
label6.pack(pady=5)

# anchor='se' (southeast/bottom-right)
label7 = tk.Label(
    window,
    text="anchor='se' (Bottom-Right)",
    width=30,
    height=3,
    bg="peachpuff",
    anchor="se",
    relief="solid",
    borderwidth=2
)
label7.pack(pady=5)

# Info
info = tk.Label(
    window,
    text="Anchor options: n, s, e, w, ne, nw, se, sw, center",
    font=("Arial", 9),
    fg="darkblue"
)
info.pack(pady=10)

window.mainloop()
